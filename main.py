"""
Archivo Principal (Entry Point)
-------------------------------
Punto de entrada del sistema Alke PIM. Coordina el flujo
entre el menú y los módulos de lógica.
"""

import sys
# Importación absoluta desde el paquete 'modulos'
from modulos import menu, gestion_datos

def main():
    """
    Función principal que ejecuta el bucle del sistema.
    """
    # Mensaje de bienvenida (TASK-003)
    print(f"Iniciando sistema... Python versión: {sys.version.split()[0]}")
    
    ejecutando = True

    while ejecutando:
        menu.mostrar_menu_principal()
        opcion = menu.obtener_opcion()

        # Control de Flujo (EPIC 4 - TASK-010)
        if opcion == '1':
            print("\n🚧 [TODO] Funcionalidad 'Agregar' en desarrollo...")
        
        elif opcion == '2':
            # Visualización rápida para verificar estructura (TASK-006)
            print(f"\n📦 Listado actual ({len(gestion_datos.productos)} productos):")
            for prod in gestion_datos.productos:
                print(prod)
        
        elif opcion == '3':
            print("\n🚧 [TODO] Funcionalidad 'Buscar' en desarrollo...")
        
        elif opcion == '4':
            print("\n🚧 [TODO] Funcionalidad 'Actualizar' en desarrollo...")
        
        elif opcion == '5':
            print("\n🚧 [TODO] Funcionalidad 'Eliminar' en desarrollo...")
            
        elif opcion == '6':
            gestion_datos.inicializar_datos_prueba()
            
        elif opcion == '7':
            print("\n👋 Gracias por usar Alke PIM. ¡Hasta pronto!")
            ejecutando = False
            
        else:
            print("\n⚠️ Opción no válida. Intente nuevamente.")

# Buenas prácticas: Ejecutar solo si es el script principal
if __name__ == "__main__":
    main()