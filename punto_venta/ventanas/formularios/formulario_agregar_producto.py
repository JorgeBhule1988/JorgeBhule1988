from tkinter import *
from tkinter import ttk, messagebox
from dominio.tickets import Producto
import dominio.controlador.controlador_flujo as controlador

class FormularioAgregarProducto:

    def alta(self):

        p = Producto()
        p.nombre = self.enombre_producto.get()
        p.categoria = self.ecategoria.get()
        p.precio_unitario = self.eprecio_unit.get()
        p.stock = self.estock.get()
        p.existencia = self.eexistencias.get()

        afectados =controlador.insertar_producto(p)
        if(afectados == 0):
            messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados} registro", title="Salvar")
        self.limpiar()
    

    def limpiar(self):
        
        self.enombre_producto.delete(0, END)
        self.ecategoria.delete(0, END)
        self.eprecio_unit.delete(0, END)
        self.estock.delete(0, END)
        self.eexistencias.delete(0, END)


    def __init__(self, v):

        productname = []
        category = ['COMIDA', 'BEBIDA NO ALCOHOL', 'CERVEZA', 'COCKTELERIA', 'VINO TINTO',
                    'VINO BLANCO', 'VINO ROSADO', 'VINO ESPUMOSO', 'RON', 'VODKA', 'WHISKY',
                    'TEQUILA', 'MEZCAL', 'LICORES', 'OTROS']
        existens = ['SI', 'NO']

        self.lname_product = Label(v, text = 'Nombre del Producto', font = ('Arial', 12, 'bold'))
        self.lcategory = Label(v, text = 'Categoria', font = ('Arial', 12, 'bold'))
        self.lprice_unit = Label(v, text = 'Precio Unitario', font = ('Arial', 12, 'bold'))
        self.lstock = Label(v, text = 'Stock', font = ('Arial', 12, 'bold'))
        self.lexitencias = Label(v, text = 'Existencia', font = ('Arial', 12, 'bold'))

        self.enombre_producto = ttk.Combobox(v, values = productname, width = 12)
        self.ecategoria = ttk.Combobox(v, values = category, width = 12)
        self.eprecio_unit = Entry(v, width = 15)
        self.estock = Entry(v, width = 15)
        self.eexistencias = ttk.Combobox(v, values = existens, width = 12)

        self.lname_product.place(x = 0, y = 40)
        self.lcategory.place(x = 0, y = 80)
        self.lprice_unit.place(x = 0, y = 120)
        self.lstock.place(x = 0, y = 160)
        self.lexitencias.place(x = 0, y = 200)
        self.enombre_producto.place(x = 200, y = 40)
        self.ecategoria.place(x = 200, y = 80)
        self.eprecio_unit.place(x = 200, y = 120)
        self.estock.place(x = 200, y = 160)
        self.eexistencias.place(x = 200, y = 200)

        self.agregar_producto = ttk.Button(v, text = 'Agregar Producto', width = 20, command = self.alta)
        self.agregar_producto.place(x = 0, y = 240)
