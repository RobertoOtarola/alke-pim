"""
Archivo Principal (Entry Point)
-------------------------------
Punto de entrada del sistema Alke PIM.
"""
import sys
from modulos import menu, gestion_datos, datos_basicos # <--- Nuevo import

def main():
    print(f"Iniciando sistema... Python versión: {sys.version.split()[0]}")
    ejecutando = True

    while ejecutando:
        menu.mostrar_menu_principal()
        opcion = menu.obtener_opcion()

        if opcion == '1':
            print("\n--- 🆕 AGREGAR NUEVO PRODUCTO ---")
            # 1. Captura de datos (TASK-004)
            nombre = datos_basicos.solicitar_nombre()
            precio = datos_basicos.solicitar_precio()
            cantidad = datos_basicos.solicitar_cantidad()
            categoria = datos_basicos.solicitar_categoria()

            # 2. Guardado de datos (TASK-006)
            gestion_datos.crear_producto(nombre, precio, cantidad, categoria)
            print(f"\n✅ Producto '{nombre}' agregado exitosamente.")

        elif opcion == '2':
            # Listado simple actualizado
            print(f"\n📦 Listado actual ({len(gestion_datos.productos)} productos):")
            for prod in gestion_datos.productos:
                # Uso de f-strings para formato legible
                print(f"ID: {prod['id']} | {prod['nombre']} | ${prod['precio']} | Stock: {prod['cantidad']} | Total: ${prod['valor_inventario']}")
        
        elif opcion == '3':
             print("\n🚧 [TODO] Funcionalidad 'Buscar' en desarrollo...")
        # ... resto del código igual ...
        elif opcion == '7':
            print("\n👋 Gracias por usar Alke PIM.")
            ejecutando = False
        else:
             if opcion not in ['1', '2', '3', '4', '5', '6', '7']: # Pequeña validación extra
                print("\n⚠️ Opción no válida.")

if __name__ == "__main__":
    main()