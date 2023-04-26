from dash import Dash, html, dcc, callback, Output, Input, State, dash_table
import plotly.express as px
import pandas as pd
import requests
import json

# Initialisation de l'app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Layout de l'app
app.layout = html.Div([
    # Titre et présentation de la page
    html.H1(children='Projet New-York Times Bootcamp DE Février 2023', style={'textAlign':'center'}),
    html.H5(children ='Vous proposez un mot clé. On vous propose les concepts officiels du New-York Times affiliés et, si vous en choisissez un, on vous dit si le nombre d\'articles taggés avec ce concept publié dans le New-York Times est corrélés aux cas Covid !'),
    
    # Recherche via mot clé
    html.Div([
        html.H2(children="Quel mot-clé souhaitez-vous chercher ?"),
        dcc.Textarea(
            id='textarea-state-unknow',
            value='Mot-clé',
            style={'width': '20%', 'height': "30%"}),
        html.Button('Submit', id='textarea-state-unknow-button', n_clicks=0),
        html.Div(id='textarea-unknow-output', style={'whiteSpace': 'pre-line'})]),

    # Recherche concept  
    html.Div([
        html.H2(children="Quel concept souhaitez-vous chercher ? format : concept:type"),
        dcc.Textarea(
            id='textarea-state-concept',
            value='Mot-clé',
            style={'width': '20%', 'height': "30%"}),
        html.Button('Submit', id='textarea-state-concept-button', n_clicks=0),
        html.Div(id='textarea-concept-output', style={'whiteSpace': 'pre-line'})])
  

])
# Controles
    # Recherche via mot clé
@callback(
    Output('textarea-unknow-output', "children" ),
    Input('textarea-state-unknow-button', 'n_clicks'),
    State('textarea-state-unknow', 'value')
)
def semantic_request_unknow(n_clicks, value_unknow):
    if n_clicks > 0:
        req = requests.get(f"http://localhost:8000/semantic/unknow/list?conceptInconnu={value_unknow}")
        wb = req.json()
        if type(wb) == list:
            return [f'Concept : {i[0]} \n Pour pouvoir le requêter, copiez et collez ceci juste en dessous :    {i[0]}:{i[1]}\n' for i in wb]
        else :
            return wb

    # Recherche concept officel + type
@callback(
    Output('textarea-concept-output', "children" ),
    Input('textarea-state-concept-button', 'n_clicks'),
    State('textarea-state-concept', 'value')
)
def get_concept(n_clicks,value):
    if n_clicks >0:
        value_split = value.split(":")
        concept = value_split[0]
        type = value_split[1]
        req = requests.get(f"http://localhost:8000/semantic/concept?knownconcept={concept}&conceptType={type}")
        wb = req.json()
        articles = []
        for i in wb["article_list"]:
            articles.append(f"Article {i['title']}, publié le {i['date']}. Url : {i['url']}")
        
        Output = f"Le concept a été créé le {wb['concept_created']}. \n Il y a {wb['nb_articles']} articles dans le New-York Times qui lui sont affiliés.\n Il est considéré comme {wb['concept_status']} par le journal. \n\n {articles}"
        return Output
        

#[f"Article  {articles[0]}\n Publié le {articles[1]} \n Url : {articles[2]}"]
# Exécute l'app
if __name__ == '__main__':
    app.run_server(debug=True)