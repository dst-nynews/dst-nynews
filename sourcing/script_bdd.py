"""
Script récupérant les fichiers Json de article search pour les mettre dans une collection de mongoDB
"""
from pymongo import MongoClient
import json
import glob




class ImportMongDB:

    def __init__(self,coll,db="NYTimes",host = "127.0.0.1",port =27017 ) -> None:
        self.host = host
        self.port = port 
        self.db = db 
        self.coll = coll

    def import_json(self,file_name):
        with open(file_name, "r") as file:
            file_json = json.load(file)
        return file_json
    
    def insert_mongoDB(self,json_cleaned):
        client = MongoClient(
            host= self.host,
            port = self.port
        )
        db = client[self.db]
        collection = db[self.coll]

        to_stock = self.import_json(json_cleaned)

        if to_stock != None:    
    
            if isinstance(to_stock, list):
                collection.insert_many(to_stock) 
            else:
                collection.insert_one(to_stock)



#Test
test = ImportMongDB("ArticleSearch")

liste_cleaned = glob.glob("data/cleaned_data/cleaned*")
test = ImportMongDB("ArticleSearch")
for i in liste_cleaned:
    test.insert_mongoDB(i)