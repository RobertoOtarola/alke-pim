"""
Módulo de Menú Principal
------------------------
Contiene las funciones para mostrar las opciones al usuario
y capturar su selección.
"""

def mostrar_menu_principal():
    """
    Muestra las opciones principales del sistema Alke PIM en consola.
    
    No recibe parámetros.
    No retorna valores, solo imprime en pantalla.
    """
    print("\n" + "=" * 50)
    print("   🛒  ALKE PIM - GESTIÓN DE PRODUCTOS  🛒")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Cargar datos de prueba")
    print("7. Salir")
    print("-" * 50)

def obtener_opcion():
    """
    Captura y devuelve la opción seleccionada por el usuario.
    
    Retorna:
        str: La opción ingresada por el usuario.
    """
    return input("👉 Seleccione una opción: ")
