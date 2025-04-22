# vista.py

class VistaInventario:
    @staticmethod
    def mostrar_menu():
        print("\n1. Ver productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_productos(productos):
        print("\n--- Productos en inventario ---")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: ${producto[3]}")
        print("-------------------------------")

    @staticmethod
    def solicitar_datos_producto():
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        return nombre, cantidad, precio

    @staticmethod
    def solicitar_id_producto():
        return int(input("Ingrese el ID del producto: "))

    @staticmethod
    def solicitar_datos_actualizacion():
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        return cantidad, precio

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
