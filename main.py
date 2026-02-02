"""
Archivo Principal (Entry Point)
-------------------------------
Orquestador del sistema Alke PIM con CRUD completo.
"""
import sys
from modulos import menu, gestion_datos, datos_basicos

def main():
    print(f"Iniciando sistema... Python versión: {sys.version.split()[0]}")
    # Aseguramos datos de prueba al inicio para facilitar corrección
    gestion_datos.inicializar_datos_prueba()
    
    ejecutando = True

    while ejecutando:
        menu.mostrar_menu_principal()
        opcion = menu.obtener_opcion()

        # --- OPCIÓN 1: ALTA DE PRODUCTOS (TASK-011: Ingreso múltiple) ---
        if opcion == '1':
            continuar_agregando = True
            while continuar_agregando:
                print("\n--- 🆕 AGREGAR NUEVO PRODUCTO ---")
                nombre = datos_basicos.solicitar_nombre()
                precio = datos_basicos.solicitar_precio()
                cantidad = datos_basicos.solicitar_cantidad()
                categoria = datos_basicos.solicitar_categoria()

                gestion_datos.crear_producto(nombre, precio, cantidad, categoria)
                print(f"✅ Producto '{nombre}' guardado.")

                # Pregunta para continuar (Bucle)
                continuar_agregando = datos_basicos.confirmar_accion("\n¿Desea agregar otro producto?")

        # --- OPCIÓN 2: LISTAR ---
        elif opcion == '2':
            print(f"\n📦 Listado actual ({len(gestion_datos.productos)} productos):")
            print("-" * 105)
            print(f"{'ID':<4} | {'Nombre':<20} | {'Precio':<10} | {'Nivel':<10} | {'Stock':<6} | {'Estado'}")
            print("-" * 105)
            for prod in gestion_datos.productos:
                print(f"{prod['id']:<4} | {prod['nombre']:<20} | ${prod['precio']:<9} | {prod['nivel_precio']:<10} | {prod['cantidad']:<6} | {prod['estado_stock']}")
            print("-" * 105)

        # --- OPCIÓN 3: BUSCAR ---
        elif opcion == '3':
            print("\n--- 🔍 BUSCAR PRODUCTO ---")
            id_buscar = datos_basicos.solicitar_id()
            producto = gestion_datos.buscar_producto_por_id(id_buscar)
            
            if producto:
                print("\n✅ PRODUCTO ENCONTRADO:")
                print(producto) # Imprime el diccionario completo (podríamos formatearlo mejor)
            else:
                print("❌ No se encontró ningún producto con ese ID.")

        # --- OPCIÓN 4: ACTUALIZAR STOCK ---
        elif opcion == '4':
            print("\n--- 🔄 ACTUALIZAR STOCK ---")
            id_buscar = datos_basicos.solicitar_id()
            producto = gestion_datos.buscar_producto_por_id(id_buscar)

            if producto:
                print(f"Producto seleccionado: {producto['nombre']} | Stock actual: {producto['cantidad']}")
                nueva_cantidad = datos_basicos.solicitar_cantidad()
                
                gestion_datos.actualizar_stock(id_buscar, nueva_cantidad)
                print("✅ Stock actualizado correctamente.")
            else:
                print("❌ Producto no encontrado.")

        # --- OPCIÓN 5: ELIMINAR ---
        elif opcion == '5':
            print("\n--- 🗑️ ELIMINAR PRODUCTO ---")
            id_buscar = datos_basicos.solicitar_id()
            producto = gestion_datos.buscar_producto_por_id(id_buscar)

            if producto:
                print(f"Va a eliminar: {producto['nombre']}")
                if datos_basicos.confirmar_accion("¿Está seguro? Esta acción no se puede deshacer."):
                    gestion_datos.eliminar_producto(id_buscar)
                    print("✅ Producto eliminado.")
                else:
                    print("🚫 Operación cancelada.")
            else:
                print("❌ Producto no encontrado.")

        # --- OPCIONES EXTRAS ---
        elif opcion == '6':
            gestion_datos.inicializar_datos_prueba()
            
        elif opcion == '7':
            print("\n👋 Gracias por usar Alke PIM.")
            ejecutando = False
            
        else:
            print("\n⚠️ Opción no válida.")

if __name__ == "__main__":
    main()