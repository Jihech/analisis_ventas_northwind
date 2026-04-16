import pandas as pd

def limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """ Normaliza nombres de columnas"""
    df.columns = df.columns.str.lower().str.strip()
    return df

def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """ Elimina filas duplicadas"""
    return df.drop_duplicates()

def eliminar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """ Elimina valores nulos"""
    return df.dropna()

def convertir_fechas(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """ Convierte columna a formato datetime """
    df[columna] = pd.to_datetime(df[columna], errors = 'coerce')
    return df

def rellenar_valores_nan(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """ Convertir NaN a 0 en una columna especifica"""
    df[columna] = df[columna].fillna(0)
    return df
    