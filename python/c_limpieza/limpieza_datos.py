import pandas as pd

# Limpiar nombre de columnas
def f_limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    # Normaliza nombres de columnas
    df.columns = df.columns.str.lower().str.strip()
    return df

def f_convertir_fechas(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    # Convierte columna a formato datetime 
    df[columna] = pd.to_datetime(df[columna], errors = 'coerce')
    return df


