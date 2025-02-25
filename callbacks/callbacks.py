from dash import Input, Output, html
from app import app
from data.data import get_data
import dash

# Cargar los datos
df = get_data()

# Callback para actualizar las estadísticas del quarterback seleccionado
@app.callback(
    dash.dependencies.Output("stats-output", "children"),
    [dash.dependencies.Input("qb-selector", "value")]
)
def mostrar_estadisticas(value):
    if value is None:
        return html.P("Selecciona un quarterback para ver sus estadísticas.")

    # Filtrar datos del jugador seleccionado
    df_qb = df[df["Jugador"] == value]

    # Sumar estadísticas de toda su carrera
    total_yardas = df_qb["YardasPase"].sum()
    total_td = df_qb["Touchdowns"].sum()
    total_int = df_qb["Intercepciones"].sum()
    
    return html.Div([
        html.H3(f"Estadísticas de {value}"),
        html.P(f"Yardas Totales: {total_yardas}"),
        html.P(f"Touchdowns: {total_td}"),
        html.P(f"Intercepciones: {total_int}")
    ])