from tkinter import *
from tkinter import ttk
import mysql.connector
from persistencia.repositorio_conexion import RepositorioConexionSQLite

class FormularioInventario(RepositorioConexionSQLite):

    def consultar(self):
        self.limpiar()
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select nombre, precio_unitario, stock, existencia from tabla_producto"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[1], row[2], row[3]))

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    def limpiar(self):
        for i in self.captura.get_children():
            self.captura.delete(i)

    def __init__(self, v):

        self.captura = ttk.Treeview(v, height=11, columns=('#0', '#1', '#2'))
        self.captura.place(x = 0, y = 450)
        self.captura.column('#0', width = 200)
        self.captura.heading('#0', text = 'Producto', anchor=CENTER)
        self.captura.column('#1', width = 70)
        self.captura.heading('#1', text = 'Precio Unit', anchor=CENTER)
        self.captura.column('#2', width = 50)
        self.captura.heading('#2', text = 'Cant', anchor=CENTER)
        self.captura.column('#3', width = 80)
        self.captura.heading('#3', text = 'Existencia', anchor=CENTER)
        self.captura.place(x = 80, y = 40)

        self.actualizar = ttk.Button(v, text = 'Actualizar', width = 90, command = self.consultar)
        self.actualizar.place(x = 0, y = 0)
