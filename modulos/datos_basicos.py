"""
Módulo de Datos Básicos
-----------------------
Captura y valida entradas del usuario interactuando con las nuevas estructuras.
"""
from modulos import validaciones, gestion_datos

def solicitar_nombre():
    """Solicita el nombre y valida longitud."""
    while True:
        nombre = input("📝 Ingrese el nombre del producto: ").strip()
        if validaciones.validar_nombre_producto(nombre):
            return nombre
        print("⚠️  Error: Nombre inválido (min 3 caracteres).")

def solicitar_precio():
    """Solicita el precio y valida que sea positivo."""
    while True:
        try:
            precio = float(input("💲 Ingrese el precio: "))
            if validaciones.validar_precio_logico(precio):
                return precio
            print("⚠️  Error: Precio debe ser positivo.")
        except ValueError:
            print("⚠️  Debe ser número.")

def solicitar_cantidad():
    """Solicita la cantidad y valida que sea entero no negativo."""
    while True:
        try:
            cant = int(input("📦 Ingrese la cantidad: "))
            if validaciones.validar_cantidad_logica(cant):
                return cant
            print("⚠️  Error: No negativos.")
        except ValueError:
            print("⚠️  Debe ser entero.")

def solicitar_categoria():
    """
    Muestra las categorías disponibles (Tupla) y obliga a elegir una válida.
    """
    print("\n🗂️  Categorías disponibles:")
    for i, cat in enumerate(gestion_datos.CATEGORIAS_VALIDAS, 1):
        print(f"   {i}. {cat}")

    while True:
        entrada = input("👉 Seleccione una categoría (nombre exacto): ").strip()

        if entrada in gestion_datos.CATEGORIAS_VALIDAS:
            return entrada
        print("⚠️  Error: Categoría no válida. Revise el listado.")

def solicitar_datos_proveedor():
    """
    Captura datos para el diccionario anidado del proveedor.
    """
    print("\n🚚 --- Datos del Proveedor ---")
    nombre_prov = input("   Nombre empresa: ").strip()
    pais_prov = input("   País de origen: ").strip()

    return {
        "nombre": nombre_prov,
        "pais": pais_prov
    }

def solicitar_id():
    """Solicita un ID numérico."""
    while True:
        try:
            return int(input("🆔 Ingrese ID: "))
        except ValueError:
            pass

def confirmar_accion(mensaje):
    """Solicita confirmación S/N."""
    return input(f"{mensaje} (S/N): ").upper() == 'S'
