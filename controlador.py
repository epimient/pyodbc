# controlador.py
from modelo import ModeloInventario
from vista import VistaInventario

class ControladorInventario:
    def __init__(self):
        self.modelo = ModeloInventario()
        self.vista = VistaInventario()

    def iniciar(self):
        opcion = ""
        while opcion != "5":
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                productos = self.modelo.obtener_productos()
                self.vista.mostrar_productos(productos)

            elif opcion == "2":
                nombre, cantidad, precio = self.vista.solicitar_datos_producto()
                self.modelo.agregar_producto(nombre, cantidad, precio)
                self.vista.mostrar_mensaje("Producto agregado exitosamente.")

            elif opcion == "3":
                id_producto = self.vista.solicitar_id_producto()
                cantidad, precio = self.vista.solicitar_datos_actualizacion()
                self.modelo.actualizar_producto(id_producto, cantidad, precio)
                self.vista.mostrar_mensaje("Producto actualizado exitosamente.")

            elif opcion == "4":
                id_producto = self.vista.solicitar_id_producto()
                self.modelo.eliminar_producto(id_producto)
                self.vista.mostrar_mensaje("Producto eliminado exitosamente.")

        self.modelo.cerrar_conexion()
