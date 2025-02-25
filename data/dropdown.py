import dash
from dash import html
from dash import dcc
import pandas as pd

df = pd.read_csv("data/NFL QB Stats.csv")

# Obtener la lista única de jugadores
jugadores = df["Jugador"].unique()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("NFL QB Dashboard", style={"textAlign": "center"}),
    
    dcc.Dropdown(
        id='player',
        options=[{"label": jugador, "value": jugador} for jugador in jugadores],
        value='Joe Burrow'
    ),
    html.Div(id='stats-output')
])

@app.callback(
    dash.dependencies.Output('stats-output', 'children'),
    [dash.dependencies.Input('player', 'value')])
def mostrar_estadisticas(value):
    qb_seleccionado = value
    if qb_seleccionado is None:
        return html.P("Selecciona un quarterback para ver sus estadísticas.")

    # Filtrar datos del jugador seleccionado
    df_qb = df[df["Jugador"] == qb_seleccionado]

    # Calcular estadísticas de toda su carrera
    temporadas_jugadas = len(df_qb)
    total_yardas = df_qb["YardasPase"].sum()
    total_td = df_qb["Touchdowns"].sum()
    total_int = df_qb["Intercepciones"].sum()
    promedio_cmp = round(df_qb["PorcentajeCmp"].mean(), 2)
    rating_qb = round(df_qb["RatingQB"].mean(), 2)
    pase_mas_largo = df_qb["PaseMasLargo"].max()

    # Crear una tabla HTML con los datos
    stats_table = html.Table([
        html.Thead(html.Tr([
            html.Th("Estadística"), html.Th("Valor")
        ])),
        html.Tbody([
            html.Tr([html.Td("Temporadas Jugadas"), html.Td(temporadas_jugadas)]),
            html.Tr([html.Td("Yardas Totales"), html.Td(total_yardas)]),
            html.Tr([html.Td("Touchdowns"), html.Td(total_td)]),
            html.Tr([html.Td("Intercepciones"), html.Td(total_int)]),
            html.Tr([html.Td("Porcentaje de Completos"), html.Td(f"{promedio_cmp}%")]),
            html.Tr([html.Td("QB Rating Promedio"), html.Td(rating_qb)]),
            html.Tr([html.Td("Pase Más Largo"), html.Td(pase_mas_largo)]),
        ])
    ], style={"width": "50%", "margin": "auto", "border": "1px solid black", "textAlign": "center"})

    return html.Div([
        html.H3(f"Estadísticas de {qb_seleccionado}", style={"textAlign": "center"}),
        stats_table
    ])

if __name__ == '__main__':
    app.run_server(debug=False)