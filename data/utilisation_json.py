"""
FICHIER PERMETTANT DE JOUER AVEC LES DONNEES OBTENUES PAR LE REQUETE DU FICHIER "requete.py" et stocké dans "json_ny.json".

!!! Si vous n'avez pas de fichier "json_ny.json". Lancez le fichier "requete.py" pour utiliser celui-ci.

Requirement:
    pandas
    json

    
Jouez avec les lignes # pour activer les print()


df : contient les données telles qu'elles sont dans le json en sortie de l'API
status : Etat de la requête (à vérifier), ok si tout s'est bien passé
copyright : Le copyright des données disant qu'elles appartiennent au NY
response : Les données et le méta données de la requête à proprement parler 



"""

import pandas as pd
import json


#Gestion du fichier json et du dataframe
with open("json_ny.json", "r") as rf:
    obj_pyth = json.load(rf)

df = pd.DataFrame(obj_pyth)

#On regarde le nom des colonnes du DataFrame (*spoiler* il y en a 3 : status, copyright, response)
#print(df.columns)

status = df["status"]
copyright = df['copyright']
response = df["response"] 


#On regarde ce que contient la séries response (spoiler : les données des article dans "docs" et les meta données dans "meta")
#print(response)

#Nombre d'articles
#print(len(response["docs"]))





#Structure des données d'un article

article1 = response["docs"][0] 

contenu_article1 = [] #On récupère le nom des clé du dico pour connaitre la structure des données
for key in article1:
    contenu_article1.append(key)
#print(contenu_article1)




#STRUCTURE DONNEES STATUS
#print(status)


#STRUCTURE DONNEES COPYRIGHT
#print(copyright)
#print(len(copyright))