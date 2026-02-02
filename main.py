"""
Archivo Principal (Entry Point)
-------------------------------
Sistema Alke PIM v3.0 (Modularizado)
"""
import sys
# TASK-022: Importación limpia de módulos
from modulos import menu, gestion_datos, datos_basicos, funciones_utiles

def mostrar_tabla(lista_productos):
    """Muestra tabla formateada usando utilidades."""
    print("-" * 115)
    print(f"{'ID':<4} | {'Nombre':<18} | {'Precio Unit.':<12} | {'Cat.':<12} | {'Prov.':<10} | {'Stock':<6} | {'Total'}")
    print("-" * 115)
    
    for prod in lista_productos:
        # TASK-019: Uso de función de formateo
        precio_fmt = funciones_utiles.formatear_precio(prod['precio'])
        total_fmt = funciones_utiles.formatear_precio(prod['valor_inventario'])
        prov = prod.get("proveedor", {}).get("nombre", "N/A")
        
        print(f"{prod['id']:<4} | {prod['nombre']:<18} | {precio_fmt:<12} | {prod['categoria']:<12} | {prov:<10} | {prod['cantidad']:<6} | {total_fmt}")
    print("-" * 115)

def main():
    print(f"Iniciando Alke PIM... (v3.0 Modular + Recursividad)")
    gestion_datos.inicializar_datos_prueba()
    
    ejecutando = True
    while ejecutando:
        menu.mostrar_menu_principal()
        print("8. 📊 Reportes y Utilidades")
        print("-" * 50)
        
        opcion = menu.obtener_opcion()

        if opcion == '1':
            n = datos_basicos.solicitar_nombre()
            p = datos_basicos.solicitar_precio()
            c = datos_basicos.solicitar_cantidad()
            cat = datos_basicos.solicitar_categoria()
            prov = datos_basicos.solicitar_datos_proveedor()
            if gestion_datos.crear_producto(n, p, c, cat, prov):
                print("✅ Guardado.")

        elif opcion == '2':
            mostrar_tabla(gestion_datos.productos)

        elif opcion == '3':
            id_b = datos_basicos.solicitar_id()
            prod = gestion_datos.buscar_producto_por_id(id_b)
            if prod:
                print(f"\n🔎 --- FICHA PRODUCTO ---")
                print(f"Nombre: {prod['nombre']}")
                print(f"Precio: {funciones_utiles.formatear_precio(prod['precio'])}")
                print(f"Stock:  {prod['cantidad']} ({prod['estado_stock']})")
            else:
                print("❌ No encontrado.")

        elif opcion == '4':
            id_b = datos_basicos.solicitar_id()
            if gestion_datos.buscar_producto_por_id(id_b):
                c = datos_basicos.solicitar_cantidad()
                gestion_datos.actualizar_stock(id_b, c)
                print("✅ Stock actualizado.")
            else:
                print("❌ No existe.")

        elif opcion == '5':
            id_b = datos_basicos.solicitar_id()
            if datos_basicos.confirmar_accion("¿Eliminar?"):
                gestion_datos.eliminar_producto(id_b)
                print("🗑️ Eliminado.")

        elif opcion == '6':
            gestion_datos.inicializar_datos_prueba()

        elif opcion == '8':
            print("\n📊 --- REPORTES ---")
            print("1. Valor Total del Inventario (Cálculo Recursivo)")
            print("2. Productos ordenados por precio")
            print("3. Filtrar por categoría")
            
            sub = input("👉 Opción: ")
            
            if sub == '1':
                # TASK-020: Prueba de la función recursiva
                total = gestion_datos.obtener_total_inventario()
                print(f"\n💰 VALOR TOTAL DEL INVENTARIO: {funciones_utiles.formatear_precio(total)}")
                print("(Cálculo realizado mediante algoritmo recursivo)")
                
            elif sub == '2':
                ordenados = gestion_datos.obtener_productos_ordenados_precio()
                mostrar_tabla(ordenados)
                
            elif sub == '3':
                cat = datos_basicos.solicitar_categoria()
                filtrados = gestion_datos.filtrar_por_categoria(cat)
                mostrar_tabla(filtrados)

        elif opcion == '7':
            ejecutando = False
            print("👋 Bye!")

if __name__ == "__main__":
    main()
    