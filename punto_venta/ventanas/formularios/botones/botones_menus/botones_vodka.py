from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BotonesVodka:

    def titos1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Titos', '140', subtotal))
            self.ecantidad.delete(0, END)
    

    def adsolut1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Adsolut', '140', subtotal))
            self.ecantidad.delete(0, END)


    def citron1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Adsolut Citron', '120', subtotal))
            self.ecantidad.delete(0, END)
    

    def pear1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Adsolut Pear', '120', subtotal))
            self.ecantidad.delete(0, END)

    
    def mandarin1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Adsolut Mandarin', '120', subtotal))
            self.ecantidad.delete(0, END)

    
    def ketelone1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 130
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Ketel One', '130', subtotal))
            self.ecantidad.delete(0, END)
    

    def greygoose1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Grey Goose', '140', subtotal))
            self.ecantidad.delete(0, END)


    def smirnoff1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Smirnoff', '120', subtotal))
            self.ecantidad.delete(0, END)

    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
