from tkinter import *
from tkinter import ttk
import mysql.connector
from persistencia.repositorio_conexion import RepositorioConexionSQLite

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
    
    def agregar_producto(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * float(self.eprecio_unit.get())
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = (str(self.enombre_product.get()), str(self.eprecio_unit.get()), subtotal))
            self.ecantidad.delete(0, END)
            self.enombre_product.delete(0, END)
            self.eprecio_unit.delete(0, END)


    def limpiar(self):
        for i in self.inventario.get_children():
            self.inventario.delete(i)

    def seleccionar(self, click):
        
        item = self.inventario.identify('item', click.x, click.y)
        self.nomb.set(self.inventario.item(item, 'text'))
        self.canti.set(self.inventario.item(item, 'value')[0])

    def __init__(self, v):
        
        cantidad = IntVar()
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
        lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

        self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
        self.ecantidad = Entry(v, textvariable = cantidad)
        self.emesa = ttk.Combobox(v, value = lista_mesas)
        self.emesero = ttk.Combobox(v, value = lista_meseros)

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

        self.agregarproducto = ttk.Button(v, text = 'Agregar', width = 15, command = self.agregar_producto)
        self.agregarproducto.place(x = 0, y = 200)
        self.actualizar = ttk.Button(v, text = 'Actualizar', width = 90, command = self.consultar)
        self.actualizar.place(x = 300, y = 0)
