# modeloInventario.py
import pyodbc

class ModeloInventario:
    def __init__(self):
        self.conexion = pyodbc.connect(
            'DRIVER={MySQL ODBC 9.3 Unicode Driver};SERVER=localhost;PORT=3306;DATABASE=control_inventario;UID=root;PWD=Alex032020'
)
        self.cursor = self.conexion.cursor()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def agregar_producto(self, nombre, cantidad, precio):
        self.cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        self.conexion.commit()

    def actualizar_producto(self, id_producto, cantidad, precio):
        self.cursor.execute("UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?", (cantidad, precio, id_producto))
        self.conexion.commit()

    def eliminar_producto(self, id_producto):
        self.cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
