"""

FICHIER DE REQUETE DE L'API "Semantic" DU NYTIMES AVEC LES REQUETES PROPOSEES PAR LA DOCUMENTATION DE L'API

Requirement
    requests
    pandas
    json
    os
    dotenv

    Variable env: KEY_API_NYT = clé de l'api du NYT

Deux cas de figure:
A: requête avec type et name précis:
    1. Requête l'api semantic à l'aide de la méthode spécifique type et concept
    2. Le transforme en JSON et le copie dans un fichier de type rawData nommé "conceptRaw.json"
    3. Obtient une liste d'éléments clean à partir du concept requété
    4. Copie la liste d'éléments filtrée dans un JSON propre nommé "Concept.json"

B: requête avec recherche string:
    1. Requête l'api semantic à l'aide de la méthode search qui renvoi une liste de concept qui contiennent le string recherché
    2. Le transforme en JSON et le copie dans un fichier de type rawData nommé "SearchRaw.json". C'est une liste
    3. Clean la liste JSON raw en une liste de dictionnaire clean
    4. Copie la liste d'éléments filtrée dans un JSON propre nommé "Search.json" ou Search est le string recherché par le user

Pour chacun des cas de figure, la classe contient une fonction d'orchestration qui va appeler successivement les fonctions correspondantes à chacunes de ces 4 étapes.

"""

import requests
import pandas as pd
import json
import os
import time
from pprint import pprint
from dotenv import load_dotenv
from typing import Dict, Optional
load_dotenv()

class ApiSemantic:
    def __init__(self, repo_path_raw: Optional[str] = None, repo_path_clean: Optional[str] = None) -> None:
        """Instanciate a connection to fetch data from an API of the NY Times.
        Args:
            repo_path (Optional[str], optional): Path to storage directory.
        """

        self.key_api = os.getenv("KEY_API_NYT")
        self.params_req = {"api-key" : self.key_api, "fields" : "article_list"}
        self.repo_path_raw = repo_path_raw
        self.repo_path_clean = repo_path_clean



