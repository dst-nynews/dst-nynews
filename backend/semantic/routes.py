import sys
sys.path.insert(0,".")
from fastapi import APIRouter
from database import mongodb
from typing import Optional
from sourcing.requete_semantic import ApiSemantic
from db.bdd_write import Bdd
import json

# Instanciate a router for this endpoint
routeSe = APIRouter()

# Import ApiArticleSearch to request NYT API
semantic = ApiSemantic("../data/raw_data/", "../data/clean_data/")
bddSemantic = Bdd("../data/clean_data/")
bbdconcepts = Bdd("../data/clean_data/")


# Connection to mongodb collection
searchSemantic = mongodb["SearchSemantic"]
concepts = mongodb["Concepts"]



# Retourne le fichier json de la requête semantic utilisée avec une chaine de caractères 
@routeSe.get('/unknow', name='Requête json semantic chaine de caractère', tags=['Semantic'])
def resquestSemanticUnknow():
    pass


# Requête qui renvoie le json d'une requête avec un concept officiel et son type
@routeSe.get('/concept', name ="Requête concept officel NYT", tags=["Semantic"])
def requestKnownConcept(knownconcept,conceptType):
    if concepts.find_one({"concept_name" : knownconcept}) != None:
        return concepts.find_one({"concept_name" : knownconcept})
    else :
        semantic.type_concept_to_clean_Json(knownconcept,conceptType)
        with open(f"../data/clean_data/{knownconcept}.json", "r") as file:
            file_json = json.load(file)
        bddSemantic.insert_mongoDB(f"{knownconcept}.json",concepts)
        return file_json
    
    
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
            answer.append(i["concept_name"])
        bddSemantic.insert_mongoDB(f"{conceptInconnu}.json",searchSemantic)
    return answer

