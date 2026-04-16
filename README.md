# 📊 Proyecto de Análisis de Datos - Dataset Northwind

## 🧠 Descripción del proyecto
En este proyecto analizo datos de ventas del dataset Northwind con el objetivo de entender el comportamiento de las ventas y obtener insights de negocio.

Sigo un flujo real de trabajo como Data Analyst: exploración de datos, limpieza, transformación, análisis y visualización, utilizando Python.

---

## 🎯 Objetivos del proyecto
- Explorar y entender los datos de ventas
- Limpiar y preparar los datos para el análisis
- Identificar tendencias y patrones importantes
- Generar indicadores clave (KPIs)
- Preparar la información para su visualización en Power BI

---

## 🧹 Calidad de los datos

- No se encontraron valores nulos en el dataset
- No se encontraron registros duplicados
- El dataset presenta una estructura consistente para análisis

### ⚠️ Observación sobre tipos de datos
Algunas columnas fueron cargadas como tipo `object`, principalmente:

- `fecha`
- `Mes`
- `clienteID`
- `NombreProducto`
- `NombreCategoria`

Durante la fase de limpieza, estas columnas fueron transformadas para asegurar un análisis correcto, especialmente en variables de tipo fecha.

---

## 🛠️ Herramientas utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- SQL (consultas de apoyo)
- Power BI (visualización final)

---

## 📁 Estructura del proyecto
```
```
analisis-ventas-northwind/
│
├── dataset/
│   ├── raw/
│   │   └── ventas.csv
│   └── procesado/
│       └── ventas_limpio.csv
│
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_limpieza_datos.ipynb
│   ├── 03_analisis_ventas.ipynb
│   └── 04_visualizaciones.ipynb
│
├── sql_scripts/
│   ├── 01_ventas_por_mes.sql
│   ├── 02_top_10_productos_por_ventas.sql
│   ├── 03_ventas_por_categoria.sql
│   ├── 04_top_10_productos_mas_vendidos.sql
│   ├── 05_ventas_de_categoria_por_mes.sql
│   ├── 06_top_5_categoria_con_mas_ventas.sql
│   ├── 07_comparacion_de_categorias.sql
│   ├── 08_evolucion_productos_top_3_con_mas_ventas.sql
│   └── 09_crecimiento_porcentual.sql
│
├── python/
│   ├── carga/
│   │   ├── __init__.py
│   │   └── cargar_datos.py
│   │
│   └── limpieza/
│       ├── __init__.py
│       └── limpieza_datos.py
│
├── powerbi/
│
├── imagenes/
│   ├── sql_resultados/
│   │   ├── 01_venta_por_mes.png
│   │   ├── 02_top_10_productos_por_ventas.png
│   │   ├── 03_ventas_por_categorias.png
│   │   ├── 04_top_10_productos_mas_vendidos.png
│   │   ├── 05_ventas_categorias_por_mes.png
│   │   ├── 06_top_5_categorias_con_mas_ventas.png
│   │   ├── 07_comparacion_de_categorias.png
│   │   ├── 08_evolucion_productos_top_3_con_mas_ventas.png
│   │   └── 09_crecimiento_porcentual.png
│   │
│   └── powerbi_resultados/
│
└── docs/

