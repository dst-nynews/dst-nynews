"""
Script récupérant les fichiers Json de article search pour les mettre dans une collection de mongoDB
"""
from pymongo import MongoClient
import json

client = MongoClient(
    host="127.0.0.1",
    port = 27017
)

db = client['NYTimes']
article_search = db['article_search']

# récupération fichiers json
def import_json(file_name):
    with open(file_name, "r") as file:
        file_json = json.load(file)
    return file_json

# insertion dans la bdd
def insert_mongoDB(json_cleaned):
    if isinstance(json_cleaned, list):
        article_search.insert_many(json_cleaned) 
    else:
        article_search.insert_one(json_cleaned)
    

file = import_json("../data/raw_data/covid20192023_Page_0.json")
file_cleaned = json_clean(file)
insert_mongoDB(file_cleaned)

print(client.list_database_names())




