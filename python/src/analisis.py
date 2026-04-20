import pandas as pd
from typing import Union, List

# Venta Total
def f_suma_ventas(df: pd.DataFrame, columna_valor: str) -> None:
    venta_total = df[columna_valor].sum()
    print(f'Venta total {venta_total:,.2f}')
    
# Venta promedio    
def f_promedio_venta(df: pd.DataFrame, columna_valor: str) -> None:
    venta = df[columna_valor].mean()
    print(f'Venta total {venta:,.2f}') 

# Los meses ordenados    
def f_venta_por_mes(df: pd.DataFrame, columna_grupo: Union[str, List[str]], columna_valor: str) -> pd.DataFrame:
    return df.groupby(columna_grupo, as_index = False)[columna_valor].sum().sort_values(columna_grupo)

# Ventas por productos
def f_mayor_ventas(df: pd.DataFrame, columna_grupo: Union[str, List[str]], columna_valor: str) -> pd.DataFrame:
    return df.groupby(
        columna_grupo, as_index = False)[columna_valor].sum().sort_values(columna_valor, ascending = False)

# Los N más grandes    
def f_grupo_nlargest(df: pd.DataFrame, columna_grupo: str, columna_valor: str, n: int) -> pd.Index:
    return df.groupby(columna_grupo)[columna_valor].sum().nlargest(n).index
    
# Filtro    
def f_filtro(df: pd.DataFrame, columna_grupo: str, valores: Union[pd.Index, List[str]]) -> pd.DataFrame:
    return df[df[columna_grupo].isin(valores)]

# Pivot
def f_pivotear_interno(df: pd.DataFrame, columna_grupo: List[str], columna_valor: str) -> pd.DataFrame:
    return df.groupby(columna_grupo)[columna_valor].sum().unstack()
    
    