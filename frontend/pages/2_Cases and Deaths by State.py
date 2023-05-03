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
st.header("Nombre de cases et de deaths covid sur une période de temps pour chaque State")
st.divider()


# Input form
with st.form("state_cases_deaths_form"):
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
    request_id = 'cases_deaths_by_date_by_state?date_debut='+str(date_form_début)+'&date_fin='+str(date_form_fin)
    response = get_request(request_id)
    dictResp = json.loads(response)

    sortedStatesCases = sorted(dictResp, key=lambda d: d["Total cases"], reverse=True)
    sortedStatesDeaths = sorted(dictResp, key=lambda d: d["Total deaths"], reverse=True)

    listStatesCases = []
    listStatesDeaths = []
    listTotalCases = []
    listTotalDeaths = []

    for s in sortedStatesCases:
        listStatesCases.append(s["States"])
        listTotalCases.append(s["Total cases"])
    
    for s in sortedStatesDeaths:
        listStatesDeaths.append(s["States"])
        listTotalDeaths.append(s["Total deaths"])

    
    if dictResp == []:
        # Error message (bad input)
        st.markdown(
            "🙈 Désolé, ça n'a pas marché"
        )

    else:
    
        st.markdown(
                "Bien ouej"
        )

        st.write('Voici le nombre de cas et de morts Covid entre le  ' +str(date_form_début)+ ' et le '+str(date_form_fin) , dictResp)

        fig, ax = plt.subplots()
        ax.set_xticklabels(listStatesCases, rotation='vertical', fontsize=5)
        ax.set_xlabel("States")
        ax.set_ylabel("Nombre de Cases")
        ax.set_title("Nombre de Cases par State")
        ax = plt.bar( listStatesCases,listTotalCases, color = 'orange')
        #ax = plt.bar( listStates,listTotalDeaths, color = 'red')
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        ax.set_xticklabels(listStatesDeaths, rotation='vertical', fontsize=5)
        ax.set_xlabel("States")
        ax.set_ylabel("Nombre de Deaths")
        ax.set_title("Nombre de Deaths par State")
        ax = plt.bar( listStatesDeaths,listTotalDeaths, color = 'red')
        st.pyplot(fig)
        