import os
import sys
sys.path.insert(0,".")
from fastapi import APIRouter
from typing import Optional
from sourcing.requete_semantic import ApiSemantic
from db.bdd_write import Bdd
import json

# Instanciate a router for this endpoint
routeSe = APIRouter()

# Import ApiArticleSearch to request NYT API
semantic = ApiSemantic("data/raw_data/", "data/clean_data/")
bddSemantic = Bdd("data/clean_data/")
bbdconcepts = Bdd("data/clean_data/")


# Connection to mongodb collection
from pymongo import MongoClient
hostmongo = os.getenv("MONGO_CLIENT_HOST")
client = MongoClient(host = hostmongo, port=27017)
db = client["NYTimes"]
searchSemantic = db["SearchSemantic"]
concepts = db["Concepts"]



# Retourne le fichier json de la requête semantic utilisée avec une chaine de caractères 
@routeSe.get('/unknow', name='Requête json semantic chaine de caractère', tags=['Semantic'])
async def resquestSemanticUnknow(unknow):
    a = semantic.search_concept(unknow)
    answer = a.json()
    return answer


# Requête qui renvoie le json d'une requête avec un concept officiel et son type
@routeSe.get('/concept', name ="Requête concept officel NYT", tags=["Semantic"])
async def requestKnownConcept(knownconcept,conceptType):
    if concepts.find_one({"concept_name" : knownconcept}) != None:
        return concepts.find_one({"concept_name" : knownconcept})
    else :
        semantic.type_concept_to_clean_Json(knownconcept,conceptType)
        try:
            with open(f"data/clean_data/{knownconcept}.json", "r") as file:
                file_json = json.load(file)
            bddSemantic.insert_mongoDB(f"{knownconcept}.json",concepts)
            return file_json
        except: 
            return "Oups, il y a eu un problème !"
        
    
# Requête qui renvoie une liste de concepts et de leur type officiels lié à un mot clé
@routeSe.get('/unknow/list', name="Requête Semantic inconnu", tags=['Semantic'])
async def requestSemantic(conceptInconnu):
    answer = []
    if concepts.find_one({"concept_name" : conceptInconnu}) != None:
        return concepts.find_one({"concept_name" : conceptInconnu})
    elif searchSemantic.find_one({"search_name" : conceptInconnu}) != None:
        for concept in searchSemantic.find({"search_name" : conceptInconnu}):
            answer.append((concept["concept_name"],concept["concept_type"]) )

    else :
        semantic.search_to_clean_Json(conceptInconnu)
        file_json = bddSemantic.import_json(f"{conceptInconnu}.json")
        for i in file_json:
            if type(i) != dict:
                return "Aucun concept avec ce mot"
            else:
                answer.append((i["concept_name"], i["concept_type"] ))
        bddSemantic.insert_mongoDB(f"{conceptInconnu}.json",searchSemantic)
    return answer