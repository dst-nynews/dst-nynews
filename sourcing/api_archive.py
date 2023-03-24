"""Get data on all NY Times articles published at a specific month.

Fetch data by making a `GET` request to the Archive API,
and store the response as a JSON file in a folder.

It needs:
    - API key,
    - the year and the month of the targeted data,
    - the path to a storage folder (optional).
"""

import json
import os
from typing import Dict, Optional
from urllib.parse import urljoin

import requests

# Fetch environment variables
from dotenv import load_dotenv

load_dotenv()


class ApiArchive:
    def __init__(self, repo_path: Optional[str] = None) -> None:
        """Instanciate a connection to fetch data from an API of the NY Times.

        Args:
            repo_path (Optional[str], optional): Path to storage directory.
        """

        self.KEY_API = os.environ["KEY_API_NYT"]
        self.BASE_URI = "https://api.nytimes.com/"
        self.repo_path = repo_path

    def get_data(self, year: int, month: int) -> Dict[str, str]:
        """GET request to the API.

        Args:
            year (int): Year of publication of articles.
            month (int): Month of publication of articles.

        Returns:
            dict[str, str]: Response as a JSON.
        """

        url_path = f"/svc/archive/v1/{year}/{month}.json"
        url = urljoin(self.BASE_URI, url_path)
        params = {"api-key": self.KEY_API}

        response = requests.get(url, params=params)
        # print(response.status_code)

        return response.json()

    def save_data(self, data: Dict[str, str], year: int, month: int) -> None:
        """Save response in a JSON file.

        Args:
            data (Dict[str, str]): Response as a JSON.
            year (int): Year of publication of articles.
            month (int): Month of publication of articles.
        """

        filename = f"archive_{year}_{month}.json"
        if self.repo_path:
            filepath = self.repo_path + filename
        else:
            filepath = f"../data/raw_data/{filename}"

        with open(filepath, "w") as file:
            json.dump(data, file)


if __name__ == "__main__":
    # Fetch articles (params: year, month, repo_path).

    import sys

    year = int(sys.argv[1])
    month = int(sys.argv[2])

    try:
        api_archive = ApiArchive(repo_path=sys.argv[3])
    except IndexError:
        api_archive = ApiArchive()

    query = api_archive.get_data(year, month)

    if query:
        api_archive.save_data(query, year, month)
        hits = query["response"]["meta"]["hits"]
        print(f"\n{hits} articles récupérés pour {month}-{year}. \n")
