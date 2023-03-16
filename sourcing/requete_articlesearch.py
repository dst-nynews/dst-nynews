"""

FICHIER DE REQUETE DE L'API "ARTICLE SEARCH" DU NYTIMES AVEC LA REQUETE PROPOSEE PAR LA DOCUMENTATION DE L'API

Requirement
    requests
    pandas
    json
    os
    dotenv

    Variable env: KEY_API_NYT = clé de l'api du NYT


1. Requête l'api à l'aide de la requête contenue dans le lien url "url_api"
2. Le transforme en JSON
3. Le copie dans un fichier nommé "json_ny.json"

"""

import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv
load_dotenv()

key_api = os.getenv("KEY_API_NYT")
params_req = {"api-key" : key_api}


def get_articles(concept,filter=""):
    url_api="https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+ concept

    if filter != "":
        filter_api = f"&fq={{{filter}}}"
        url_api = url_api + filter_api
        req = requests.get(url_api,  params=params_req)
        print(url_api)

    else:
        req = requests.get(url_api,  params=params_req)
        print(url_api)
    return req


#Mise sous format json

def articles_json(req,concept):
    wb = req.json()
    with open("../data/raw_data/"+concept+".json", "w") as f:
        json.dump(wb,f)


concept = "election"
election = get_articles(concept)
articles_json(election,concept)