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
    