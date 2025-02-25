import dash
from layout.layout import layout  # Importamos el layout de la interfaz
  # Importamos los callbacks para la interactividad

# Inicializar la app
app = dash.Dash(__name__)

# Usar el layout definido en layout.py
app.layout = layout

# Ejecutar el servidor
if __name__ == "__main__":
    app.run_server(debug=True)