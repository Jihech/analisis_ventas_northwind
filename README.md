# 📊 Proyecto de Análisis de Datos - Dataset Northwind

## 🧠 Descripción del proyecto
Este proyecto consiste en un análisis de datos de ventas utilizando el dataset Northwind, aplicando un flujo completo de trabajo de un Data Analyst.

Se desarrollan etapas de exploración, limpieza, transformación y análisis de datos para generar insights de negocio y preparar la información para su visualización en herramientas de Business Intelligence como Power BI.

---

## 🎯 Objetivos del proyecto
- Cargar y explorar datos de ventas usando Python (Pandas)
- Realizar análisis exploratorio de datos (EDA)
- Transformar y preparar datos para análisis
- Identificar tendencias de ventas e insights de negocio
- Generar indicadores clave (KPIs)
- Preparar datos para visualización en Power BI

---

## 🧹 Calidad de los datos

- No se encontraron valores nulos en el dataset.
- No se encontraron registros duplicados.
- El dataset presenta una estructura consistente para análisis.

### ⚠️ Observación sobre tipos de datos
Algunas columnas fueron cargadas como tipo "object", principalmente:

- fecha
- Mes
- clienteID
- NombreProducto
- NombreCategoria

Estas columnas fueron transformadas durante la fase de limpieza para permitir un análisis correcto, especialmente en variables temporales.

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

analisis-ventas-northwind/
│
├── data/
│ ├── raw/
│ │ └── ventas.csv
│ └── processed/
│ └── ventas_limpio.csv
│
├── notebooks/
│ ├── 01_exploracion_datos.ipynb
│ ├── 02_limpieza_datos.ipynb
│ ├── 03_analisis_ventas.ipynb
│ └── 04_visualizaciones.ipynb
│
├── sql_scripts/
├── python/
├── powerbi/
├── images/
└── docs/

---

## 📌 Progreso actual
✔ Repositorio creado en GitHub  
✔ Dataset cargado correctamente  
✔ Exploración inicial de datos completada (Notebook 01)  
✔ Limpieza y transformación de datos completada (Notebook 02)  
✔ Dataset limpio generado (`ventas_limpio.csv`)  
✔ Inicio del análisis de ventas (Notebook 03)  

---

## 🚧 En proceso
- Análisis de ventas (KPIs, productos, tendencias)

---

## 🚀 Próximos pasos
- Finalizar análisis exploratorio (Notebook 03)
- Generar visualizaciones de insights (Notebook 04)
- Construcción de dashboard en Power BI

---

## 🧠 Nota
Este proyecto simula un flujo real de trabajo en análisis de datos, desde la exploración hasta la generación de insights de negocio orientados a la toma de decisiones.