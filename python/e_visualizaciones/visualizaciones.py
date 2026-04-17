import matplotlib.pyplot as plt
import pandas as pd

def f_plot_lineal(
    df: pd.DataFrame, 
    columna_x: str, 
    columna_y: str, 
    columna_categoria: str = None, 
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
    plt.figure(figsize=(12, 6))

    if columna_categoria is None:
        plt.plot(
            df[columna_x],
            df[columna_y],
            marker='o'
        )
    else:
        for categoria in df[columna_categoria].unique():
            filtro = df[df[columna_categoria] == categoria]
            plt.plot(
                filtro[columna_x],
                filtro[columna_y],
                marker='o',
                label=categoria
            )
        plt.legend(title=columna_categoria)

    plt.xticks(rotation=45)
    plt.title(titulo if titulo else f'{columna_y} por {columna_x}', fontsize=15)
    plt.xlabel(xlabel if xlabel else columna_x, fontsize=15)
    plt.ylabel(ylabel if ylabel else columna_y, fontsize=15)
    plt.grid()
    plt.tight_layout()
    plt.show()


def f_plot_bar(
    df: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
    plt.figure(figsize=(12, 6))

    plt.bar(
        df[columna_x],
        df[columna_y]
    )

    plt.xticks(rotation=45)
    plt.title(titulo if titulo else f'{columna_y} por {columna_x}', fontsize=15)
    plt.xlabel(xlabel if xlabel else columna_x, fontsize=15)
    plt.ylabel(ylabel if ylabel else columna_y, fontsize=15)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def f_plot_barh(
    df: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    titulo: str = None,
    xlabel: str = None,
    ylabel: str = None) -> None:
    
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