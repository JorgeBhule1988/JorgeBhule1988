from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BotonesCervezas:

    def pacifico(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def ultra(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Ultra', '60', subtotal))
            self.ecantidad.delete(0, END)


    def pacificol(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Ligth', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def corona(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Corona', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def victoria(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Victoria', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def artesanal(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cerveza Artesanal', '95', subtotal))
            self.ecantidad.delete(0, END)

    
    def negramodelo(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 85
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negra Modelos', '85', subtotal))
            self.ecantidad.delete(0, END)

    
    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
