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
analisis-ventas-northwind/
│
├── data/
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
├── python/
├── powerbi/
├── images/
└── docs/
```

---
## 📌 Progreso actual
- Repositorio creado en GitHub  
- Dataset cargado correctamente  
- Exploración de datos completada (Notebook 01)  
- Limpieza y transformación de datos completada (Notebook 02)  
- Dataset limpio generado (`ventas_limpio.csv`)  
- Análisis de ventas en desarrollo (Notebook 03)  

---

## 🚧 En proceso
- Análisis de ventas (KPIs, productos y tendencias)
- Creación de visualizaciones con matplotlib

---

## 📊 Insights principales
- Ventas por mes
	- Las ventas muestran una tendencia general de crecimiento a lo largo del tiempo, evidenciando una evolución positiva del negocio
	- A partir de 1998 se observa incremento significativo en el volumen de ventas, superando los $100k mensuales.
	- Se detecta posible anomalía en el último mes (caída abrupta), que podrían estar relacionadas con datos incompletos o factores externos

- Top 10 productos por ventas
	- Se observa que las ventas están altamente concentradas en pocos productos, destacando *Côte de Blaye* como el principal generador de ingresos, con una diferencia significativa frente al resto.
	
## 📌 Sugerencias
- Validar los datos de mayo de 1998 para confirmar si la caída en ventas corresponde a una anomalía o a información incompleta, ya que este punto puede distorsionar la interpretación de la tendencia general.
- Se recomienda analizar estrategias para potenciar los productos de mayor demanda y evaluar oportunidades de diversificación del catálogo de productos.

---

## 🚀 Próximos pasos
- Finalizar análisis exploratorio (Notebook 03)
- Completar visualizaciones (Notebook 04)
- Construcción de dashboard en Power BI

---

## 🧠 Nota
Este proyecto simula un flujo real de trabajo en análisis de datos, desde la exploración hasta la generación de insights que pueden apoyar la toma de decisiones.
