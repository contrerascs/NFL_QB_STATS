import dash_bootstrap_components as dbc
from dash import html, dcc
from utils.data_loader import load_data, get_unique_players

# Cargar datos y obtener jugadores únicos
df = load_data()
jugadores = get_unique_players(df)

# Definir el layout de la aplicación
layout = dbc.Container([
    html.H1("NFL QB Dashboard", id='title', className="text-center my-4"),
    
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='player',
                options=[{"label": jugador, "value": jugador} for jugador in jugadores],
                placeholder="Selecciona un quarterback",
                className="mb-4"
            ),
            width=6, className="mx-auto"
        )
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='stats-output', className="p-3 rounded"), width=12, className="mb-4")
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='yardas-graph'), width=6),
        dbc.Col(dcc.Graph(id='td-graph'), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='scatter-plot'), width=6),
        dbc.Col(dcc.Graph(id='pie-chart'), width=6)
    ])
], fluid=True, style={"minHeight": "100vh", "padding": "20px"})