"""

FICHIER DE REQUETE DE L'API "Semantic" DU NYTIMES AVEC LES REQUETES PROPOSEES PAR LA DOCUMENTATION DE L'API

Requirement
    requests
    pandas
    json
    os
    dotenv

    Variable env: KEY_API_NYT = clé de l'api du NYT


1. Requête l'api semantic à l'aide de la méthode spécifique type et concept
2. Le transforme en JSON et le copie dans un fichier de type rawData nommé "conceptRaw.json"
3. Obtient une liste d'éléments à partir du concept requété
4. Copie la liste d'éléments filtrée dans un JSON propre nommé "conceptClean.json"

"""

import requests
import pandas as pd
import json
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

key_api = os.getenv("KEY_API_NYT")
params_req = {"api-key" : key_api, "fields" : "article_list"}



def getConceptDes(concept):
    conceptName=concept
    #url_api_concept = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_des/{conceptName}.json?"
    url_api_concept = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_des/Coronavirus (2019-nCoV).json?"
    requestConcept = requests.get(url_api_concept, params=params_req)
    return requestConcept



#Stockage dans un fichier "ConceptTest.json"
def writeRawConceptToJSON(requestConcept):
    conceptJSON = requestConcept.json()
    with open("conceptRaw.json", "w") as conceptJSONDoc:
        json.dump(conceptJSON, conceptJSONDoc)
        return conceptJSON


#Obtention des éléments du concept
#Fonction qui prend en argument un concept (string) de type des (descriptor) et qui renvoi certains éléments du concept suivant l'API semantic du NY Times. 
#Les éléments renvoyés sont les suivants:
# concept_id
#-concept_name
#-concept_created
#-concept_status
#-concept_type
#-concept_uri
#-article_list:
#   -body
#   -concepts:
#       -nydt_des[]
#       -nydt_geo[]
#       -nydt_org[]
#       -nydt_per[]
#   -date
#   -title
#   -type_of_material
#   -url
def getElementsFromConcept(rawJSONConcept):
    results = rawJSONConcept['results']
    
    conceptPropre = {}

    concept_id = results[0]['concept_id']
    concept_name = results[0]['concept_name']
    concept_created = results[0]['concept_created']
    concept_status = results[0]['concept_status']
    concept_type = results[0]['concept_type']
    concept_uri = results[0]['concept_uri']

    print(concept_id)
    #pprint(rawJSONConcept)

    #conceptPropre["concept_id" : "results[0]['concept_id']"]
    #conceptPropre["concept_name" : concept_name]
    pprint(conceptPropre)
    
    return conceptPropre
    
    

conceptString = getConceptDes("Coronavirus (2019-nCoV)")
print(conceptString)
rawJSON = writeRawConceptToJSON(conceptString)
#print(rawJSON)
dictConceptPropre = getElementsFromConcept(rawJSON)
pprint(dictConceptPropre)