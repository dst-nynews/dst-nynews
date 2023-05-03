import streamlit as st
import matplotlib.pyplot as plt
import json
import requests
import pandas as pd


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
st.header("D'un mot à l'autre : recherche d'un concept officiel du NYT")
st.divider()


# 1st Input form
form = st.form(key='char')
value_unknow = form.text_input(label='Quel mot-clé souhaitez-vous rechercher ?')
submit_button = form.form_submit_button(label='Consultez')

# 1st Output display
if submit_button:
        req = requests.get(f"http://localhost:8000/semantic/unknow/list?conceptInconnu={value_unknow}")
        wb = req.json()
        df = pd.DataFrame(wb, columns=['Concept', "Type du concept"])
        if wb == []:
             st.write(f"Aucun concept lié à {value_unknow} n'a été trouvé dans le NYT ")
        else:
            st.write(df)



# 2nd Input
with st.form(key='concept_and_type'):
    col1, col2 = st.columns(2)

    with col1:
        concept = st.text_input(label='Quel concept souhaitez-vous rechercher ?')
    
    with col2:
        type = st.text_input(label='Quel type de concept est-ce ?')

    submit_button_2 = st.form_submit_button(label='Consultez')

# 2nd Output
if submit_button_2:
        req = requests.get(f"http://localhost:8000/semantic/concept?knownconcept={concept}&conceptType={type}")
        try:
            wb = req.json()
            articles = []
            for i in wb["article_list"]:
                articles.append([{i['title']}, {i['date']}, {i['url']}])
            df = pd.DataFrame(articles, columns=['Titre', 'Date de publication', 'URL'])
            
            st.write(f"Le concept a été créé le {wb['concept_created']}. \n Il y a {wb['nb_articles']} articles dans le New-York Times qui lui sont affiliés.\n Il est considéré comme {wb['concept_status']} par le journal.") 
            st.write(df)
        except: st.write("Oups, il y a eu une erreur !")