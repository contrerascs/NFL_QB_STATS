import pandas as pd

def load_data():
    return pd.read_csv("data/NFL QB Stats.csv")

def get_unique_players(df):
    return df["Jugador"].unique()