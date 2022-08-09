from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BotonesMezcal:

    def cuatroconejo1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 160
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('400 Conejos', '160', subtotal))
            self.ecantidad.delete(0, END)
    

    def buensuceso1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Buen Suceso', '220', subtotal))
            self.ecantidad.delete(0, END)


    def aleron1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 190
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Aleron', '190', subtotal))
            self.ecantidad.delete(0, END)
    

    def mitre1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 160
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mitre', '160', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalcasa1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcal de la Casa', '120', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
