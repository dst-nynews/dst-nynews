"""

FICHIER DE REQUETE DE L'API "Most Popular" DU NYTIMES AVEC LES REQUETES PROPOSEES PAR LA DOCUMENTATION DE L'API

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

#Requete l'API pour les plus envoyés par email, les plus partagés sur facebook et les plus populaires sur NYT
url_api_email="https://api.nytimes.com/svc/mostpopular/v2/emailed/1.json?"
url_api_facebook = "https://api.nytimes.com/svc/mostpopular/v2/shared/1/facebook.json?"
url_api_viewed = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?"
req_email = requests.get(url_api_email, params=params_req)
req_facebook = requests.get(url_api_facebook, params=params_req)
req_viewed = requests.get(url_api_viewed, params=params_req)

#Mise sous format json
email = req_email.json()
facebook = req_facebook.json()
viewed = req_viewed.json()


#Stockage dans un fichier "json_ny.json"
with open("most_emailed.json", "w") as f:
    json.dump(email,f)

with open("most_shared_facebook.json", "w") as f:
    json.dump(facebook,f)

with open("most_viewed.json", "w") as f:
    json.dump(viewed,f)