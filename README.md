# 📊 Proyecto de Análisis de Datos - Dataset Northwind

## 🧠 Descripción del proyecto
Este proyecto consiste en un análisis completo de datos de ventas utilizando el dataset Northwind.

El objetivo es desarrollar un flujo real de análisis de datos aplicando técnicas de exploración, transformación, análisis y visualización de datos para generar insights de negocio.

---

## 🎯 Objetivos del proyecto
- Cargar y explorar datos de ventas usando Python (Pandas)
- Realizar análisis exploratorio de datos (EDA)
- Identificar tendencias de ventas e insights de negocio
- Transformar y preparar datos para análisis
- Generar visualizaciones e indicadores clave (KPIs)
- Preparar datos para herramientas de BI como Power BI

---

## 🧹 Calidad de los datos

- No se encontraron valores nulos en el dataset.
- No se encontraron registros duplicados.
- El dataset presenta una estructura consistente para análisis.

### ⚠️ Observación sobre tipos de datos
Algunas columnas fueron cargadas como tipo `object`, principalmente:

- fecha
- Mes
- clienteID
- NombreProducto
- NombreCategoria

Estas columnas serán transformadas en la fase de limpieza para optimizar el análisis y el uso de funciones de tiempo y agrupación.

---

## 🛠️ Herramientas utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- SQL (consultas de apoyo)
- Power BI (futuras visualizaciones)

---

## 📁 Estructura del proyecto
analisis-ventas-northwind/
│
├── data/
│ ├── raw/
│ │ └── ventas.csv
│ └── procesado/
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
✔ Calidad de datos validada (sin nulos ni duplicados)  
✔ Identificación de ajustes en tipos de datos  
✔ Estructura del proyecto definida  

---

## 🚧 En proceso
- Limpieza y transformación de datos (Notebook 02)

---

## 🚀 Próximos pasos
- Creación de nuevas variables (feature engineering)
- Análisis exploratorio avanzado (Notebook 03)
- Visualización de insights (Notebook 04)
- Desarrollo de dashboard en Power BI

---

## 🧠 Nota
Este proyecto simula un flujo real de trabajo en análisis de datos, desde la exploración hasta la generación de insights de negocio listos para toma de decisiones.