"""Get the 20 most popular articles of the NY Times.

Fetch data by making a `GET` request to an endpont of the Most Popular API,
and store the response as a JSON file in a subfolder of `data/`.

It needs an:
    - API key,
    - the endpoint (`emailed`, `shared`, `viewed`),
    - and the period of days (`1`, `7`, `30`)

The endpoint gives the metric on which is measured the popularity of articles
"""


import json
import os
from datetime import date
from urllib.parse import urljoin

import requests

# Fetch environment variables
from dotenv import load_dotenv

load_dotenv()


# Set constants
API_KEY = os.environ["KEY_API_NYT"]
BASE_URI = "https://api.nytimes.com/"


def get_most_popular(endpoint="emailed", period=1):
    """GET request to an endpoint of the `Most Popular` API of the NY Times

    Args:
        endpoint (str): the endpoint to call (`emailed`, `shared`, `viewed`).
                        Defaults to "emailed".
        period (int): the period of days (`1`, `7`, `30`). Defaults to 1.

    Returns:
        dict[str, str]: a JSON with the content of the response from the API
    """

    url_path = f"/svc/mostpopular/v2/{endpoint}/{period}.json"
    url = urljoin(BASE_URI, url_path)
    params = {"api-key": API_KEY}

    response = requests.get(url, params=params)

    # print(response.status_code)
    return response.json()


def write_json(data, endpoint, period):
    """Save response in a JSON file

    Args:
        data (dict[str, str]): Response as a JSON
        endpoint (str): the endpoint to call (`emailed`, `shared`, `viewed`)
        period (int): the period of days (`1`, `7`, `30`)
    """

    today = date.today()
    filename = f"most_popular-{endpoint}_{period}d-{today.month}_{today.day}"
    filepath = f"../data/raw_data/{filename}.json"

    with open(filepath, "w") as file:
        json.dump(data, file)


def main():
    """
    Ask user for an endpoint and a period,
    to fetch most popular articles for this period.
    """

    endpoint = input("Mesure de popularité? (emailed, shared, viewed)\n> ")
    period = input("Période? (1, 7, 30)\n> ")

    query = get_most_popular(endpoint, period)
    if query:
        write_json(query, endpoint, period)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAurevoir!")
