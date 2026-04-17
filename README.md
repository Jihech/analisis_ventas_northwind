# 📊 Proyecto de Análisis de Datos - Dataset Northwind

## 🧠 Descripción del proyecto
Este proyecto consiste en el análisis de datos de ventas del dataset Northwind, con el objetivo de entender el comportamiento del negocio y generar insights que apoyen la toma de decisiones.

Se sigue un flujo completo de trabajo como Data Analyst: carga de datos, exploración (EDA), limpieza, transformación, análisis y visualización utilizando Python, SQL y herramientas de BI.

El proyecto se encuentra en desarrollo, con las principales fases ya implementadas mediante funciones reutilizables en Python y análisis complementario en SQL.

---

## 🎯 Objetivos del proyecto
- Explorar y comprender la estructura del dataset
- Realizar limpieza y transformación de datos
- Aplicar análisis exploratorio (EDA)
- Construir KPIs de ventas
- Identificar tendencias y patrones de negocio
- Generar insights accionables
- Preparar datos para visualización en Power BI

---

## 🛠️ Herramientas utilizadas
- Python (Pandas, NumPy, Matplotlib)
- SQL Server
- Jupyter Notebook
- Power BI
- Git y GitHub

---

## 📁 Estructura del proyecto

analisis-ventas-northwind/
│
├── dataset/
│   ├── raw/
│   └── procesado/
│
├── notebooks/
│   ├── 01_carga_datos.ipynb
│   ├── 02_exploracion_datos.ipynb
│   ├── 03_limpieza_datos.ipynb
│   └── 04_analisis_ventas.ipynb
│
├── python/
│   ├── a_carga/
│   │   ├── __init__.py
│   │   └── cargar_datos.py
│   │
│   ├── b_eda/
│   │   ├── __init__.py
│   │   └── exploracion_datos.py
│   │
│   ├── c_limpieza/
│   │   ├── __init__.py
│   │   └── limpieza_datos.py
│   │
│   └── d_analisis/
│       ├── __init__.py
│       └── analisis.py
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
├── powerbi/
│
└── docs/

---

## 📌 Estado del proyecto

✔ Repositorio creado en GitHub  
✔ Dataset cargado correctamente  
✔ Exploración de datos (EDA) completada  
✔ Limpieza y transformación de datos completada  
✔ Análisis de ventas en progreso  
✔ Visualizaciones con Matplotlib en progreso  
✔ Consultas SQL desarrolladas  
✔ Evidencias guardadas en imágenes  

---

## 🧠 Metodología de trabajo

El proyecto ha sido estructurado siguiendo buenas prácticas de análisis de datos:

- Modularización del código en Python (funciones reutilizables)
- Separación por etapas: carga, EDA, limpieza y análisis
- Reutilización de funciones en notebooks principales (01, 02 y 03)
- Integración de análisis en Python y SQL
- Generación de evidencias visuales en imágenes

---

## 📊 Análisis realizados

- Análisis de ventas en el tiempo (tendencia y crecimiento mensual)
- Análisis de productos (ranking por ingresos y volumen de ventas)
- Análisis de categorías (participación y comportamiento en el tiempo)
- Análisis de crecimiento de ventas (variación porcentual mensual)

---

## 📌 Insights principales

- Las ventas presentan una tendencia general creciente con variaciones mensuales significativas.
- Existe una alta concentración de ingresos en pocos productos y categorías.
- Las categorías **Beverages** y **Dairy Products** concentran gran parte de los ingresos.
- El comportamiento mensual de las ventas es volátil, con picos y caídas pronunciadas.
- Se identifican posibles anomalías en ciertos periodos del dataset que requieren validación.

---

## 📌 Sugerencias de negocio

- Diversificar el portafolio de productos para reducir dependencia de categorías líderes.
- Analizar patrones de demanda para replicar estrategias exitosas.
- Garantizar disponibilidad de productos de alta rotación.
- Evaluar el comportamiento de categorías con menor rendimiento.
- Validar posibles anomalías en los datos históricos.

---

## 🚧 En progreso
- Finalización del análisis exploratorio (Notebook 03)
- Mejora de visualizaciones (Notebook 04)
- Integración con Power BI
- Optimización de consultas SQL
- Desarrollo de KPIs adicionales

---

## 📌 Evidencias del proyecto
- Consultas SQL almacenadas en `sql_scripts/`
- Resultados visuales en `imagenes/sql_resultados/`
- Análisis en Jupyter Notebook
- Dashboard en desarrollo en Power BI

---

## 🧠 Nota final
Este proyecto simula un flujo real de trabajo en análisis de datos, aplicando buenas prácticas de organización, reutilización de código y generación de insights orientados al negocio.

