import pandas as pd

# Cargar el dataset
df = pd.read_csv("data/NFL QB Stats.csv")

# Verificar que se cargó correctamente
#print(df.head())

# Exportamos el DataFrame para usarlo en otros archivos
def get_data():
    return df