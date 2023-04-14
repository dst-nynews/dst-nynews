from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd
import requests
import json

# Initialisation de l'app
app = Dash(__name__)

# Layout de l'app
app.layout = html.Div([
    html.H1(children='Projet New-York Times Bootcamp DE Février 2023', style={'textAlign':'center'}),
    html.H2(children ='Les publications du New-York Times sont-elles corrélées avec le nombre réel de cas ?'),
    dcc.Textarea(
        id='textarea-state-example',
        value='Quel mot-clé souhaitez-vous rechercher ?',
        style={'width': '20%', 'height': 30},
    ),
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})
])

# Controles
@callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')
)

def semantic_request(n_clicks, value):
    result = {}
    if n_clicks > 0:
        req = requests.get(f"http://127.0.0.1:8000/semantic?conceptInconnu={value}")
        wb = req.json()
        return [ f'Concept : {i} \n' for i in wb]



# Exécute l'app
if __name__ == '__main__':
    app.run_server(debug=True)