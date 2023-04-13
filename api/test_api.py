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
import json


# Connexion à la BDD Atlas et à ses collections
hostmongo = os.getenv("MONGO_CLIENT_HOST")
client = MongoClient(host = hostmongo, port=27017)
db = client["NYTimes"]
articles = db["Articles"]
concepts = db["Concepts"]
searchMostPopular = db["SearchMostPopular"]
searchSemantic = db["SearchSemantic"]

api = FastAPI(
    title = "New-York Times  ",
    description = "API du projet New-York Times du Bootcamp DE de février 2023",
    version = "1.0.1",
    openapi_tags=[
    {
        'name': 'Requête API New-York Times'
    },
    {
        'name': 'Requête BDD NoSQL',
    }
])

#Instanciation des objets nécessaires aux requêtes
ArticleSearch = ApiArticleSearch()
semantic = ApiSemantic("../data/raw_data/", "../data/clean_data/")

@api.get('/articleSearchApi', name="Requête ArticleSearch", tags=['Requête API New-York Times'])
def requestArticleSearch(motCle : str, nomFichier : str, filtre : Optional[str]="" ):
    ArticleSearch.request(motCle, nomFichier, filtre )
    return "Fichier bien récupéré"


@api.get('/semantic', name="Requête Semantic inconnu", tags=['Requête API New-York Times'])
def requestSemantic(conceptInconnu):
    answer = []
    if searchSemantic.find_one({"search_name" : conceptInconnu}) != None:
        for concept in searchSemantic.find({"search_name" : conceptInconnu}):
            answer.append(concept["concept_name"])
        answer.append("Obtenu via Atlas")

    else :
        semantic.search_to_clean_Json(conceptInconnu)
        with open(f"../data/clean_data/{conceptInconnu}.json", "r") as file:
            file_json = json.load(file)
        for i in file_json:
            answer.append(i["concept_name"])
    return answer

