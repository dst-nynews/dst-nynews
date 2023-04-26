"""
Fichier qui va écrire les dictionnaires clean dans la BD Mongo.
- Concepts
- Search Concept
- Articles
- Search Most popular

"""

from pymongo import MongoClient
import json
from datetime import datetime
import glob
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Bdd:
    def __init__(self, repo_path_clean: Optional[str] = None) -> None:
        """Instanciate a connection to fetch data from an API of the NY Times.
        Args:
            repo_path (Optional[str], optional): Path to clean storage directory.
        """
        self.repo_path_clean = repo_path_clean
        self.MongoHost = os.getenv("MONGO_CLIENT_HOST")
        self.Client = MongoClient(host=self.MongoHost, port=27017)

    def import_json(self, file_name):
            with open(self.repo_path_clean+file_name, "r") as file:
                file_json = json.load(file)
            return file_json


    def insert_mongoDB(self, json_cleaned, collection):
            to_stock = self.import_json(json_cleaned)
            if to_stock != None:    
                if isinstance(to_stock, list):
                    for document in to_stock:
                        document["created_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        collection.replace_one({"_id": document["_id"]}, document, upsert = True)
                else:
                    #collection.insert_one(to_stock)
                    to_stock["created_at"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    collection.replace_one({"_id": to_stock["_id"]}, to_stock, upsert = True)


# test
"""
bddSemantic = Bdd("../data/clean_data/semantic/")
db = bddSemantic.Client['NYTimes']
print(db.list_collection_names())

concepts = db['Concepts']
searchSemantic = db["SearchSemantic"]

bddSemantic.insert_mongoDB("Baseball.json", concepts)
bddSemantic.insert_mongoDB("Coronavirus (2019-nCoV).json", concepts)
bddSemantic.insert_mongoDB("Acapulco (Mexico).json", concepts)
bddSemantic.insert_mongoDB("Abbas, Mahmoud.json", concepts)
bddSemantic.insert_mongoDB("Chicago White Sox.json", concepts)

bddSemantic.insert_mongoDB("Coronavirus.json", searchSemantic)


#articles = db['Articles']
#liste_cleaned = glob.glob("data/cleaned_data/cleaned*")
#for i in liste_cleaned:
#    insert_mongoDB(i,articles)

bddMostPopular = Bdd("../data/clean_data/most_popular/")
db = bddMostPopular.Client['NYTimes']
print(db.list_collection_names())
searchMostPopular = db["SearchMostPopular"]
bddMostPopular.insert_mongoDB("clean_most_popular_emailed_7d_4_7.json", searchMostPopular)
<<<<<<< HEAD

"""
"""
# Peupler la BDD collection SearchMostPopular à la main, jouer sur le fichier json clean à ajouter en BD
bddMostPopular = Bdd("../data/clean_data/most_popular/")
db = bddMostPopular.Client['NYTimes']
searchMostPopular = db["SearchMostPopular"]
bddMostPopular.insert_mongoDB("clean_most_popular_viewed_1d_4_25.json", searchMostPopular)
=======
>>>>>>> 35619cb4fb8208f09e508102d1db444568a295bb
"""