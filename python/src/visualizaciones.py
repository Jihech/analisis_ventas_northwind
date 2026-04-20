import matplotlib.pyplot as plt
import pandas as pd
from typing import List

# Validación de columnas con valores NaN
def f_validar_columnas(df: pd.DataFrame, columnas: List[str]) -> pd.DataFrame:
    for columna in columnas:
        if columna not in df.columns:
            raise ValueError(f'La columna "{columna}" no existen en el DataFrame')
    return df.dropna(subset = columnas) 

# Con una sola linea o multiples lineas
def f_plot_lineal(
    df: pd.DataFrame, 
    columna_x: str, 
    columna_y: str, 
    multi_linea: str = None, # Definición si se usa o no con multiples lineas
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
    if multi_linea:
        df = f_validar_columnas(df, [columna_x, columna_y, multi_linea])
    else:
        df = f_validar_columnas(df, [columna_x, columna_y])
    
    # Gráfico 
    plt.figure(figsize=(12, 6))

    # Con una sola linea
    if multi_linea is None:
        plt.plot(df[columna_x], df[columna_y], marker='o')
        
    # Con multiples lineas 
    else:
        for categoria in sorted(df[multi_linea].dropna().unique()):
            filtro = df[df[multi_linea] == categoria]
            plt.plot(filtro[columna_x], filtro[columna_y], marker='o', label=categoria)
            
        plt.legend(title=multi_linea)

    plt.xticks(rotation=45)
    plt.title(titulo if titulo else f'{columna_y} por {columna_x}', fontsize=15)
    plt.xlabel(xlabel if xlabel else columna_x, fontsize=12)
    plt.ylabel(ylabel if ylabel else columna_y, fontsize=12)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Barra vertical
def f_plot_bar(
    df: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
    df = f_validar_columnas(df, [columna_x, columna_y])
    
    plt.figure(figsize=(12, 6))

    plt.bar(df[columna_x], df[columna_y])
    plt.xticks(rotation=45)
    plt.title(titulo if titulo else f'{columna_y} por {columna_x}', fontsize=15)
    plt.xlabel(xlabel if xlabel else columna_x, fontsize=15)
    plt.ylabel(ylabel if ylabel else columna_y, fontsize=15)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Barra horizontal
def f_plot_barh(
    df: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
    df = f_validar_columnas(df, [columna_x, columna_y])
    
    plt.figure(figsize=(12, 6))

    plt.barh(
        df[columna_x],
        df[columna_y]
    )

    plt.gca().invert_yaxis()
    plt.title(titulo if titulo else f'{columna_y} por {columna_x}', fontsize=15)
    plt.xlabel(xlabel if xlabel else columna_x, fontsize=15)
    plt.ylabel(ylabel if ylabel else columna_y, fontsize=15)
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()
    
