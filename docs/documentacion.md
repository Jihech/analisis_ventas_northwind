```
# 📄 Documentación Técnica - Proyecto Northwind

## 🧭 1. Introducción

Este documento describe el flujo técnico del proyecto de análisis de ventas del dataset Northwind, detallando los procesos de extracción, transformación, análisis y visualización de datos.

El objetivo es proporcionar una guía clara para comprender, replicar y escalar el análisis.

---

## 🗂️ 2. Fuente de datos

El dataset utilizado corresponde a la base de datos **Northwind**, la cual contiene información relacionada con:

* Ordenes
* DetalleOrden
* Producto
* Categoria

Los datos fueron trabajados desde SQL Server y posteriormente utilizados en Python y Power BI.

---

## ⚙️ 3. Flujo de trabajo

El proyecto sigue un flujo estructurado de análisis de datos:

1. Extracción de datos (SQL Server)
2. Exploración inicial (Jupyter Notebook)
3. Limpieza y transformación (Python - Pandas)
4. Análisis de datos (Python + SQL)
5. Visualización (Jupyter - Pandas - Matplotlib)
5. Validación de métricas entre herramientas (SQL Server - Python - Power BI)
6. Modelado de datos (Power BI)
7. Creación de medidas con DAX (Power BI)
8. Visualización y construcción de dashboards (Power BI)

---

## 🧪 4. Exploración de datos (EDA)

Durante esta fase se realizaron:

* Revisión de tipos de datos
* Identificación de valores nulos
* Análisis de distribución de variables
* Detección de outliers
* Análisis inicial de relaciones entre tablas

Se utilizaron notebooks para documentar cada paso del proceso.

---

## 🧹 5. Limpieza y transformación de datos

Se aplicaron las siguientes transformaciones:

* Conversión de tipos de datos
* Eliminación o tratamiento de valores nulos
* Creación de nuevas columnas (ej: métricas derivadas)
* Normalización de estructuras para análisis

Estas transformaciones fueron implementadas mediante funciones reutilizables en Python.

---

## ♻️ 6. Arquitectura de código (Python)

El proyecto utiliza una estructura modular para organizar el código:

* `cargar_datos.py` → carga de datasets
* `exploracion_datos.py` → funciones de análisis exploratorio
* `limpieza_datos.py` → funciones de limpieza
* `analisis.py` → cálculos y métricas
* `visualizaciones.py` → gráficos

Esto permite reutilizar lógica y mantener el código escalable y ordenado.

---

## 🗃️ 7. Análisis en SQL Server

Se desarrollaron múltiples consultas SQL para:

* Venta por mes
* Top 10 productos por ventas
* Ventas por categorias
* Top 10 productos mas vendidos
* Ventas categorias por en el tiempo
* Top 5 categorias con mas ventas
* Comparacion de categorias
* Vvolucion productos_top 3 con mas ventas
* Crecimiento porcentual

Estas consultas permiten validar resultados obtenidos en Python.

---

## 🔁 8. Validación de datos

Se replicaron métricas clave en:

* SQL Server
* Python (Pandas)
* Power BI

Esto permitió asegurar consistencia en los resultados y detectar posibles discrepancias.

---

## 📊 9. Modelado de datos en Power BI

Se realizó:

* Importación de tablas desde SQL Server
* Creación de relaciones entre tablas
* Diseño de modelo de datos

El modelo permite análisis dinámico mediante segmentaciones.

---

## 📐 10. Medidas DAX

Se implementaron medidas para cálculos dinámicos, tales como:

* Total de ventas
* Cantidad total vendida
* Número de órdenes
* Participación porcentual
* Métricas de crecimiento

Estas medidas permiten análisis interactivo en los dashboards.

---

## 📈 11. Visualización

Se desarrollaron dashboards enfocados en:

* Resumen general de ventas
* Análisis de productos
* Análisis de clientes

Las visualizaciones permiten identificar patrones y facilitar la toma de decisiones.

---

## ⚠️ 12. Consideraciones

* El dataset es simulado (Northwind)
* Algunos valores pueden presentar inconsistencias
* Los insights deben interpretarse en contexto académico

---

## 🧠 14. Conclusión

El proyecto demuestra un flujo completo de análisis de datos, integrando SQL, Python y Power BI, aplicando buenas prácticas como modularización, validación de resultados y generación de insights orientados al negocio.
