"""Helper functions connecting frontend (Streamlit) and backend (FastAPI)."""

from typing import Dict

import requests
import streamlit as st


class APINames:
    API_BASE = "http://localhost:8000"  # Local hosting
    API_ROOT = API_BASE + "/"
    API_COVID = API_BASE + "/covid"


@st.cache_data
def _get_json_data(endpoint) -> Dict:
    """Gets relevant JSON data from given FastAPI endpoint."""
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


@st.cache_data
def get_popular_list() -> Dict:
    return _get_json_data(APINames.API_COVID)


@st.cache_data
def get_request(request_id) -> Dict:
    return _get_json_data(f"{APINames.API_COVID}/{request_id}")
