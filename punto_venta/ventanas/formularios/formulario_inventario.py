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
               self.inventario.insert('', END, text = row[0], values = (row[1], row[2], row[3]))

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    def limpiar(self):
        for i in self.inventario.get_children():
            self.inventario.delete(i)

    def seleccionar(self, click):
        
        item = self.inventario.identify('item', click.x, click.y)
        self.nomb.set(self.inventario.item(item, 'text'))
        self.canti.set(self.inventario.item(item, 'value')[0])

    def __init__(self, v):
        
        self.inventario = ttk.Treeview(v, height=11, columns=('#0', '#1', '#2'))
        self.inventario.column('#0', width = 200)
        self.inventario.heading('#0', text = 'Producto', anchor=CENTER)
        self.inventario.column('#1', width = 70)
        self.inventario.heading('#1', text = 'Precio Unit', anchor=CENTER)
        self.inventario.column('#2', width = 50)
        self.inventario.heading('#2', text = 'Cant', anchor=CENTER)
        self.inventario.column('#3', width = 80)
        self.inventario.heading('#3', text = 'Existencia', anchor=CENTER)
        self.inventario.place(x = 400, y = 40)
        self.inventario.bind('<Double-1>', self.seleccionar)

        deslizarv = ttk.Scrollbar(v, orient = 'vertical', command = self.inventario.yview)
        deslizarv.place(x = 800, y = 40, relheight = 0.8)
        deslizarv.config(command = self.inventario.yview)
        self.inventario.configure(yscrollcommand = deslizarv.set)

        self.nomb = StringVar()
        self.canti = IntVar()

        self.lname_product = Label(v, text = 'Nombre del Producto', font = ('Arial', 12, 'bold'), bg = 'orange')
        self.lprice_unit = Label(v, text = 'Precio Unitario', font = ('Arial', 12, 'bold'), bg = 'orange')
        self.enombre_product = Entry(v, width = 15, textvariable = self.nomb)
        self.eprecio_unit = Entry(v, width = 15, textvariable = self.canti)

        self.lname_product.place(x = 0, y = 40)
        self.lprice_unit.place(x = 0, y = 80)
        self.enombre_product.place(x = 200, y = 40)
        self.eprecio_unit.place(x = 200, y = 80)

        self.actualizar = ttk.Button(v, text = 'Actualizar', width = 90, command = self.consultar)
        self.actualizar.place(x = 300, y = 0)
