import pandas as pd

# Cargar el dataset limpio
df = pd.read_csv("data/NFL QB Stats.csv")

def buscar_jugador(nombre, temporada=None):
    """
    Busca un jugador en el dataset, opcionalmente filtrando por temporada.
    
    Parámetros:
        - nombre (str): Nombre del jugador a buscar.
        - temporada (int, opcional): Temporada específica a consultar.
    
    Retorna:
        - DataFrame con los resultados encontrados.
    """
    # Filtrar por nombre de jugador
    resultados = df[df["Jugador"].str.contains(nombre, case=False, na=False)]

    # Si se proporciona una temporada, filtramos aún más
    if temporada:
        resultados = resultados[resultados["Temporada"] == temporada]

    # Verificar si hay resultados
    if resultados.empty:
        return None  # Indicar que no se encontraron datos

    return resultados

# Pruebas
jugador = "Joe Burrow"
temporada = 2022  # Prueba con una temporada específica

resultado = buscar_jugador(jugador, temporada)
if resultado is not None:
    print(resultado)
else:
    print("Jugador no encontrado.")

