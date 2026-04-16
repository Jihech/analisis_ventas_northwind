import pandas as pd

def limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.strip()
    return df

def ver_nulos(df: pd.DataFrame) -> pd.Series:
    return df.isnull().sum()
    
def ver_info(df: pd.DataFrame) -> None:
    df.info()

def eliminar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def guardar_csv(df: pd.DataFrame, ruta: str) -> None:
    df.to_csv(ruta, index = False) 
    
    