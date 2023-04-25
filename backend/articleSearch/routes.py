from fastapi import APIRouter
from database import mongodb
from sourcing.request_article_search import ApiArticleSearch
from typing import Optional


# Instanciate a router for this endpoint
routeAs = APIRouter()

# Import ApiArticleSearch to request NYT API
ArticleSearch = ApiArticleSearch()

# Connection to mongodb collection
articles = mongodb["Articles"]

# Requêtes ArticleSearch
@routeAs.get('/articleSearchApi', name="Requête ArticleSearch JSON", tags=['Article Search'])
def requestArticleSearch(keyWord : str, fileName : str, filter : Optional[str]="" ):
    ArticleSearch.request(keyWord, fileName, filter)
    return "Fichier(s) bien récupéré(s)"