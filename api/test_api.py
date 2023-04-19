import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import sys
sys.path.insert(0,"..")
from sourcing.request_article_search import ApiArticleSearch
from sourcing.requete_semantic import ApiSemantic
from db.bdd_write import Bdd
import json


# Connexion à la BDD Atlas et à ses collections
hostmongo = os.getenv("MONGO_CLIENT_HOST")
client = MongoClient(host = hostmongo, port=27017)
db = client["NYTimes"]
articles = db["Articles"]
concepts = db["Concepts"]
searchMostPopular = db["SearchMostPopular"]
searchSemantic = db["SearchSemantic"]

# Création de l'API
api = FastAPI(
    title = "New-York Times  ",
    description = "API du projet New-York Times du Bootcamp DE de février 2023",
    version = "1.0.1",
    openapi_tags=[
    {
        'name': 'Requête cas métier n°1'
    },
    {
        'name': 'Requête cas métier n°2',
    }
])

#Instanciation des objets nécessaires aux requêtes
ArticleSearch = ApiArticleSearch()
semantic = ApiSemantic("../data/raw_data/", "../data/clean_data/")
bddSemantic = Bdd("../data/clean_data/")
bbdconcepts = Bdd("../data/clean_data/")



# Requêtes ArticleSearch
@api.get('/articleSearchApi', name="Requête ArticleSearch", tags=['Requête cas métier n°1'])
def requestArticleSearch(motCle : str, nomFichier : str, filtre : Optional[str]="" ):
    ArticleSearch.request(motCle, nomFichier, filtre )
    return "Fichier bien récupéré"

# Requête qui renvoie une liste de concepts officiels lié à un mot clé
@api.get('/semantic', name="Requête Semantic inconnu", tags=['Requête cas métier n°2'])
def requestSemantic(conceptInconnu):
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

# Requête information concept officiel NYT
@api.get('/concept', name ="Requête concept officel NYT", tags=["Requête cas métier n°2"])
def requestKnownConcept(knownconcept,conceptType):
    if concepts.find_one({"concept_name" : knownconcept}) != None:
        return concepts.find_one({"concept_name" : knownconcept})
    else :
        semantic.type_concept_to_clean_Json(knownconcept,conceptType)
        with open(f"../data/clean_data/{knownconcept}.json", "r") as file:
            file_json = json.load(file)
        bddSemantic.insert_mongoDB(f"{knownconcept}.json",concepts)
        return file_json