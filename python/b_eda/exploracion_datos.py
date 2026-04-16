import pandas as pd

def f_info_general(df: pd.DataFrame) -> None:
    # Muestra la información del DataFrame 
    print('Información General\n')
    df.info()
    
def f_contar_nulos(df: pd.DataFrame) -> pd.Series:
    # Retorna cantidad de valores NULOS por columna
    print('Recuento de valores NULL \n')
    return df.isnull().sum()

def f_estadistica(df: pd.DataFrame) -> pd.DataFrame:
    # Retorna estadísticas descriptivas
    print('Estadistica descriptiva\n')
    return df.describe()

def f_contar_duplicados(df: pd.DataFrame) -> int:
    # Retorna la cantidad de filas duplicadas
    print('Duplicados')
    return df.duplicated().sum()

def f_columnas(df: pd.DataFrame) -> list:
    # Retorna lista de columnas 
    print('Columnas del archivo \n')
    return df.columns

def f_resumen_eda(df: pd.DataFrame) -> None:
    f_info_general(df)
    
    print('\n\n')
    nulos = f_contar_nulos(df)
    print(nulos)
    
    print('\n\n')
    stats = f_estadistica(df)
    print(stats)
    
    print('\n\n')
    doble = f_contar_duplicados(df)
    print(doble)
    
    print('\n\n')
    print(f_columnas(df))
    
    
    