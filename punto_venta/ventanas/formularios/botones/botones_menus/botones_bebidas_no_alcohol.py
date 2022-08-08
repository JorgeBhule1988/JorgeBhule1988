from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BotonesBebidas:

    def agua(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Agua Panna', '75', subtotal))
            self.ecantidad.delete(0, END)


    def topochico(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Topo Chico', '95', subtotal))
            self.ecantidad.delete(0, END)


    def limonada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Limonada', '60', subtotal))
            self.ecantidad.delete(0, END)
    

    def naranjada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Naranjada', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def cocacola(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola', '40', subtotal))
            self.ecantidad.delete(0, END)

    
    def cocaligth(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola Ligth', '40', subtotal))
            self.ecantidad.delete(0, END)
    

    def sprite(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sprite', '40', subtotal))
            self.ecantidad.delete(0, END)

    
    def fresca(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Fresca', '40', subtotal))
            self.ecantidad.delete(0, END)


    def mundet(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mundet', '40', subtotal))
            self.ecantidad.delete(0, END)


    def pinada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piñada', '75', subtotal))
            self.ecantidad.delete(0, END)


    def mojitov(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito S/A', '75', subtotal))
            self.ecantidad.delete(0, END)

    
    def pituv(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña S/A', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botaguanat(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bot de Agua', '40', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
