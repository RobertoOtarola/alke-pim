"""
Módulo de Datos Básicos
-----------------------
Responsable de la captura de datos desde la consola, 
conversión de tipos y validación de reglas de negocio
mediante el módulo de validaciones.
"""

# Importamos el módulo hermano
from modulos import validaciones

def solicitar_nombre():
    """Solicita nombre y valida longitud mínima."""
    while True:
        nombre = input("📝 Ingrese el nombre del producto: ").strip()
        if validaciones.validar_nombre_producto(nombre):
            return nombre
        print("⚠️  Error: El nombre debe tener al menos 3 caracteres.")

def solicitar_precio():
    """Solicita precio, valida tipo float y regla de negocio (>0)."""
    while True:
        try:
            entrada = input("💲 Ingrese el precio del producto: ")
            precio = float(entrada)
            
            # TASK-009: Validación condicional robusta
            if validaciones.validar_precio_logico(precio):
                return precio
            else:
                print("⚠️  Error: El precio debe ser mayor a 0 y razonable.")
                
        except ValueError:
            print("⚠️  Error: Debe ingresar un número válido.")

def solicitar_cantidad():
    """Solicita cantidad, valida tipo int y regla de negocio (>=0)."""
    while True:
        try:
            entrada = input("📦 Ingrese la cantidad disponible: ")
            cantidad = int(entrada)
            
            if validaciones.validar_cantidad_logica(cantidad):
                return cantidad
            else:
                print("⚠️  Error: La cantidad no puede ser negativa.")
                
        except ValueError:
            print("⚠️  Error: Debe ingresar un número entero.")

def solicitar_categoria():
    """Solicita categoría (sin validación compleja por ahora)."""
    while True:
        categoria = input("🗂️  Ingrese la categoría: ").strip()
        if len(categoria) > 0:
            return categoria
        print("⚠️  Error: La categoría no puede estar vacía.")