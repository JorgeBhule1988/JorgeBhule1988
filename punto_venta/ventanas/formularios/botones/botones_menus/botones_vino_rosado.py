from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BotonesVinoRosado:

    def coparosado1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Rosado', '165', subtotal))
            self.ecantidad.delete(0, END)


    def bonina1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bonina Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def raza1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Raza Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def porta1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Porta 6 Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def rincones1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 580
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rincones Rose', '580', subtotal))
            self.ecantidad.delete(0, END)

    
    def espumosopaxx1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Espumoso Paax Dulce', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def espumosopaxx_2_1(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Espumoso Paax Brut Rose', '800', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

                cantidad = IntVar()
                lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
                lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

                self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
                self.ecantidad = Entry(v, textvariable = cantidad)
                self.emesa = ttk.Combobox(v, value = lista_mesas)
                self.emesero = ttk.Combobox(v, value = lista_meseros)
