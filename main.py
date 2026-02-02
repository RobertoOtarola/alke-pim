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
            print(f"\n📦 Listado actual ({len(gestion_datos.productos)} productos):")
            print("-" * 100)
            # Cabecera simulada
            print(f"{'ID':<4} | {'Nombre':<20} | {'Precio':<10} | {'Nivel':<10} | {'Stock':<6} | {'Estado'}")
            print("-" * 100)
            
            for prod in gestion_datos.productos:
                print(f"{prod['id']:<4} | {prod['nombre']:<20} | ${prod['precio']:<9} | {prod['nivel_precio']:<10} | {prod['cantidad']:<6} | {prod['estado_stock']}")
            print("-" * 100)
        
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