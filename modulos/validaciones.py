"""
Módulo de Validaciones
----------------------
Contiene funciones puras para validar reglas de negocio.
Retorna True/False o lanza excepciones, sin interactuar con la consola.
"""

def validar_nombre_producto(nombre):
    """
    Valida que el nombre no esté vacío y tenga una longitud mínima.
    
    Args:
        nombre (str): El nombre a validar.
        
    Retorna:
        bool: True si es válido, False si no.
    """
    if not nombre:
        return False
    if len(nombre.strip()) < 3:
        return False
    return True

def validar_precio_logico(precio):
    """
    Valida que el precio sea un número positivo mayor a 0.
    (TASK-007)
    """
    if precio <= 0:
        return False
    if precio > 1000000: # Ejemplo de regla de tope máximo (opcional)
        return False
    return True

def validar_cantidad_logica(cantidad):
    """
    Valida que la cantidad sea un entero positivo o cero.
    (TASK-007)
    """
    if cantidad < 0:
        return False
    return True
