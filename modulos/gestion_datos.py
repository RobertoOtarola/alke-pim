"""
Módulo de Gestión de Datos
--------------------------
Maneja la lista de productos y las operaciones CRUD básicas.
Incluye lógica de negocio para categorización automática.
"""

# Lista global que actúa como base de datos en memoria
productos = []

def inicializar_datos_prueba():
    """Carga datos iniciales para pruebas."""
    global productos
    productos.clear() # Limpiamos para evitar duplicados si se llama varias veces
    
    # Usamos la función interna para asegurar que pasen por la lógica de categorización
    crear_producto("Laptop Pythonic", 1200.50, 5, "Electrónica")
    crear_producto("Monitor 24 pulg", 180.00, 10, "Electrónica")
    crear_producto("Mouse Genérico", 15.00, 50, "Accesorios")
    
    print("✅ Datos de prueba cargados correctamente.")

def generar_id_nuevo():
    """Genera ID autoincremental."""
    if len(productos) == 0:
        return 1
    return productos[-1]["id"] + 1

def determinar_nivel_precio(precio):
    """
    TASK-008: Lógica condicional para categorización por precio.
    """
    if precio < 50:
        return "Económico"
    elif 50 <= precio < 500:
        return "Estándar"
    else:
        return "Premium"

def verificar_alerta_stock(cantidad):
    """
    TASK-008: Alerta de stock bajo.
    Retorna un string con la alerta o un string vacío si todo está bien.
    """
    if cantidad <= 5:
        return "⚠️ BAJO STOCK"
    return "✅ OK"

def crear_producto(nombre, precio, cantidad, categoria):
    """
    Crea un diccionario de producto y lo agrega a la lista global.
    Aplica lógica de negocio para campos calculados.
    """
    nuevo_id = generar_id_nuevo()
    valor_total = precio * cantidad 
    
    # Aplicamos lógica de clasificación automática
    nivel = determinar_nivel_precio(precio)
    estado_stock = verificar_alerta_stock(cantidad)

    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "valor_inventario": valor_total,
        "nivel_precio": nivel,       # Campo automático
        "estado_stock": estado_stock # Campo automático
    }

    productos.append(producto)
    return True

def buscar_producto_por_id(id_producto):
    """
    Busca un producto por su ID único.
    
    Args:
        id_producto (int): ID a buscar.
        
    Retorna:
        dict: El producto encontrado o None si no existe.
    """
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None

def eliminar_producto(id_producto):
    """
    Elimina un producto de la lista por su ID.
    
    Args:
        id_producto (int): ID del producto a eliminar.
        
    Retorna:
        bool: True si se eliminó, False si no se encontró.
    """
    producto = buscar_producto_por_id(id_producto)
    if producto:
        productos.remove(producto)
        return True
    return False

def actualizar_stock(id_producto, nueva_cantidad):
    """
    Actualiza el stock de un producto y recalcula su estado.
    """
    producto = buscar_producto_por_id(id_producto)
    if producto:
        producto["cantidad"] = nueva_cantidad
        # Recalcular campos dependientes
        producto["valor_inventario"] = producto["precio"] * nueva_cantidad
        producto["estado_stock"] = verificar_alerta_stock(nueva_cantidad)
        return True
    return False