import pandas as pd
from typing import Union, List

# Venta Total
def f_ventas_totales(
    df: pd.DataFrame, 
    columna_valor: str) -> None:
    
    venta_total = df[columna_valor].sum()
    print(f'Venta total {venta_total:,.2f}')

# Ventas por productos
def f_mayor_ventas(
    df: pd.DataFrame, 
    columna_grupo: str, 
    columna_valor: str) -> pd.DataFrame:
    
    return df.groupby(columna_grupo, as_index = False).agg(
        Total = (columna_valor, 'sum')
    ).sort_values('Total', ascending = False)
       

def f_ventas_por_mes(
    df: pd.DataFrame, 
    columna_grupo: Union[str, List[str]], 
    columna_valor: str) -> pd.DataFrame:
    
    return df.groupby(columna_grupo, as_index = False).agg(
        Total = (columna_valor, 'sum')
        ).sort_values(columna_grupo)
    
def f_promedio_venta(
    df: pd.DataFrame, 
    columna_valor: str) -> None:
    
    venta = df[columna_valor].mean()
    print(f'Venta total {venta:,.2f}')
    
def f_grupo_nlargest(
    df: pd.DataFrame,
    columna_grupo: str,
    columna_valor: str,
    n: int) -> pd.Series:
    
    df_agg = df.groupby(columna_grupo, as_index = False).agg(
        Total = (columna_valor, 'sum'))
        
    return df_agg.nlargest(n, 'Total')[columna_grupo]
    
def f_filtro(
    df: pd.DataFrame,
    columna_grupo: str,
    valores: Union[pd.Index, List[str]]) -> pd.DataFrame:
    
    return df[df[columna_grupo].isin(valores)]

def f_pivotear_interno(
    df: pd.DataFrame,
    columna_grupo: List[str],
    columna_valor: str) -> pd.DataFrame:
    
    return df.groupby(columna_grupo).agg(
        Total = (columna_valor, 'sum')
    ).unstack()
    
    