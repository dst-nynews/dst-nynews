"""Helper functions connecting frontend (Streamlit) and backend (FastAPI)."""

from typing import Dict

import requests
import streamlit as st


class APINames:
    API_BASE = "http://api:8000"  # Local hosting
    API_ROOT = API_BASE + "/"
    API_POPULAR = API_BASE + "/popular"
    API_COVID = API_BASE + "/covid"


def make_clickable_article_title(title: str, url: str) -> str:
    """HTML hyperlink to article page.

    :param id: article id as string
    :param title: title of article as string
    :return: string with url attachment to make hyperlink in markdown
    """
    return f"[{title}]({url})"


@st.cache_data
def _get_json_data(endpoint) -> Dict:
    """Gets relevant JSON data from given FastAPI endpoint."""
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


@st.cache_data
def get_popular_list() -> Dict:
    return _get_json_data(APINames.API_POPULAR)


@st.cache_data
def get_popular(popular_id) -> Dict:
    return _get_json_data(f"{APINames.API_POPULAR}/{popular_id}")


"""Helper functions connecting frontend (Streamlit) and backend (FastAPI) / covid."""



@st.cache_data
def get_request(request_id) -> Dict:
    return _get_json_data(f"{APINames.API_COVID}/{request_id}")
