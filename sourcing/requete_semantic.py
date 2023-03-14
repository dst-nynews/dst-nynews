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


def getConcept(concept, type):
    """
    On utilise l'api semantic avec la méthode GET /name/{concept-type}/{specific-concept}.json
    """
    print(concept)
    print(type)
    
    conceptName = concept
    conceptType = type+"/"

    url_base = "http://api.nytimes.com/svc/semantic/v2/concept/name/"
    url_end = ".json?"
    url_api_concept = url_base + conceptType + conceptName + url_end
    print(url_api_concept)
    #url_api_concept = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_des/Coronavirus (2019-nCoV).json?"
    requestConcept = requests.get(url_api_concept, params=params_req)
    return requestConcept


def searchConcept(concept):
    """
    On utilise l'api semantic avec la méthode GET /search.json
    """
    print(concept)
    
    conceptName = concept

    url_base = "http://api.nytimes.com/svc/semantic/v2/concept/search.json?query="
    url_api_concept = url_base + conceptName
    print(url_api_concept)
    searchConcept = requests.get(url_api_concept, params=params_req)
    return searchConcept


def writeRawConceptToJSON(requestConcept, rawJsonName):
    """
    Stockage dans un fichier "ConceptRaw.json"
    """
    conceptJSON = requestConcept.json()
    with open("../data/raw_data/conceptRaw_"+rawJsonName+".json", "w") as conceptJSONDoc:
        json.dump(conceptJSON, conceptJSONDoc)
        return conceptJSON



def getElementsFromConcept(rawJSONConcept):
    """
    Obtention des éléments du concept
    Fonction qui prend en argument un concept (string) de type des (descriptor) et qui renvoi certains éléments du concept suivant l'API semantic du NY Times. 
    Les éléments renvoyés sont les suivants:
     -concept_id
     -concept_name
     -concept_created
     -concept_status
     -concept_type
     -concept_uri
     -article_list:
        -body
        -concepts:
            -nytd_des[]
            -nytd_geo[]
            -nytd_org[]
            -nytd_per[]
        -date
        -title
        -type_of_material
        -url        
    """
    results = rawJSONConcept['results']
    #pprint(rawJSONConcept)

    article_list_raw = results[0]['article_list']['results']
    #print(len(article_list_raw))

    article_list_clean = []

    #boucler sur les articles de la article_list avec limite sur le length pour pas aller out of bounds
    for index, article in zip(range(len(article_list_raw)), article_list_raw):
        #pprint(article['title'])
        article = {}
        article['body'] = article_list_raw[0]['body']
        article['date'] = article_list_raw[0]['date']
        article['title'] = article_list_raw[0]['title']
        article['type_of_material'] = article_list_raw[0]['type_of_material']
        article['url'] = article_list_raw[0]['url']
        article['linkedConcepts'] = article_list_raw[0]['concepts']
        article_list_clean.append(article)
    
    #print(len(article_list_clean))
    #pprint(article_list_clean)

    conceptPropre = {}

    conceptPropre["concept_id"] = results[0]['concept_id']
    conceptPropre["concept_name"] = results[0]['concept_name']
    conceptPropre["concept_created"] = results[0]['concept_created']
    conceptPropre["concept_status"] = results[0]['concept_status']
    conceptPropre["concept_type"] = results[0]['concept_type']
    conceptPropre["concept_uri"] = results[0]['concept_uri']
    conceptPropre["article_list"] = article_list_clean

    return conceptPropre
    

def writeCleanConceptToJSON(cleanConcept, jsonName):
    with open(jsonName+".json", "w") as cleanConceptJSONDoc:
        json.dump(cleanConcept, cleanConceptJSONDoc)




def descriptorConceptToCleanJson(concept, type):
    """
    Fonction complète qui récupère le concept de type descriptor et crée et stock le JSON clean avec ce concept
    """
    #conceptString = getConceptDes(concept)
    conceptString = getConcept(concept, type)
    print(conceptString)

    rawJSON = writeRawConceptToJSON(conceptString, concept)
    #print(rawJSON)

    if (rawJSON['num_results'] != 0):
        dictConceptPropre = getElementsFromConcept(rawJSON)
        #pprint(dictConceptPropre)
        writeCleanConceptToJSON(dictConceptPropre, concept)
    else:
        print("Le concept: " + concept +  " n'a pas été trouvé dans l'API du NY Times")


typeDes = "nytd_des"
typeGeo = "nytd_geo"
typePer = "nytd_per"
typeOrg = "nytd_org"

conceptDes1 = "Coronavirus (2019-nCoV)"
descriptorConceptToCleanJson(conceptDes1, typeDes)

conceptDes2 = "Baseball"
descriptorConceptToCleanJson(conceptDes2, typeDes)

conceptGeo = "Acapulco (Mexico)"
descriptorConceptToCleanJson(conceptGeo, typeGeo)

conceptPer = "Abbas, Mahmoud"
descriptorConceptToCleanJson(conceptPer, typePer)

conceptOrg = "Chicago White Sox"
descriptorConceptToCleanJson(conceptOrg, typeOrg)

conceptInexistant = "Baskurt, Can"
descriptorConceptToCleanJson(conceptInexistant, typePer)