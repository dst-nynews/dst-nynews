"""

FICHIER DE REQUETE DE L'API "ARTICLE SEARCH" DU NYTIMES AVEC LA REQUETE PROPOSEE PAR LA DOCUMENTATION DE L'API

Requirement
    requests
    pandas
    json
    os
    dotenv

    Variable env: KEY_API_NYT = clé de l'api du NYT


1. Requête l'api ArticleSearch du NYT
3. Copie le résultat dans un json_raw

"""

import requests
import pandas as pd
import json
import os
import time
from dotenv import load_dotenv
load_dotenv()


class ApiArticleSearch:

    """
    Classe permettant d'instancier un objet pour requeter l'API Article Search du NYT

    Méthode :
        init
        get_article :   Se connecte à l'API "Article Search" du NYT pour la requêter
            Args : 
                Concept : le concept que l'on souhaite rechercher dans le NYT

                filter : les filtres que l'on souhaite ajouter à notre requête (notamment la date de publications des articles que l'on souhaite obtenir)

                page : Permet de choisir la page de réponse que l'on souhaite (l'API ne permettant d'obtenir qu'une page de 10 résultats par requête et 100 pages au maximum). Par défautl : la première page (0)

        to_raw_json : Insère le json obtenu après la requête dans un fichier "nom_fichier_page_n°.json"
            Args :
                wb : Le json obtenu avec la requête
                file_name : le nom du fichier dans lequel il sera stocké
                page_number : le n° de page qui viendra complet le nom du fichier

        request : Automatise la requête d'un concept pour avoir toutes les pages qui lui sont liées.

            Args :
                concept : Le concept qu'on souhaite requêter
                file_name : Le nom que l'on souhaite donner au fichers récupérés (auquel s'ajoutera le n° de la page)
                filter : Le filtre pour la requête (vide par défaut) 
    """

    def __init__(self, repo_path= None):
        self.KEY_API = os.getenv("KEY_API_NYT")
        self.BASE_URI = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="
        self.PARAM = {"api-key" : self.KEY_API}
        self.repo_path = repo_path


    def get_articles(self,concept,filter="",page=0):

        """
        Se connecte à l'API "Article Search" du NYT pour la requêter
        Args : 
            Concept : le concept que l'on souhaite rechercher dans le NYT

            filter : les filtres que l'on souhaite ajouter à notre requête (notamment la date de publications des articles que l'on souhaite obtenir)

            page : Permet de choisir la page de réponse que l'on souhaite (l'API ne permettant d'obtenir qu'une page de 10 résultats par requête et 100 pages au maximum). Par défautl : la première page (0)  
        """

        url_api= self.BASE_URI + concept

        if filter != "":
            filter_api = f"&fq={filter}"
            page_api = "&page=" + str(page)
            url_api = url_api + filter_api + page_api
            req = requests.get(url_api,  params=self.PARAM)
            print(f'Url :' + url_api)

        else:
            req = requests.get(url_api,  params=self.PARAM)
            print(f'Url :' + url_api)
        
        wb = req.json()

        return wb


    def to_raw_json(self,wb,file_name,page_number):

        """
        Insère le json obtenu après la requête dans un fichier "nom_fichier_page_n°.json"
        Args :
            wb : Le json obtenu avec la requête
            file_name : le nom du fichier dans lequel il sera stocké
            page_number : le n° de page qui viendra complet le nom du fichier
        """

        with open("data/raw_data/"+file_name+ "_Page_" + str(page_number)+".json", "w") as f:
            json.dump(wb,f)


    def request(self,concept,file_name, filter=""):
        """
        Automatise la requête d'un concept pour avoir toutes les pages qui lui sont liées.

        Args :
            concept : Le concept qu'on souhaite requêter
            file_name : Le nom que l'on souhaite donner au fichers récupérés (auquel s'ajoutera le n° de la page)
            filter : Le filtre pour la requête (vide par défaut) 
        """

        req_dico = self.get_articles(concept,filter)

        try:
            hits = req_dico["response"]["meta"]["hits"]

        except KeyError:
            return print(f"Request failed. Please try another concept or filter")
            
        
        nbr_pages = hits//10
        page = 0
        self.to_raw_json(req_dico,file_name,page)

        if nbr_pages >100:
            print(f'N° of pages :{nbr_pages}. API limited to 100 pages.')


        else:
            print(page)

            for i in range (1, nbr_pages +1):
                if i < 100 and i < nbr_pages+1:
                    page = page + 1
                    print(page)
                    req_dico = self.get_articles(concept,filter,page)
                    self.to_raw_json(req_dico,file_name,page)
                    time.sleep(11)
                    i+=1
        
            print("done")





# TEST
daterange = pd.date_range(start="2019,31,12", end="2023,07,02", freq="m")

test = ApiArticleSearch()
for i in daterange:
    date= i.strftime("%Y-%m-%d")
    concept = "covid"
    fichier_name = f"Covid{date}"
    filtre = f"pub_date:({date})"
    test.request(concept,fichier_name,filtre)
    time.sleep(5)