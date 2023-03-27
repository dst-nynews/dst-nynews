"""
Script récupérant les fichiers Json de article search pour les mettre dans une collection de mongoDB
"""
from pymongo import MongoClient
import json


def import_json(file_name):
    with open(file_name, "r") as file:
        file_json = json.load(file)
    return file_json



class ImportMongDB:

    def __init__(self,coll,db="NYTimes",host = "127.0.0.1",port =27017 ) -> None:
        self.host = host
        self.port = port 
        self.db = db 
        self.coll = coll

   
    # insertion dans la bdd
    
    def insert_mongoDB(self,json_cleaned):
        client = MongoClient(
            host= self.host,
            port = self.port
        )
        db = client[self.db]
        collection = db[self.coll]
    
        if isinstance(json_cleaned, list):
            collection.insert_many(json_cleaned) 
        else:
            collection.insert_one(json_cleaned)



#Test
json_cleaned = import_json("data/raw_data/Covid2020-01-31_Page_0.json")
test = ImportMongDB("ArticleSearch")
test.insert_mongoDB(json_cleaned)




