import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.layout import layout
from components.callbacks import register_callbacks

# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Establecer el layout de la aplicación
app.layout = html.Div([
    dcc.Store(id='theme-store', data='darkly'),  # Almacenar el tema actual
    layout,
    dbc.Button("Cambiar Tema", id='theme-toggle', className="mt-3")
])

# Registrar los callbacks
register_callbacks(app)

# Gunicorn necesita un objeto WSGI, que en Dash se obtiene con 'app.server'
server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)