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

```
## 🛠️ Herramientas utilizadas
- Python (Pandas, Matplotlib, Typing)
- SQL Server
- Jupyter Notebook
- Power BI
- Git y GitHub

---

## 📁 Estructura del Proyecto

analisis-ventas-northwind/
│
├── dataset/
│   ├── raw/                      # Datos originales (sin modificar)
│   └── procesado/                # Datos limpios y transformados
│
├── notebooks/                    
│   ├── 01_carga_exploracion_datos.ipynb
│   ├── 02_limpieza_transformacion_datos.ipynb
│   ├── 03_analisis.ipynb
│   └── 04_visualizaciones.ipynb
│
├── python/
│   └── src/                      # Módulos reutilizables
│       ├── __init__.py
│       ├── cargar_datos.py
│       ├── exploracion_datos.py
│       ├── limpieza_datos.py
│       ├── analisis.py
│       └── visualizaciones.py
│
├── sql_scripts/                  # Query SQL para análisis
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
│       ├── modelo_datos_northwind_sqlserver.png
│       ├── nueva_medida_y_nueva_tabla.png
│       └── dashboard_resumen.png
│
├── powerbi/
│   └── dashboard_ventas_northwind.pbix   
│
└── docs/                         
                        

---

## 📌 Estado del proyecto

- Repositorio creado en GitHub - completada
- Dataset cargado correctamente - completada  
- Exploración de datos (EDA) - completada  
- Limpieza y transformación de datos - completada  
- Análisis de ventas - completada  
- Visualizaciones con Matplotlib - completada
- Consultas SQL desarrolladas - completada
- Evidencias Querys guardadas en imágenes - completada
- Importe de tablas de Base de datos Northwind de SQLSERVER a PowerBI - completada
- Creación de medidas para realizar cálculos dinámicos - en progreso
- Evidencias Dashboard guardadas en imágenes - en progreso
- Dashboard Resumen - completado
- Dashboard Producto - en progreso

---

## 🧠 Metodología de trabajo

El proyecto ha sido estructurado siguiendo buenas prácticas de análisis de datos:

- Modularización del código en Python (funciones reutilizables)
- Separación por etapas: carga, EDA, limpieza, análisis y visualizaciones
- Reutilización de funciones en notebooks principales (01, 02, 03, 04)
- Integración de análisis en Python y SQL
- Generación de evidencias visuales en imágenes
- Generación de dashboard con 4 dimensiones de base de datos northwind

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

## 📌 Evidencias del proyecto
- Consultas SQL almacenadas en `sql_scripts/`
- Resultados visuales en `imagenes/sql_resultados/`
- Análisis y representaciones gráficas en Jupyter Notebook
- Funciones reutilizables en `python/src/`
- Dashboard en Power BI con datos importados desde SQL Server
- Dashboard en desarrollo en Power BI
- Resultados dashboard en `imagenes/powerbi_resultados/`

---

## 🧠 Nota final
Este proyecto simula un flujo real de trabajo en análisis de datos, aplicando buenas prácticas de organización, reutilización de código y generación de insights orientados al negocio.

