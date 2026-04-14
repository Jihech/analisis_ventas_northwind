# 📊 Proyecto de Análisis de Ventas - Dataset Northwind

## 🧠 Descripción del proyecto
Este proyecto es un análisis completo de datos de ventas utilizando el dataset Northwind.

El objetivo es desarrollar un flujo de análisis de datos real aplicando:
- Exploración de datos (EDA)
- Limpieza y transformación
- Análisis de ventas
- Visualización de insights
- Preparación para Power BI

---

## 🎯 Objetivos del proyecto
- Cargar y explorar datos de ventas usando Python (Pandas)
- Realizar análisis exploratorio de datos (EDA)
- Identificar tendencias de ventas e insights de negocio
- Preparar datos para visualización en Power BI
- Practicar un flujo completo de análisis de datos

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

Estas columnas serán transformadas en la fase de limpieza para asegurar un análisis correcto.

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
│
├── data/
│ ├── raw/
│ │ └── ventas.csv
│ └── processed/
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
✔ Estructura del proyecto definida  

---

## 🚀 Próximos pasos
- Limpieza y transformación de datos (Notebook 02)
- Creación de nuevas variables (features)
- Análisis exploratorio avanzado (Notebook 03)
- Visualización de insights (Notebook 04)
- Desarrollo de dashboard en Power BI

---

## 🧠 Nota
Este proyecto simula un flujo real de trabajo en análisis de datos, desde la exploración hasta la visualización final de insights de negocio.