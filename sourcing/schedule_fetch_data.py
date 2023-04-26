import time
from datetime import datetime

import schedule
from api_most_popular import ApiMostPopular
import sys
sys.path.insert(0,"../db")

from bdd_write import Bdd


def job():
    """Query NY Times API to fetch data of the previous day.
    """
    endpoints = ["emailed", "shared", "viewed"]
    api_popular = ApiMostPopular(repo_path="../data/raw_data/most_popular/")

    for e in endpoints:
        req = api_popular.get_data(endpoint=e, period=1)

        if req:
            raw_data_most_popular = api_popular.save_data(data=req, endpoint=e, period=1)
            to_treat = raw_data_most_popular[0]
            name = raw_data_most_popular[1] 
        
        to_stock = api_popular.clean_data(to_treat, name)
        most_popular_clean = api_popular.save_clean_data(to_stock, e, 1)[1]

        bddMostPopular = Bdd("../data/clean_data/most_popular/")
        db = bddMostPopular.Client['NYTimes']
        searchMostPopular = db["SearchMostPopular"]
        bddMostPopular.insert_mongoDB(most_popular_clean, searchMostPopular)

"""
# Run job every day at 8:00 until the 25/05/2023
schedule.every().day.at("08:00").until(datetime(2023, 5, 25)).do(job)


while True:
    schedule.run_pending()
    time.sleep(5)
"""
print("execution du job")
job()
print("fin du job")