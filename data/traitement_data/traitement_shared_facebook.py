"""


FICHIER PERMETTANT DE JOUER AVEC LES DONNEES OBTENUES PAR LE REQUETE DU FICHIER "requete_mostpopular.py" ET STOCKE DANS "most_shared_facebook.json".

!!! Si vous n'avez pas de fichier "most_shared_facebook.json". Lancez le fichier "requete_mostpopular.py" pour le créer.


Requirement:
    pandas
    json

    
Jouez avec les lignes # pour activer les print()


"""

import pandas as pd
import json


#Gestion du fichier json et du dataframe
with open("most_shared_facebook.json", "r") as rf:
    obj_pyth = json.load(rf)

df = pd.DataFrame(obj_pyth)

#Nom des colonnes du DataFrame (*spoiler* il y en a 4 : status, copyright, ,num_results, results)
#print(df.columns)

status = df["status"]
copyright = df["copyright"]
num_results = df["num_results"] 
results = df["results"]

#Contenu de results (spoiler : 20 dictionnaires contenant les données)
#print(results)

#Liste des clés du premier dictionnaire : ['uri', 'url', 'id', 'asset_id', 'source', 'published_date', 'updated', 'section', 'subsection', 'nytdsection', 'adx_keywords', 'column', 'byline', 'type', 'title', 'abstract', 'des_facet', 'org_facet', 'per_facet', 'geo_facet', 'media', 'eta_id']
contenu_dictionnaire = []
for key in results[0]:
    contenu_dictionnaire.append(key)
#print(contenu_dictionnaire)