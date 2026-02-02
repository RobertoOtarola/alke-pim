"""
Módulo de Datos Básicos
-----------------------
Responsable de la captura de datos desde la consola y
la conversión básica de tipos (str, int, float).
"""

def solicitar_nombre():
    """
    Solicita el nombre del producto al usuario.
    
    Retorna:
        str: El nombre ingresado.
    """
    # Se usa .strip() para eliminar espacios accidentales al inicio/final
    nombre = input("📝 Ingrese el nombre del producto: ").strip()
    return nombre

def solicitar_precio():
    """
    Solicita el precio y valida que sea un número flotante válido.
    Maneja la excepción ValueError si el usuario ingresa texto.
    
    Retorna:
        float: El precio convertido.
    """
    while True:
        try:
            entrada = input("💲 Ingrese el precio del producto: ")
            precio = float(entrada)
            return precio
        except ValueError:
            print("⚠️  Error: Debe ingresar un número válido (ej: 10.50).")

def solicitar_cantidad():
    """
    Solicita la cantidad y valida que sea un número entero.
    
    Retorna:
        int: La cantidad convertida.
    """
    while True:
        try:
            entrada = input("📦 Ingrese la cantidad disponible: ")
            cantidad = int(entrada)
            return cantidad
        except ValueError:
            print("⚠️  Error: Debe ingresar un número entero.")

def solicitar_categoria():
    """
    Solicita la categoría del producto.
    
    Retorna:
        str: La categoría ingresada.
    """
    categoria = input("🗂️  Ingrese la categoría: ").strip()
    return categoria