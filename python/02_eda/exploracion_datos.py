import pandas as pd

def info_general(df: pd.DataFrame) -> None:
    """ Muestra la información del DataFrame """
    print('Información General\n')
    df.info()
    
def contar_nulos(df: pd.DataFrame) -> pd.Series:
    """Retorna cantidad de valores NULOS por columna """
    print('Valores NULL \n')
    return df.isnull().sum()

def estadistica(df: pd.DataFrame) -> pd.DataFrame:
    """ Retorna estadísticas descriptivas """
    print('Estadistica descriptiva\n')
    return df.describe()

def contar_duplicados(df: pd.DataFrame) -> int:
    """ Retorna la cantidad de filas duplicadas"""
    print('Duplicados')
    return df.duplicated().sum()

def columnas(df: pd.DataFrame) -> list:
    """ Retorna lista de columnas """
    print('Columnas del archivo \n')
    return df.columns

def resumen_eda(df: pd.DataFrame) -> None:
    info_general(df)
    
    print('\n\n')
    nulos = contar_nulos(df)
    print(nulos)
    
    print('\n\n')
    stats = estadistica(df)
    print(stats)
    
    print('\n\n')
    doble = contar_duplicados(df)
    print(doble)
    
    print('\n\n')
    print(columnas(df))
    
    
    