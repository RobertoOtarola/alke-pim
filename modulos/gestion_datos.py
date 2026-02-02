"""
Módulo de Gestión de Datos
--------------------------
Maneja el CRUD y estructuras avanzadas (Sets, Tuplas, List Comprehensions).
"""

# TASK-014: Tupla para categorías inmutables (Definida al inicio)
CATEGORIAS_VALIDAS = ('Electrónica', 'Hogar', 'Indumentaria', 'Juguetería', 'Alimentos')

# TASK-015: Set para controlar unicidad de nombres de productos
nombres_registrados = set()

# Lista global de productos
productos = []

def inicializar_datos_prueba():
    """Carga datos iniciales respetando las nuevas estructuras."""
    global productos, nombres_registrados
    productos.clear()
    nombres_registrados.clear()
    
    # Datos semilla con estructura actualizada (Diccionario anidado)
    crear_producto("Laptop Pythonic", 1200.50, 5, "Electrónica", 
                   {"nombre": "Tech Corp", "pais": "China"})
    crear_producto("Monitor 24 pulg", 180.00, 10, "Electrónica", 
                   {"nombre": "Screen S.A.", "pais": "Corea"})
    crear_producto("Cafetera Express", 45.00, 20, "Hogar", 
                   {"nombre": "Home Goods", "pais": "Italia"})
    
    print("✅ Datos de prueba cargados con estructuras avanzadas.")

def generar_id_nuevo():
    if len(productos) == 0:
        return 1
    return productos[-1]["id"] + 1

def determinar_nivel_precio(precio):
    if precio < 50: return "Económico"
    elif 50 <= precio < 500: return "Estándar"
    else: return "Premium"

def verificar_alerta_stock(cantidad):
    return "⚠️ BAJO STOCK" if cantidad <= 5 else "✅ OK"

def crear_producto(nombre, precio, cantidad, categoria, datos_proveedor):
    """
    Crea un producto validando unicidad con Sets y agregando proveedor.
    Args:
        datos_proveedor (dict): Diccionario anidado (TASK-016)
    """
    # TASK-015: Validación de unicidad usando Set (Búsqueda rápida)
    if nombre in nombres_registrados:
        print(f"⚠️  Error: El producto '{nombre}' ya existe.")
        return False

    nuevo_id = generar_id_nuevo()
    valor_total = precio * cantidad
    
    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "valor_inventario": valor_total,
        "nivel_precio": determinar_nivel_precio(precio),
        "estado_stock": verificar_alerta_stock(cantidad),
        "proveedor": datos_proveedor # TASK-016: Diccionario anidado
    }

    productos.append(producto)
    nombres_registrados.add(nombre) # Actualizamos el set
    return True

# --- Métodos de Búsqueda y Actualización ---

def buscar_producto_por_id(id_producto):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None

def eliminar_producto(id_producto):
    producto = buscar_producto_por_id(id_producto)
    if producto:
        nombres_registrados.remove(producto["nombre"]) # Mantenemos el set sincronizado
        productos.remove(producto)
        return True
    return False

def actualizar_stock(id_producto, nueva_cantidad):
    producto = buscar_producto_por_id(id_producto)
    if producto:
        producto["cantidad"] = nueva_cantidad
        producto["valor_inventario"] = producto["precio"] * nueva_cantidad
        producto["estado_stock"] = verificar_alerta_stock(nueva_cantidad)
        return True
    return False

# --- TASK-017: Nuevos métodos de manipulación de colecciones (Al final) ---

def filtrar_por_categoria(categoria_buscar):
    """Usa List Comprehension para filtrar."""
    return [p for p in productos if p["categoria"] == categoria_buscar]

def obtener_productos_ordenados_precio():
    """Usa sorted() con función lambda para ordenar sin modificar la original."""
    return sorted(productos, key=lambda p: p["precio"], reverse=True)