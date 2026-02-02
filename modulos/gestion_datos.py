"""
Módulo de Gestión de Datos
--------------------------
Maneja la lista de productos y las operaciones CRUD básicas.
"""

# Lista global que actúa como base de datos en memoria
productos = []

# --- FUNCIONES EXISTENTES (EPIC 1) ---
def inicializar_datos_prueba():
    """
    Carga datos iniciales en la lista de productos para facilitar pruebas.
    """
    global productos
    # Datos semilla (Seed data)
    productos.extend([
        {
            "id": 1,
            "nombre": "Laptop Pythonic",
            "precio": 1200.50,
            "cantidad": 5,
            "categoria": "Electrónica",
            "valor_inventario": 6002.50
        },
        {
            "id": 2,
            "nombre": "Monitor 24 pulg",
            "precio": 180.00,
            "cantidad": 10,
            "categoria": "Electrónica",
            "valor_inventario": 1800.00
        }
    ])
    print("✅ Datos de prueba cargados correctamente.")

# --- NUEVAS FUNCIONES (EPIC 2) ---
def generar_id_nuevo():
    """
    Genera un ID autoincremental simple basado en la longitud de la lista.
    """
    if len(productos) == 0:
        return 1
    # Busca el último ID y le suma 1 para evitar duplicados si se borran elementos
    return productos[-1]["id"] + 1

def crear_producto(nombre, precio, cantidad, categoria):
    """
    Crea un diccionario de producto y lo agrega a la lista global.
    Realiza cálculos derivados como el valor total del inventario del producto.
    """
    nuevo_id = generar_id_nuevo()
    
    # TASK-005: Operadores aritméticos para datos derivados
    valor_total = precio * cantidad 

    # Estructura de Diccionario requerida en la consigna
    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "valor_inventario": valor_total  # Campo calculado
    }

    productos.append(producto)
    return True