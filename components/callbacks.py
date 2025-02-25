from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
from utils.data_loader import load_data
import dash_bootstrap_components as dbc

# Cargar datos
df = load_data()

def register_callbacks(app):
    @app.callback(
        [Output('stats-output', 'children'),
         Output('yardas-graph', 'figure'),
         Output('td-graph', 'figure'),
         Output('scatter-plot', 'figure'),
         Output('pie-chart', 'figure'),
         Output('theme-store', 'data'),
         Output('title', 'className')],
        [Input('player', 'value'),
         Input('theme-toggle', 'n_clicks')],
        [State('theme-store', 'data')]
    )
    def update_dashboard(qb_seleccionado, n_clicks, current_theme):
        # Cambiar el tema al hacer clic en el botón
        if n_clicks and n_clicks > 0:
            new_theme = 'darkly' if current_theme == 'flatly' else 'flatly'
        else:
            new_theme = current_theme

        # Determinar el template de Plotly según el tema
        plotly_template = 'plotly_dark' if new_theme == 'darkly' else 'plotly_white'

        # Actualizar el título y el tema
        title_class = "text-center my-4 text-white" if new_theme == 'darkly' else "text-center my-4 text-dark"

        if qb_seleccionado is None:
            return (
                html.P("Selecciona un quarterback para ver sus estadísticas."),
                {}, {}, {}, {},
                new_theme,
                title_class
            )

        # Filtrar datos del jugador seleccionado
        df_qb = df[df["Jugador"] == qb_seleccionado]

        # Calcular estadísticas
        temporadas_jugadas = len(df_qb)
        total_yardas = df_qb["YardasPase"].sum()
        total_td = df_qb["Touchdowns"].sum()
        total_int = df_qb["Intercepciones"].sum()
        promedio_cmp = round(df_qb["PorcentajeCmp"].mean(), 2)
        rating_qb = round(df_qb["RatingQB"].mean(), 2)
        pase_mas_largo = df_qb["PaseMasLargo"].max()

        # Crear tabla de estadísticas
        stats_table = dbc.Table([
            html.Thead(html.Tr([html.Th("Estadística"), html.Th("Valor")])),
            html.Tbody([
                html.Tr([html.Td("Temporadas Jugadas"), html.Td(temporadas_jugadas)]),
                html.Tr([html.Td("Yardas Totales"), html.Td(total_yardas)]),
                html.Tr([html.Td("Touchdowns"), html.Td(total_td)]),
                html.Tr([html.Td("Intercepciones"), html.Td(total_int)]),
                html.Tr([html.Td("Porcentaje de Completos"), html.Td(f"{promedio_cmp}%")]),
                html.Tr([html.Td("QB Rating Promedio"), html.Td(rating_qb)]),
                html.Tr([html.Td("Pase Más Largo"), html.Td(pase_mas_largo)]),
            ])
        ], bordered=True, dark=new_theme == 'darkly', hover=True, responsive=True, striped=True)

        # Gráfico de yardas por temporada
        fig_yardas = px.line(
            df_qb, x="Temporada", y="YardasPase",
            title=f"Yardas por Temporada de {qb_seleccionado}",
            labels={"YardasPase": "Yardas", "Temporada": "Temporada"},
            template=plotly_template
        )

        # Gráfico de touchdowns por temporada
        fig_td = px.bar(
            df_qb, x="Temporada", y="Touchdowns",
            title=f"Touchdowns por Temporada de {qb_seleccionado}",
            labels={"Touchdowns": "Touchdowns", "Temporada": "Temporada"},
            template=plotly_template
        )

        # Gráfico de dispersión: Yardas vs Touchdowns
        fig_scatter = px.scatter(
            df_qb, x="YardasPase", y="Touchdowns",
            title=f"Relación entre Yardas y Touchdowns de {qb_seleccionado}",
            labels={"YardasPase": "Yardas", "Touchdowns": "Touchdowns"},
            template=plotly_template
        )

        # Gráfico de torta: Distribución de touchdowns por temporada
        fig_pie = px.pie(
            df_qb, names="Temporada", values="Touchdowns",
            title=f"Distribución de Touchdowns por Temporada de {qb_seleccionado}",
            template=plotly_template
        )

        return (
            dbc.Card([dbc.CardBody(stats_table)], className="mb-4"),
            fig_yardas, fig_td, fig_scatter, fig_pie,
            new_theme,
            title_class
        )