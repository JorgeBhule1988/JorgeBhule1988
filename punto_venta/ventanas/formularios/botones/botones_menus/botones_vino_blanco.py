from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BotonesVinoBlanco:

    def copablanco1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Blanco', '165', subtotal))
            self.ecantidad.delete(0, END)
    

    def cavacordova1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 920
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cava Cordova Chardonnay', '920', subtotal))
            self.ecantidad.delete(0, END)
    

    def anniespecial1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 870
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Anni Especial Sauvignon Blanc', '870', subtotal))
            self.ecantidad.delete(0, END)

    
    def islanegra1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Isla Negra Sauvignon Blanc', '800', subtotal))
            self.ecantidad.delete(0, END)
    
    def tantehue1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 750
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tantehue Chardonnay', '750', subtotal))
            self.ecantidad.delete(0, END)

    
    def micheltorino1(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 850
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Michel Torino Torrentes', '850', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

                cantidad = IntVar()
                lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
                lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

                self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
                self.ecantidad = Entry(v, textvariable = cantidad)
                self.emesa = ttk.Combobox(v, value = lista_mesas)
                self.emesero = ttk.Combobox(v, value = lista_meseros)
