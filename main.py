"""
Archivo Principal (Entry Point)
-------------------------------
Sistema Alke PIM actualizado con estructuras avanzadas.
"""
import sys
from modulos import menu, gestion_datos, datos_basicos

def mostrar_tabla(lista_productos):
    """Función auxiliar para no repetir código de impresión."""
    print("-" * 100)
    print(f"{'ID':<4} | {'Nombre':<18} | {'Precio':<9} | {'Cat.':<12} | {'Prov.':<10} | {'Stock'}")
    print("-" * 100)
    for prod in lista_productos:
        # Acceso a diccionario anidado con .get() para evitar errores
        nom_prov = prod.get("proveedor", {}).get("nombre", "N/A")
        print(f"{prod['id']:<4} | {prod['nombre']:<18} | ${prod['precio']:<8} | {prod['categoria']:<12} | {nom_prov:<10} | {prod['cantidad']}")
    print("-" * 100)

def main():
    print(f"Iniciando Alke PIM... (v2.0 Estructuras Avanzadas)")
    gestion_datos.inicializar_datos_prueba()
    
    ejecutando = True

    while ejecutando:
        menu.mostrar_menu_principal()
        # Agregamos una opción visual extra manualmente
        print("8. 📊 Reportes Avanzados (Ordenar/Filtrar)")
        print("-" * 50)
        
        opcion = menu.obtener_opcion()

        if opcion == '1':
            continuar = True
            while continuar:
                print("\n--- 🆕 ALTA DE PRODUCTO ---")
                nombre = datos_basicos.solicitar_nombre()
                precio = datos_basicos.solicitar_precio()
                cantidad = datos_basicos.solicitar_cantidad()
                
                # Nuevas solicitudes (Tupla y Diccionario Anidado)
                categoria = datos_basicos.solicitar_categoria()
                proveedor = datos_basicos.solicitar_datos_proveedor()

                exito = gestion_datos.crear_producto(nombre, precio, cantidad, categoria, proveedor)
                if exito:
                    print(f"✅ Producto guardado.")
                
                continuar = datos_basicos.confirmar_accion("\n¿Agregar otro?")

        elif opcion == '2':
            print(f"\n📦 Listado General:")
            mostrar_tabla(gestion_datos.productos)

        elif opcion == '3':
            id_b = datos_basicos.solicitar_id()
            prod = gestion_datos.buscar_producto_por_id(id_b)
            if prod:
                print(f"\n🔎 Detalle: {prod['nombre']}")
                print(f"   Categoría: {prod['categoria']}")
                print(f"   Proveedor: {prod['proveedor']['nombre']} ({prod['proveedor']['pais']})")
            else:
                print("❌ No encontrado.")

        elif opcion == '4': # Actualizar Stock
            id_b = datos_basicos.solicitar_id()
            if gestion_datos.buscar_producto_por_id(id_b):
                n_cant = datos_basicos.solicitar_cantidad()
                gestion_datos.actualizar_stock(id_b, n_cant)
                print("✅ Actualizado.")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == '5': # Eliminar
            id_b = datos_basicos.solicitar_id()
            if datos_basicos.confirmar_accion("¿Eliminar?"):
                if gestion_datos.eliminar_producto(id_b): print("✅ Eliminado.")
                else: print("❌ No existe.")

        elif opcion == '6':
            gestion_datos.inicializar_datos_prueba()

        elif opcion == '8':
            # TASK-017: Demostración de métodos de colecciones
            print("\n📊 --- REPORTES AVANZADOS ---")
            print("1. Ver ordenados por precio (Mayor a menor)")
            print("2. Filtrar por categoría")
            sub_op = input("👉 Elija reporte: ")
            
            if sub_op == '1':
                ordenados = gestion_datos.obtener_productos_ordenados_precio()
                mostrar_tabla(ordenados)
            elif sub_op == '2':
                cat = datos_basicos.solicitar_categoria() # Reusamos la validación de tupla
                filtrados = gestion_datos.filtrar_por_categoria(cat)
                if filtrados:
                    mostrar_tabla(filtrados)
                else:
                    print("⚠️  No hay productos en esta categoría.")

        elif opcion == '7':
            ejecutando = False
            print("👋 Bye!")

if __name__ == "__main__":
    main()