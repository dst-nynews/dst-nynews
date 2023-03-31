import time
from datetime import datetime

import schedule
from api_most_popular import ApiMostPopular


def job():
    """Query NY Times API to fetch data of the previous day.
    """
    endpoints = ["emailed", "shared", "viewed"]
    api_popular = ApiMostPopular(repo_path="./data/raw_data/most_popular/")

    for e in endpoints:
        req = api_popular.get_data(endpoint=e, period=1)

        if req:
            api_popular.save_data(data=req, endpoint=e, period=1)


# Run job every day at 8:00 until the 25/05/2023
schedule.every().day.at("08:00").until(datetime(2023, 5, 25)).do(job)


while True:
    schedule.run_pending()
    time.sleep(5)