# A: requête type/concept
    # étape 1
    def get_concept(self, concept, type):
        """
        On utilise l'api semantic avec la méthode GET /name/{concept-type}/{specific-concept}.json
        """
        #print(concept)
        #print(type)
        
        conceptName = concept
        conceptType = type+"/"

        url_base = "http://api.nytimes.com/svc/semantic/v2/concept/name/"
        url_end = ".json?"
        url_api_concept = url_base + conceptType + conceptName + url_end
        print(url_api_concept)
        #url_api_concept = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_des/Coronavirus (2019-nCoV).json?"
        requestConcept = requests.get(url_api_concept, params= self.params_req)
        return requestConcept

    # étape 2
    def write_raw_concept_to_JSON(self, requestConcept, rawJsonName):
        """
        Stockage dans un fichier "ConceptRaw.json"
        """
        conceptJSON = requestConcept.json()
        with open(self.repo_path_raw+"conceptRaw_"+rawJsonName+".json", "w") as conceptJSONDoc:
            json.dump(conceptJSON, conceptJSONDoc)
            return conceptJSON

    # étape 3    
    def get_elements_from_concept(self, rawJSONConcept):
        """
        Obtention des éléments du concept
        Fonction qui prend en argument un concept (string) et qui renvoi certains éléments du concept suivant l'API semantic du NY Times. 
        Les éléments renvoyés sont les suivants:
        -concept_id
        -concept_name
        -concept_created
        -concept_status
        -concept_type
        -concept_uri
        -nb_articles
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

        conceptPropre["_id"] = results[0]['concept_id']
        conceptPropre["concept_name"] = results[0]['concept_name']
        conceptPropre["concept_created"] = results[0]['concept_created']
        conceptPropre["concept_status"] = results[0]['concept_status']
        conceptPropre["concept_type"] = results[0]['concept_type']
        conceptPropre["concept_uri"] = results[0]['concept_uri']
        conceptPropre["nb_articles"] = results[0]['article_list']['total']
        conceptPropre["article_list"] = article_list_clean

        return conceptPropre
    
    # étape 4
    def write_clean_concept_to_JSON(self, cleanConcept, jsonName):
        with open(self.repo_path_clean+jsonName+".json", "w") as cleanConceptJSONDoc:
            json.dump(cleanConcept, cleanConceptJSONDoc)


    # Fonction d'orchestration pour la requête type/concept
    def type_concept_to_clean_Json(self, concept, type):
        """
        Fonction complète qui récupère le concept de type descriptor/geo/org/per et crée et stock le JSON clean avec ce concept
        """
        #conceptString = getConceptDes(concept)
        conceptString = self.get_concept(concept, type)
        #print(conceptString)

        rawJSON = self.write_raw_concept_to_JSON(conceptString, concept)
        #print(rawJSON)

        if (rawJSON['num_results'] != 0):
            dictConceptPropre = self.get_elements_from_concept(rawJSON)
            #pprint(dictConceptPropre)
            self.write_clean_concept_to_JSON(dictConceptPropre, concept)
        else:
            print("Le concept: " + concept +  " n'a pas été trouvé dans l'API du NY Times")



# B: requête search
    # étape 1    
    def search_concept(self, concept):
        """
        On utilise l'api semantic avec la méthode GET /search.json
        """
        #print(concept)
        
        conceptName = concept

        url_base = "http://api.nytimes.com/svc/semantic/v2/concept/search.json?query="
        url_api_concept = url_base + conceptName
        print(url_api_concept)
        searchConcept = requests.get(url_api_concept, params=self.params_req)
        return searchConcept

    # étape 2
    def write_raw_search_to_JSON(self, requestSearch, rawJsonName):
        """
        Stockage dans un fichier "ConceptRaw.json"
        """
        searchJSON = requestSearch.json()
        with open(self.repo_path_raw+"searchRaw_"+rawJsonName+".json", "w") as searchJSONDoc:
            json.dump(searchJSON, searchJSONDoc)
            return searchJSON

    # étape 3
    def get_elements_from_search(self, rawJSONSearch, searchName):
        """
        On prend en paramètre la liste brut des résultats de la recherche et on renvoi un tableau de dictionnaire de concept.
        Chacun de ces dictionnaires aura les éléments suivants:
        -concept_id
        -concept_name
        -concept_created
        -concept_type
        """
        
        nombre_resultats = rawJSONSearch['num_results']
        #print(nombre_resultats)
        results = rawJSONSearch['results']
        
        clean_concepts = []

        for index, concept in zip(range(nombre_resultats), results):
            c = {}
            c["search_name"] = searchName
            c['_id'] = concept['concept_id']
            c['concept_name'] = concept['concept_name']
            c['concept_created'] = concept['concept_created']
            c['concept_type'] = concept['concept_type']
            if(c['concept_type'] in ('nytd_des','nytd_org','nytd_per','nytd_geo')):
                clean_concepts.append(c)
                
        return clean_concepts


    # étape 4
    def write_clean_search_to_JSON(self, cleanSearch, jsonName):
        with open(self.repo_path_clean+jsonName+".json", "w") as cleanSearchJSONDoc:
            json.dump(cleanSearch, cleanSearchJSONDoc)


    # Fonction d'orchestration pour la requête search
    def search_to_clean_Json(self, searchString):
        """
        Fonction complète qui récupère le string de recherche et crée et stock le JSON clean avec la liste des concepts contenants ce mot
        """
        searchConcept1 = self.search_concept(searchString)
        rawJSONSearch1 = self.write_raw_search_to_JSON(searchConcept1, searchString)
        cleanSearch1 = self.get_elements_from_search(rawJSONSearch1, searchString)
        #print(cleanSearch1)
        self.write_clean_search_to_JSON(cleanSearch1, searchString)



# test requête type/concept
semantic = ApiSemantic("../data/raw_data/semantic/", "../data/clean_data/semantic/")

typeDes = "nytd_des"
typeGeo = "nytd_geo"
typePer = "nytd_per"
typeOrg = "nytd_org"

conceptDes1 = "Coronavirus (2019-nCoV)"
#semantic.get_concept(conceptDes1,typeDes)
semantic.type_concept_to_clean_Json(conceptDes1, typeDes)

#conceptDes2 = "Baseball"
#semantic.type_concept_to_clean_Json(conceptDes2, typeDes)

conceptGeo = "Acapulco (Mexico)"
semantic.type_concept_to_clean_Json(conceptGeo, typeGeo)

conceptPer = "Abbas, Mahmoud"
semantic.type_concept_to_clean_Json(conceptPer, typePer)

conceptOrg = "Chicago White Sox"
semantic.type_concept_to_clean_Json(conceptOrg, typeOrg)

#time.sleep(10)

#conceptInexistant = "Baskurt, Can"
#semantic.type_concept_to_clean_Json(conceptInexistant, typeDes)


# test requête search
searchString = "Coronavirus"
semantic.search_to_clean_Json(searchString)