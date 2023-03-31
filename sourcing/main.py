from api_most_popular import ApiMostPopular

# import sys


def fetch_data(endpoint="viewed", period=1):

    endpoint = endpoint
    period = period
    api_most_popular = ApiMostPopular(repo_path="./data/raw_data/most_popular/")

    response = api_most_popular.get_data(endpoint, period)

    if response:
        api_most_popular.save_data(response, endpoint, period)
        print(f"\n{endpoint} - {period}d: articles récupérés.\n")


# import logging
# import logging.handlers
# import os
# import requests
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger_file_handler = logging.handlers.RotatingFileHandler(
#     "status.log",
#     maxBytes=1024 * 1024,
#     backupCount=1,
#     encoding="utf8",
# )
# formatter = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# logger_file_handler.setFormatter(formatter)
# logger.addHandler(logger_file_handler)
# try:
#     SOME_SECRET = os.environ["SOME_SECRET"]
# except KeyError:
#     SOME_SECRET = "Token not available!"
#     # logger.info("Token not available!")
#     # raise


if __name__ == "__main__":

    endpoints = ["emailed", "shared", "viewed"]
    for e in endpoints:
        fetch_data(e)

    # logger.info(f"Token value: {SOME_SECRET}")
    # r = requests.get(
    #     "https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE"
    # )
    # if r.status_code == 200:
    #     data = r.json()
    #     temperature = data["forecast"]["temp"]
    #     logger.info(f"Weather in Berlin: {temperature}")
