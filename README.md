# 🛒 Alke PIM (Product Information Management)

Sistema de gestión de información de productos desarrollado en Python. Este proyecto implementa una arquitectura modular para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un inventario en memoria, aplicando estructuras de datos avanzadas y algoritmos recursivos.

## 🚀 Características Principales

- **Gestión de Productos:** Alta, baja, modificación y lectura de productos.
- **Validaciones Robustas:** Control de tipos de datos y reglas de negocio (precios positivos, nombres únicos).
- **Estructuras Avanzadas:** - `Sets` para garantizar unicidad de SKUs/Nombres.
  - `Tuplas` para categorías inmutables.
  - `Diccionarios Anidados` para gestión de proveedores.
- **Algoritmos:** Implementación de recursividad para cálculos de inventario.
- **Persistencia:** Almacenamiento volátil (en memoria) con carga inicial de datos semilla.
- **Interfaz:** CLI (Interfaz de Línea de Comandos) interactiva y formateada.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Control de Versiones:** Git & GitHub
- **Metodología:** Scrumban (Gestión de tareas)
- **Estilo:** PEP 8 Compliant

## 📂 Estructura del Proyecto

```text
alke-pim/
├── main.py                  # Punto de entrada (Entry Point)
├── README.md                # Documentación principal
├── .gitignore               # Exclusiones de Git
├── modulos/                 # Paquete de módulos
│   ├── __init__.py          # Inicializador de paquete
│   ├── datos_basicos.py     # Capa de entrada (Inputs)
│   ├── gestion_datos.py     # Lógica de negocio y Datos
│   ├── validaciones.py      # Reglas de validación pura
│   ├── menu.py              # Interfaz de usuario (UI)
│   └── funciones_utiles.py  # Utilidades y Recursividad
└── docs/                    # Documentación técnica adicional