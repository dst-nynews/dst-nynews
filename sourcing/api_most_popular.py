"""Get the 20 most popular articles of the NY Times.

Fetch data by making a `GET` request to an endpoint of the Most Popular API,
and store the response as a JSON file in a folder.

It needs:
    - an API key,
    - the endpoint to call in ["emailed", "shared", "viewed"],
    - the period of days in [1, 7, 30],
    - the path to a storage folder (optional).

The endpoint gives the metric on which is measured the popularity of articles.
"""

import json
import os
from datetime import date
from typing import Dict, Optional
from urllib.parse import urljoin
import re

import requests

# Fetch environment variables
from dotenv import load_dotenv

load_dotenv()


class ApiMostPopular:
    def __init__(self, repo_path: Optional[str] = None) -> None:
        """Instanciate a connection to fetch data from an API of the NY Times.

        Args:
            repo_path (Optional[str], optional): Path to storage directory.
        """

        self.KEY_API = os.environ["KEY_API_NYT"]
        self.BASE_URI = "https://api.nytimes.com/"
        self.repo_path = repo_path

    def get_data(self, endpoint: str, period: int) -> Dict[str, str]:
        """GET request to an endpoint of the API.

        Args:
            endpoint (str): The endpoint to call,
                            in ["emailed", "shared", "viewed"].
            period (int): The period of days, in [1, 7, 30].

        Returns:
            dict[str, str]: Response as a JSON.
        """

        url_path = f"/svc/mostpopular/v2/{endpoint}/{period}.json"
        url = urljoin(self.BASE_URI, url_path)
        params = {"api-key": self.KEY_API}

        response = requests.get(url, params=params)
        # print(response.status_code)

        return response.json()

    def save_data(self, data: Dict[str, str], endpoint: str, period: int) -> None:
        """Save response in a JSON file

        Args:
            data (dict[str, str]): Response as a JSON.
            endpoint (str): The endpoint to call,
                            in ["emailed", "shared", "viewed"].
            period (int): The period of days, in [1, 7, 30].
        """

        _today = date.today()
        filename = f"most_popular_{endpoint}_{period}d_{_today.month}_{_today.day}.json"
        if self.repo_path:
            filepath = self.repo_path + filename
        else:
            filepath = f"../data/raw_data/most_popular/{filename}"

        with open(filepath, "w") as file:
            json.dump(data, file)

    
    def import_json(self,file_path):
        """
         Importe le fichier .json raw à traiter dans une variable
            Arg : le chemin du fichier 
        """
        with open(file_path, "r") as file:
            file_json = json.load(file)
        return file_json



    def file_name(self,file_path):
        """
          file_name : Extrait le nom du fichier
            Arg: le chemin du fichier
        """
        name = os.path.basename(file_path)
        return name
    
    def clean_data(self, rawMostPopularJSON, name):
        """
        On prend en paramètre la liste brut des 20 résultats de most popular sous forme de raw JSON 
        et on renvoi un dictionnaire contenant un tableau de dictionnaire d'articles cleanés. On stockera dans cet objet la date de recherche
        ainsi que la période recherchée (1, 7, 30) et le type de most popular (emailed, shared, viewed) à l'aide du titre
        du fichier JSON raw.
        Chacun des dictionnaires articles du tableau aura les éléments suivants:
        -_id (= l'uri)
        -url
        -title
        -published_date
        -byline
        -section
        """
        print(name)
        #name_split = name.split('_ |.')
        name_split = re.split(r"[_.]\s*",name)

        print(name_split)

        clean_most_popular = {}

        clean_most_popular['_id'] = name_split[2]+name_split[3]+name_split[4]+name_split[5]
        clean_most_popular['most_popular_type'] = name_split[2]
        clean_most_popular['search_period'] = name_split[3]
        clean_most_popular['search_month'] = name_split[4]
        clean_most_popular['search_day'] = name_split[5]

        results = rawMostPopularJSON['results']
        
        clean_most_popular_articles = []

        for index, article in zip(range(20), results):
            a = {}
            a['_id'] = article['uri']
            a['url'] = article['url']
            a['title'] = article['title']
            a['pusblished_date'] = article['published_date']
            a['byline'] = article['byline']
            a['section'] = article['section']

            clean_most_popular_articles.append(a)
        
        clean_most_popular['Articles'] = clean_most_popular_articles
                
        return clean_most_popular
    
    def save_clean_data(self, data: Dict[str, str], endpoint: str, period: int) -> None:
        """Save clean dict in a JSON file

        Args:
            data (dict[str, str]): JSON.
            endpoint (str): The endpoint to call,
                            in ["emailed", "shared", "viewed"].
            period (int): The period of days, in [1, 7, 30].
        """

        _today = date.today()
        filename = f"clean_most_popular_{endpoint}_{period}d_{_today.month}_{_today.day}.json"
        if self.repo_path:
            filepath = self.repo_path + filename
        else:
            filepath = f"../data/clean_data/most_popular/{filename}"

        with open(filepath, "w") as file:
            json.dump(data, file)



if __name__ == "__main__":
    # Fetch articles (params: endpoint, period, repo_path).

    import sys

    endpoint = sys.argv[1]
    period = int(sys.argv[2])

    try:
        api_most_popular = ApiMostPopular(repo_path=sys.argv[3])
    except IndexError:
        api_most_popular = ApiMostPopular()

    query = api_most_popular.get_data(endpoint, period)

    if query:
        api_most_popular.save_data(query, endpoint, period)
        print("\nArticles récupérés.\n")

    file = "../data/raw_data/most_popular/most_popular_emailed_7d_4_7.json"
    to_treat = api_most_popular.import_json(file)
    name = api_most_popular.file_name(file)
    print(name)
    to_stock = api_most_popular.clean_data(to_treat, name)
    print(to_stock)
    api_most_popular.save_clean_data(to_stock, endpoint, period)
