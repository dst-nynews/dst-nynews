"""Get data on all NY Times articles published at a specific month.   

Fetch data by making a `GET` request to the Archive API, 
and store the response as a JSON file in the folder `data/`.  
It needs an API key, the year, and the month of the targeted data.

Typical usage example:

    # API call
    year = 2010
    month = 10
    query = get_archive(year, month)

    # Save result as a JSON
    file_name = f"data_api_archive_{year}_{month}"
    write_json(query, year, month)

    # Display the quantity of data collected 
    hits = query["response"]["meta"]["hits"]  
    print(f"- {hits} articles récupérés pour {month}-{year}")
"""

import os
import json
from urllib.parse import urljoin
import requests

# Fetch environment variables 
from dotenv import load_dotenv
load_dotenv()


# Set constants
API_KEY = os.environ["KEY_API_NYT"]
BASE_URI = "https://api.nytimes.com/"

        
def get_archive(year: int , month: int) -> dict[str, str]:
    """GET request to the Archive API of the NY Times

    Args:
        year (int): Year of publication of articles
        month (int): Month of publication of articles

    Returns:
        dict[str, str]: Response as a JSON
    """
    
    url_path = f"/svc/archive/v1/{year}/{month}.json"
    url = urljoin(BASE_URI, url_path)
    params = {"api-key": API_KEY}
    
    return requests.get(url, params=params).json()


def write_json(data: dict[str, str], year: int , month: int) -> None:
    """Save response in a JSON file

    Args:
        data (dict[str, str]): Response as a JSON
        year (int): Year of publication of articles
        month (int): Month of publication of articles
    """
    
    filepath = f"../data/raw_data/archive_api/archive_{year}_{month}.json"
    with open(filepath, "w") as file:
        json.dump(data, file)


def main():
    """Ask user for a year and a month to fetch articles for this period."""
    
    year = input("Année?\n> ")
    month = input("Mois?\n> ")
    query = get_archive(year, month)

    if query:
        write_json(query, year, month)
        
        hits = query["response"]["meta"]["hits"]  
        print(f"\nC'est dans la boite! \n{hits} articles récupérés pour {month}-{year}. \n")
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAurevoir!')
