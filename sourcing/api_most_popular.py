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
        filename = f"most_popular_{endpoint}_{period}d-{_today.month}_{_today.day}.json"
        if self.repo_path:
            filepath = self.repo_path + filename
        else:
            filepath = f"../data/raw_data/{filename}"

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
