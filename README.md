# 🛒 Alke PIM (Product Information Management)

Sistema de gestión de inventario desarrollado en Python como proyecto final del Módulo 3 (Bootcamp Alkemy). Este sistema implementa una arquitectura modular para realizar operaciones CRUD completas en memoria, destacando el uso de estructuras de datos avanzadas y algoritmos recursivos.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Completed-success)

## 🚀 Características Principales

* **Gestión Integral:** Alta, baja, modificación (stock) y lectura de productos.
* **Validaciones Robustas:** Prevención de errores en tipos de datos y reglas de negocio (precios positivos, nombres únicos).
* **Reportes Avanzados:** Filtrado por categorías y ordenamiento por precio.
* **Algoritmo Recursivo:** Cálculo del valor total del inventario sin bucles iterativos.

## 🛠️ Tecnologías y Estructuras

* **Lenguaje:** Python 3.x
* **Control de Versiones:** Git & GitHub
* **Metodología:** Scrumban

### Implementación Técnica (Highlights)
* **Tuplas:** Utilizadas en `CATEGORIAS_VALIDAS` para garantizar la inmutabilidad de las categorías del negocio.
* **Sets:** Utilizados en `nombres_registrados` para validación de unicidad O(1) en el alta de productos.
* **Diccionarios Anidados:** Para gestionar la relación `Producto -> Proveedor`.
* **Modularización:** Separación estricta entre UI (`menu.py`), Lógica (`gestion_datos.py`) y Validaciones (`validaciones.py`).

## ⚡ Guía de Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/alke_pim.git](https://github.com/TU_USUARIO/alke_pim.git)
    cd alke_pim
    ```

2.  **Ejecutar el sistema:**
    ```bash
    python main.py
    ```

3.  **Navegación del Menú:**
    * **Opción 1:** Alta de producto (Sigue los prompts en pantalla).
    * **Opción 2:** Ver tabla de productos formateada.
    * **Opción 8:** Acceder a reportes avanzados y prueba de recursividad.
    * **Opción 6:** Cargar datos de prueba (Seed Data) automáticamente.

## 📂 Estructura del Proyecto

```text
alke-pim/
├── main.py                  # Orquestador del sistema
├── README.md                # Documentación general
├── modulos/
│   ├── datos_basicos.py     # Captura de Inputs
│   ├── gestion_datos.py     # Lógica CRUD y Estado
│   ├── validaciones.py      # Reglas de negocio puras
│   ├── menu.py              # Interfaz de consola
│   └── funciones_utiles.py  # Formateo y Recursividad
└── docs/
    ├── arquitectura.md      # Decisiones de diseño
    └── INFORME_VALIDACION.md # Pruebas funcionales

📋 Autor
Roberto Otárola - Desarrollador Fullstack Python Trainee