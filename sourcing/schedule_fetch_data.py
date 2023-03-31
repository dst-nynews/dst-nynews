import time
from datetime import datetime

import schedule
from api_most_popular import ApiMostPopular


def fetch_data(endpoint="viewed", period=1):

    endpoint = endpoint
    period = period
    api_most_popular = ApiMostPopular(repo_path="./data/raw_data/most_popular/")

    response = api_most_popular.get_data(endpoint, period)

    if response:
        api_most_popular.save_data(response, endpoint, period)


def job():

    endpoints = ["emailed", "shared", "viewed"]
    for e in endpoints:
        fetch_data(e)


# Run job every day at 8:00 until the 25/05/2023
schedule.every().day.at("08:00").until(datetime(2023, 5, 25)).do(job)


while True:
    schedule.run_pending()
    time.sleep(5)


# if __name__ == "__main__":
#     main()
