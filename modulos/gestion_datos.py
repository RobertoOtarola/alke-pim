"""
Módulo de Gestión de Datos
--------------------------
Maneja el estado global de la aplicación.
"""
# TASK-022: Imports absolutos y organizados
from modulos import funciones_utiles

# --- SCOPE GLOBAL (TASK-021) ---
# Estas variables son accesibles en todo el módulo.
CATEGORIAS_VALIDAS = ('Electrónica', 'Hogar', 'Indumentaria', 'Juguetería', 'Alimentos')
nombres_registrados = set()
productos = []

def inicializar_datos_prueba():
    global productos, nombres_registrados
    productos.clear()
    nombres_registrados.clear()
    
    # Datos semilla
    datos = [
        ("Laptop Pythonic", 1200.50, 5, "Electrónica", "Tech Corp"),
        ("Monitor 24 pulg", 180.00, 10, "Electrónica", "Screen S.A."),
        ("Cafetera Express", 45.00, 20, "Hogar", "Home Goods")
    ]
    
    for n, p, c, cat, prov in datos:
        crear_producto(n, p, c, cat, {"nombre": prov, "pais": "Importado"})
    
    print("✅ Datos de prueba cargados.")

def crear_producto(nombre, precio, cantidad, categoria, datos_proveedor):
    if nombre in nombres_registrados:
        return False

    nuevo_id = 1 if not productos else productos[-1]["id"] + 1
    
    # Usamos la utilidad para cálculo
    valor_total = funciones_utiles.calcular_valor_producto(precio, cantidad)
    
    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "proveedor": datos_proveedor,
        "valor_inventario": valor_total,
        "nivel_precio": "Premium" if precio >= 500 else "Económico",
        "estado_stock": "⚠️ BAJO" if cantidad <= 5 else "✅ OK"
    }

    productos.append(producto)
    nombres_registrados.add(nombre)
    return True

# --- Wrapper para la recursividad ---

def obtener_total_inventario():
    """
    Función pública que llama a la lógica recursiva interna.
    """
    return funciones_utiles.sumar_inventario_recursivo(productos)

# --- Métodos de búsqueda/filtro (Mantenidos del EPIC anterior) ---

def buscar_producto_por_id(id_producto):
    for p in productos:
        if p["id"] == id_producto: return p
    return None

def eliminar_producto(id_producto):
    p = buscar_producto_por_id(id_producto)
    if p:
        nombres_registrados.remove(p["nombre"])
        productos.remove(p)
        return True
    return False

def actualizar_stock(id_producto, nueva_cant):
    p = buscar_producto_por_id(id_producto)
    if p:
        p["cantidad"] = nueva_cant
        p["valor_inventario"] = funciones_utiles.calcular_valor_producto(p["precio"], nueva_cant)
        p["estado_stock"] = "⚠️ BAJO" if nueva_cant <= 5 else "✅ OK"
        return True
    return False

def filtrar_por_categoria(cat):
    return [p for p in productos if p["categoria"] == cat]

def obtener_productos_ordenados_precio():
    return sorted(productos, key=lambda p: p["precio"], reverse=True)