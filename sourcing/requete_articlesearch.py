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


def get_articles(concept,filter="",page=0):
    url_api="https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+ concept

    if filter != "":
        filter_api = f"&fq={filter}"
        page_api = "&page=" + str(page)
        url_api = url_api + filter_api + page_api
        req = requests.get(url_api,  params=params_req)
        print(f'Url utilisée :' + url_api)

    else:
        req = requests.get(url_api,  params=params_req)
        print(f'Url utilisée :' + url_api)
    
    wb = req.json()

    return wb


def stockage_fichier(wb,fichier_name,page_number):
    with open("../data/raw_data/"+fichier_name+ "_Page_" + str(page_number)+".json", "w") as f:
        json.dump(wb,f)


def requete(concept,filter,fichier_name):
    req_dico = get_articles(concept,filter)
    hits = req_dico["response"]["meta"]["hits"]
    nbr_pages = hits//10
    page = 0
    stockage_fichier(req_dico,fichier_name,page)

    if nbr_pages >100:
        print(f'L\'API ne propose que les 100 premières pages, or votre recherche comporte {nbr_pages} pages. Si vous souhaitez récupérer les données des pages 101 à {nbr_pages}, il vous faut mieux préciser votre recherche')

    print(page)

    for i in range (1, nbr_pages +1):
        if i < 10 and i < nbr_pages+1:
            page = page + 1
            print(page)
            req_dico = get_articles(concept,filtre,page)
            stockage_fichier(req_dico,fichier_name,page)
            i+=1
    
    print("données récupées")


# TEST
concept = "covid"
fichier_name = "covid20192023"
filtre = "pub_year:2019 OR 2020 OR 2021 OR 2022 OR 2023"
requete(concept,filtre,fichier_name)