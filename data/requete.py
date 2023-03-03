"""

FICHIER DE REQUETE DE L'API "ARTICLE SEARCH" DU NYTIMES AVEC LA REQUETE PROPOSEE PAR LA DOCUMENTATION DE L'API

Requirement
    requests
    pandas
    json


1. Requête l'api à l'aide de la requête contenue dans le lien url "url_api"
2. Le transforme en JSON
3. Le copie dans un fichier nommé "json_ny.json"

"""

import requests
import pandas as pd
import json

#Requete l'API avec url_api
url_api="https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=FPi7FFInbsLWxZlVGG9AFhibkiJtXkmf"
req = requests.get(url_api)

#Mise sous format json
wb = req.json()

#Stockage dans un fichier "json_ny.json"
with open("json_ny.json", "w") as f:
    json.dump(wb,f)
