"""
Módulo de Gestión de Datos
--------------------------
Este módulo maneja la estructura de datos principal del sistema
y las operaciones directas sobre la lista de productos.
"""

# Inicialización de la "Base de Datos" en memoria (EPIC 2 - TASK-006)
productos = []

def inicializar_datos_prueba():
    """
    Carga datos iniciales en la lista de productos para facilitar pruebas.
    
    Retorna:
        None: Modifica la lista global 'productos' in-place.
    """
    global productos
    # Datos semilla (Seed data)
    productos.extend([
        {
            "id": 1,
            "nombre": "Laptop Pythonic",
            "precio": 1200.50,
            "cantidad": 5,
            "categoria": "Electrónica"
        },
        {
            "id": 2,
            "nombre": "Monitor 24 pulg",
            "precio": 180.00,
            "cantidad": 10,
            "categoria": "Electrónica"
        }
    ])
    print("✅ Datos de prueba cargados correctamente.")