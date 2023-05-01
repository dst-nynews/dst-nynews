from dash import Dash, html, dcc, callback, Output, Input, State, dash_table
import plotly.express as px
import pandas as pd
import requests
import json

# Initialisation de l'app

df = pd.DataFrame({'state': [0, 0, 0], 'Total cases': [0, 0, 0], 'Total deaths': [0, 0, 0]})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Layout de l'app
app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
app.layout = html.Div([
    # Titre et présentation de la page
    html.H1(children='Projet New-York Times Bootcamp DE Février 2023', style={'textAlign':'center'}),
    html.H5(children ='Vous proposez une date de début et de fin. On vous renvoi le nombre de cases et de deaths Covid par States sur cette période'),
    
    # Request 1  
    html.Div([
        html.H2(children="Quelle date souhaitez vous format : date_debut:date_fin"),
        dcc.Textarea(
            id='textarea-state-dates',
            value='date_debut:date_fin',
            style={'width': '20%', 'height': "30%"}),
        html.Button('Submit', id='textarea-state-dates-button', n_clicks=0),
        html.Div(id='textarea-cases-deaths-output', style={'whiteSpace': 'pre-line'}),
        dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],id='tableCasesDeaths')
  
])
])
# Controles
    # Recherche concept officel + type
@callback(
    #Output('textarea-cases-deaths-output', "children" ),
    Output('textarea-cases-deaths-output', "children" ),
    Input('textarea-state-dates-button', 'n_clicks'),
    State('textarea-state-dates', 'value')
)
def request1(n_clicks,value):
    if n_clicks >0:
        value_split = value.split(":")
        date_debut = value_split[0]
        date_fin = value_split[1]
        req = requests.get(f"http://localhost:8000/covid/request1?date_debut={date_debut}&date_fin={date_fin}")
        states = req.json()
        #dictStates = json.loads(states)
        #for row in dictStates:
        #df.append(row, ignore_index=True)
        #Output = states[0]
        #return Output
        return states

# Exécute l'app
if __name__ == '__main__':
    app.run_server(debug=True)

# 2020-08-01:2020-08-10