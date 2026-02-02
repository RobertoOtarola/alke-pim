"""
Módulo de Funciones Utilitarias (TASK-019)
------------------------------------------
Funciones puras y reutilizables.
Incluye lógica recursiva para cálculos (TASK-020).
"""

def formatear_precio(valor):
    """
    Convierte un float en string con formato moneda.
    Ej: 1500.5 -> "$ 1,500.50"
    """
    if valor is None:
        return "$ 0.00"
    return f"$ {valor:,.2f}"

def calcular_valor_producto(precio, cantidad):
    """Calcula el total de línea."""
    return precio * cantidad

# --- TASK-020: FUNCIÓN RECURSIVA ---

def sumar_inventario_recursivo(lista_productos, indice=0):
    """
    Calcula la suma total del valor del inventario usando recursividad.

    Args:
        lista_productos (list): La lista de diccionarios.
        indice (int): Puntero actual en la lista.

    Retorna:
        float: La suma acumulada.
    """
    # 1. Caso Base: Si llegamos al final de la lista, la suma es 0
    if indice == len(lista_productos):
        return 0.0

    # 2. Obtener valor actual
    producto = lista_productos[indice]
    valor_actual = producto["precio"] * producto["cantidad"]

    # 3. Llamada Recursiva: Valor actual + Suma del resto de la lista
    return valor_actual + sumar_inventario_recursivo(lista_productos, indice + 1)
