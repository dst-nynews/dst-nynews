"""
Fichier qui va faire le lien entre la BD Mongo et les élements de l'API semantic:
- Concepts
- Search Concept

"""

from pymongo import MongoClient
import json
from datetime import datetime

def import_json(file_name):
        with open(file_name, "r") as file:
            file_json = json.load(file)
        return file_json


def insert_mongoDB(json_cleaned, collection):
        to_stock = import_json(json_cleaned)
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
client = MongoClient(host="mongodb+srv://canbaskurt:wxsNxL2fMLq6usJU@cluster0.zjdexu5.mongodb.net", port=27017)

db = client['NYTimes']
concepts = db['Concepts']
searchSemantic = db["SearchSemantic"]

print(client.list_database_names())
print(db.list_collection_names())

insert_mongoDB("Baseball.json", concepts)
insert_mongoDB("Coronavirus.json", searchSemantic)