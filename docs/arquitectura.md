```markdown
# Documentación de Arquitectura de Software

## 1. Visión General
El sistema **Alke PIM** sigue una arquitectura procedural modularizada. Se ha diseñado para desacoplar la interacción con el usuario (Capa de Presentación) de la lógica de manipulación de datos (Capa de Negocio), facilitando la mantenibilidad y escalabilidad futura.

## 2. Diagrama de Flujo de Datos

El flujo de la información sigue un camino unidireccional estricto para mantener el orden:

1.  **Orquestación (`main.py`):** Inicia el ciclo de vida y mantiene el estado de ejecución.
2.  **Input (`menu.py` / `datos_basicos.py`):** Captura la intención del usuario.
3.  **Validación (`validaciones.py`):** Actúa como *Gatekeeper*. Si los datos no cumplen las reglas (ej. precio > 0), no pasan a la siguiente capa.
4.  **Procesamiento (`gestion_datos.py`):** Si los datos son válidos, se actualizan las estructuras en memoria (`listas`, `sets`).
5.  **Utilidades (`funciones_utiles.py`):** Servicios transversales como formateo de moneda o cálculos matemáticos recursivos.

## 3. Decisiones Técnicas Clave

### A. Uso de Sets para Unicidad
**Problema:** Evitar productos duplicados con el mismo nombre.
**Solución:** Se implementó un `Set` paralelo a la lista de productos.
**Justificación:** La búsqueda en un set es O(1) (instantánea), mientras que recorrer la lista entera para verificar duplicados sería O(n). Esto optimiza el rendimiento.

### B. Tuplas para Categorías
**Problema:** Garantizar que las categorías del negocio no sean modificadas en tiempo de ejecución.
**Solución:** Definición de `CATEGORIAS_VALIDAS` como tupla.
**Justificación:** Las tuplas son inmutables en Python, lo que previene errores accidentales de sobrescritura de datos maestros.

### C. Recursividad en Inventario
**Requerimiento:** Implementar una función recursiva.
**Implementación:** `sumar_inventario_recursivo` en `funciones_utiles.py`.
**Lógica:** La función toma la lista y un índice.
* *Caso Base:* Si el índice iguala la longitud de la lista, retorna 0.
* *Caso Recursivo:* Retorna (Precio * Cantidad) actual + el resultado de llamarse a sí misma con el índice siguiente.

## 4. Estructura de Datos
El modelo de datos reside en memoria (RAM) durante la ejecución:

* **Principal:** Lista de Diccionarios (`productos = []`).
* **Diccionario de Producto:**
    ```python
    {
        "id": int,
        "nombre": str,
        "precio": float,
        "proveedor": { "nombre": str, "pais": str }, # Estructura anidada
        "nivel_precio": str # Campo calculado
    }
    ```
    