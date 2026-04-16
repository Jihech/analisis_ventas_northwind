import pandas as pd

# Limpiar nombre de columnas
def f_limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    # Normaliza nombres de columnas
    df.columns = df.columns.str.lower().str.strip()
    return df

# Creamos esta función si usamos un dataset con filas duplicadas
def f_eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    # Elimina filas duplicadas
    return df.drop_duplicates()

# Creamos esta función por si tenemos valores nulos
def f_eliminar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    # Elimina valores nulos
    return df.dropna()

def f_convertir_fechas(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    # Convierte columna a formato datetime 
    df[columna] = pd.to_datetime(df[columna], errors = 'coerce')
    return df

# Creamos esta función por si en algú momento usamos un dataset con valores NaN
def f_rellenar_valores_nan(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    # Convertir NaN a 0 en una columna especifica
    df[columna] = df[columna].fillna(0)
    return df

# Creamos esta función por si en algún momento deseamos eliminar una columna
def f_eliminar_una_columna(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    if columna in df.columns:
        print(f'Se eliminó la columna "{columna}" correctamente')
        return df.drop(columna, axis = 1,  inplace = True ) 
    else:
        print(f'No existe la columna "{columna}"')
        return df