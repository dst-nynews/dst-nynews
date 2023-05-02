import datetime as dt

import streamlit as st

import matplotlib.pyplot as plt
import json

# Local imports
from utils import get_request

# Page metadata
st.set_page_config(
    page_title="NyNews",
    page_icon="🗞️",
    layout="centered",
    menu_items={
        "About": "Comment is free :smiling_imp: :crystal_ball:  \n_but facts are sacred_ :angel: :abacus:"
    },
)


# Page title
st.title("NyNews 🗽")
st.header("Nombre de cases et de deaths covid sur une période de temps sur l'ensemble du pays")
st.divider()


# Input form
with st.form("total_cases_deaths_form"):
    _yesterday = dt.date.today() - dt.timedelta(days=1)
    date_form_début = st.date_input("Date de début ",
                              value=dt.date(2020, 1, 21),
                              min_value=dt.date(2020, 1, 21),
                              max_value=_yesterday,
                              )
    
    date_form_fin = st.date_input("Date de fin ",
                              value=dt.date(2020, 1, 21),
                              min_value=dt.date(2020, 1, 21),
                              max_value=_yesterday,
                              )

    # Button to request data from the backend
    submit_btn = st.form_submit_button("Consultez", type="primary")


# Output display
if submit_btn:
    request_id_1 = 'total_cases_by_date?date_debut='+str(date_form_début)+'&date_fin='+str(date_form_fin)
    response1 = get_request(request_id_1)
    dictResp_1 = json.loads(response1)

    request_id_2 = 'total_deaths_by_date?date_debut='+str(date_form_début)+'&date_fin='+str(date_form_fin)
    response2 = get_request(request_id_2)
    dictResp_2 = json.loads(response2)
    
    if (dictResp_1 == []) or (dictResp_2 == []):
        # Error message (bad input)
        st.markdown(
            "🙈 Désolé, ça n'a pas marché"
        )

    else:
    
        st.markdown(
                "Bien ouej"
        )

        st.write('Voici le nombre de cas Covid entre le  ' +str(date_form_début)+ ' et le '+str(date_form_fin) , dictResp_1[0])

        st.write('Voici le nombre de morts Covid entre le  ' +str(date_form_début)+ ' et le '+str(date_form_fin) , dictResp_2[0])