```

---
## 📌 Progreso actual
- Repositorio creado en GitHub  
- Dataset cargado correctamente  
- Exploración de datos completada (Notebook 01)  
- Limpieza y transformación de datos completada (Notebook 02)  
- Dataset limpio generado (`ventas_limpio.csv`)  
- Análisis de ventas (Notebook 03) 
- Análisis de ventas y visualizaciones con matplotlib (Notebook 04)
- Insights de las visualizaciones (Notebook 04)

---

## 🚧 En proceso
- Análisis de ventas (KPIs, productos y tendencias)
- Creación de visualizaciones con matplotlib
- Querys de SQL Server

---

## 📊 Insights del análisis de ventas
- Ventas por mes
	- Las ventas muestran una tendencia general de crecimiento a lo largo del tiempo, evidenciando una evolución positiva del negocio
	- A partir de 1998 se observa incremento significativo en el volumen de ventas, superando los $100k mensuales.
	- Se detecta posible anomalía en el último mes (caída abrupta), que podrían estar relacionadas con datos incompletos o factores externos

- Top 10 productos por ventas
	- Se observa que las ventas están altamente concentradas en pocos productos, destacando *Côte de Blaye* como el principal generador de ingresos, con una diferencia significativa frente al resto.
	
- Ventar por categoria
	- Las ventas están distribuidas entre varias categorías, destacando *Beverages* y *Dairy Products* como las de mayor aporte a los ingresos, ambas superando los $250k.

- Top 10 productos más vendidos
	- Los productos con mayor volumen en ventas están liderados por *Camembert Pierro*, *Raclette Courdavault* lo que indica una alta demanda en términos de unidades.

- Ventas de Categoria en el tiempo
	- Se obersvan picos en 1998, especialmente en *Beverages* y *Dairy Products*, junto a una caída general en mayo de 1998 que podría indicar una anomalía o datos incompletos.

- Top  categorias con mayor ventas en el tiempo
	- Las categorías líderes como *Beverages* y *Dairy Products* impulsan los principales picos de ventas, mientras que otras como *Confections* y *Meat/Poultry* presentan mayor variabilidad.

- Comparación de Categorias con menores ventas vs la categoria lider
	- Existe una brecha significativa entre *Beverages* y categorías como *Condiments*, *Grains/Cereals* y *Produce*, las cuales presentan un crecimiento más limitado y menor impacto en los ingresos.

- Evolución de productos más vendidos 
	- Los productos líderes presentan ventas con alta variabilidad, dependiendo de picos de demanda más que de un crecimiento sostenido.

- Crecimiento porcentual de ventas mensuales
	- El crecimiento de las ventas presenta alta volatilidad, con picos positivos y caídas pronunciadas, lo que indica un comportamiento irregular en el tiempo.

## 📌 Sugerencias
- Validar los datos de mayo de 1998 para confirmar si la caída en ventas corresponde a una anomalía o a información incompleta, ya que este punto puede distorsionar la interpretación de la tendencia general.

- Se recomienda analizar estrategias para potenciar los productos de mayor demanda y evaluar oportunidades de diversificación del catálogo de productos.

- Se sugiere fortalecer las categorias con mayor aporte como *Beverages* y *Dairy Products*, aprovechando su alta demanda para impulsar estrategias de crecimiento y fidelización.

- Se recomienda asegurar la disponibilidad y stock los productos de mayor volumen en ventas, clave para mantener el flujo connstante de ventas.

- Analizar el crecimiento en 1998, como *Beverages* y *Dairy Products* para identificar los factores que impulsaron su crecimiento y replicar la estrategia en otras categorias, validar datos de mayo de 1998.

- Analizar la variabilidad en categorías como *Confections* y *Meat/Poultry*, y replicar estrategias de categorías líderes como *Beverages* y *Dairy Products* para lograr un crecimiento más estable.

- Se sugiere impulsar las estrategias en categorias de menor desempeño para diversificar los ingresos y reducir la dependencia de las categorias lideres. 

- Analizar los factores que impulsan los picos de ventas para mejorar la estabilidad en el tiempo.

- Evaluar los factores de crecimiento y caída para mejorar la estabilidad y validar posibles anomalías en los datos del último mes.

---

## 🚀 Próximos pasos
- Finalizar análisis exploratorio (Notebook 03)
- Completar visualizaciones (Notebook 04)
- Construcción de dashboard en Power BI

---

## 🧠 Nota
Este proyecto simula un flujo real de trabajo en análisis de datos, desde la exploración hasta la generación de insights que pueden apoyar la toma de decisiones.
