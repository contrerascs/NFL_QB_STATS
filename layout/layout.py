from dash import dcc, html
from data.data import get_data

# Cargar los datos
df = get_data()

# Obtener la lista única de jugadores
jugadores = df["Jugador"].unique()

# Definir el layout de la aplicación
layout = html.Div([
    html.H1("NFL QB Dashboard", style={"textAlign": "center"}),

    # Dropdown para seleccionar un quarterback
    dcc.Dropdown(
        id="qb-selector",
        options=[{"label": jugador, "value": jugador} for jugador in jugadores],
        placeholder="Selecciona un quarterback",
        searchable=True,
        value='Patrick Mahomes'
    ),

    # Sección donde mostraremos las estadísticas
    html.Div(id="stats-output")
])

