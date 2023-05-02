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
st.header("Statistiques d'utilisation du mask pour un état")
st.divider()


# Input form
with st.form("mask_form"):
    state_name = st.text_input('State name', 'Alabama')

    # Button to request data from the backend
    submit_btn = st.form_submit_button("Consultez", type="primary")


# Output display
if submit_btn:
    request_id = 'avg_mask_use_by_state?state='+state_name
    response = get_request(request_id)
    dictResp = json.loads(response)
    
    if dictResp == []:
        # Error message (bad input)
        st.markdown(
            "🙈 Désolé, ce State n'existe pas"
        )

    else:
    
        st.markdown(
                "Bien ouej"
        )

        st.write('Voici les stats d\'utilisation du mask pour l\'état de ' +state_name + '\n', dictResp[0])

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Never', 'Rarely', 'Sometimes', 'Frequently', 'Always'
        sizes = [dictResp[0]["Never"], dictResp[0]["Rarely"], dictResp[0]["Sometimes"], dictResp[0]["Frequently"], dictResp[0]["Always"]]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.title(dictResp[0]["State"]+ " mask use")
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)