import pandas as pd

def carga_csv(ruta: str) -> pd.DataFrame:
    return pd.read_csv(ruta)

if __name__ == "__main__":
    df_ventas = carga_csv("../dataset/raw/ventas.csv")
    print(df_ventas.head())

