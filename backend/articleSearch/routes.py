import os
import sys
sys.path.insert(0,".")
from fastapi import APIRouter
from sourcing.request_article_search import ApiArticleSearch
from typing import Optional
from pymongo import MongoClient
hostmongo = os.getenv("MONGO_CLIENT_HOST")
client = MongoClient(host = hostmongo, port=27017)
db = client["NYTimes"]

# Instanciate a router for this endpoint
routeAs = APIRouter()

# Import ApiArticleSearch to request NYT API
ArticleSearch = ApiArticleSearch()

# Connection to mongodb collection
articles = db["Articles"]

# Requêtes ArticleSearch
@routeAs.get('/articleSearchApi', name="Requête ArticleSearch JSON", tags=['Article Search'])
def requestArticleSearch(keyWord : str, fileName : str, filter : Optional[str]="" ):
    ArticleSearch.request(keyWord, fileName, filter)
    return "Fichier(s) bien récupéré(s)"