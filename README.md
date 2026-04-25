```
# 📊 Proyecto de Análisis de Datos - Dataset Northwind

## 🧠 Descripción del proyecto
Este proyecto consiste en el análisis de datos de ventas del dataset Northwind con el objetivo de entender el comportamiento del negocio y generar insights que apoyen la toma de decisiones.

Se implementa un flujo completo de trabajo de Data Analytics: carga de datos, exploración (EDA), limpieza, transformación, análisis y visualización utilizando Python, SQL Server y Power BI.

Además, el análisis se desarrolla en *Jupyter (Python)*, *SQL Server*, *Power BI* con fines específicos, permitiendo validar la consistencia de los resultados y comprender el flujo de datos en distintos entornos.

Los dashboard se realizó aplicando filtros Top N (Top 10) basados en ventas totales para priorizar el análisis en productos y clientes de mayor impacto

---

## 🎯 Objetivos del proyecto
- Explorar y comprender la estructura del dataset  
- Realizar limpieza y transformación de datos  
- Aplicar análisis exploratorio (EDA)  
- Construir KPIs de ventas  
- Identificar tendencias y patrones de negocio  
- Generar insights accionables  
- Desarrollar dashboards interactivos en Power BI  

---

## 🛠️ Herramientas utilizadas
- Python (Pandas, Matplotlib, Typing)  
- SQL Server  
- Jupyter Notebook  
- Power BI (modelado de datos y DAX)  
- Git y GitHub  

---

## 🔄 Enfoque de análisis (Multi-herramienta)

El análisis fue desarrollado en multiples herramientas, cada una con un propósito específico dentro del flujo de trabajo:

- **SQL Server:** extracción, transformación y agregación de datos  
- **Jupyter Notebook (Python):** exploración, limpieza y análisis detallado  
- **Power BI:** modelado de datos, implementación de medidas con DAX y visualización  

Este enfoque permite validar métricas clave en distintos entornos y reforzar la confiabilidad del análisis.

---

## ♻️ Reutilización de código (Python)

El proyecto implementa una estructura modular en Python mediante funciones reutilizables, lo que permite:

- Separar la lógica por etapas (carga, exploración, limpieza, análisis y visualización)  
- Reutilizar código en diferentes notebooks  
- Facilitar el mantenimiento y escalabilidad del proyecto  
- Mantener un flujo de trabajo más ordenado

Las funciones se encuentran organizadas en el directorio: `python/src/`

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
│       ├── 01_modelo_datos_northwind_sqlserver.png
│       ├── 02_nueva_tabla.png
│       ├── 03_dashboard_resumen.png
│       ├── 04_dashboard_productos.png
│       └── 05_dashboard_clientes.png
│
├── powerbi/
│   └── dashboard_ventas_northwind.pbix   
│
└── docs/
    └── documentacion.md  

---

## 📌 Estado del proyecto

- Dataset cargado y validado   
- Exploración de datos (EDA)  
- Limpieza y transformación   
- Análisis de ventas  
- Consultas SQL desarrolladas 
- Validación de resultados entre SQL y Python  
- Visualizaciones en Python  
- Modelado de datos en Power BI 
- Implementación de medidas con DAX 
- Dashboard en Power BI 

---

## 🧠 Metodología de trabajo

El proyecto sigue buenas prácticas de análisis de datos:

- Separación por etapas: carga, EDA, limpieza, análisis y visualización  
- Modularización del código en Python (funciones reutilizables)  
- Integración de SQL y Python para validación de resultados  
- Modelado de datos en Power BI  
- Creación de medidas dinámicas con DAX  
- Generación de dashboards orientados a negocio  

---

## 📊 Análisis realizados

- Tendencia de ventas y crecimiento mensual  
- Ranking de productos (ingresos y volumen)  
- Análisis de categorías (participación y evolución)  
- Variación porcentual de ventas  

---

## 📌 Insights principales

- Existe concentración de ingresos en un grupo reducido de productos (principio de Pareto).  
- Las categorías **Beverages** y **Dairy Products** lideran las ventas.  
- Se identifican variaciones mensuales significativas en el comportamiento de ventas.  
- Algunos periodos presentan posibles anomalías que requieren validación adicional.  

---

## 📌 Sugerencias de negocio

- Diversificar el portafolio para reducir dependencia de productos clave  
- Replicar estrategias de productos con alto rendimiento  
- Optimizar inventario en productos de alta rotación  
- Analizar categorías con bajo desempeño  
- Validar inconsistencias en datos históricos, especialmente validar datos del último mes 

---

## 📌 Evidencias del proyecto

- Scripts SQL en `sql_scripts/`  
- Resultados visuales en `imagenes/sql_resultados/`  
- Notebooks de análisis en `notebooks/`  
- Código modular en `python/src/`  
- Dashboard en Power BI (`.pbix`)  
- Visualizaciones del dashboard en `imagenes/powerbi_resultados/`  

---

## 🧠 Nota final

Este proyecto representa un flujo completo de análisis de datos, integrando múltiples herramientas (SQL, Python y Power BI + DAX) para asegurar consistencia, claridad y valor de negocio en los resultados.
