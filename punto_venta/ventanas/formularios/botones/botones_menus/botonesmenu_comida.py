from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BonotonesMenuComida:

    def rodizio(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 600
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio', '600', subtotal))
            self.ecantidad.delete(0, END)


    def rodiziomenor(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 300
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Menor', '300', subtotal))
            self.ecantidad.delete(0, END)


    def rodiziolocal(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 400
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local', '400', subtotal))
            self.ecantidad.delete(0, END)


    def rodiziolocalmenor(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local Menor', '200', subtotal))
            self.ecantidad.delete(0, END)


    def rodizio20(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 320
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio 20% Desc', '320', subtotal))
            self.ecantidad.delete(0, END)


    def rodiziotogo(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 550
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Togo', '550', subtotal))
            self.ecantidad.delete(0, END)


    def picana(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña', '950', subtotal))
            self.ecantidad.delete(0, END)
    
    def picanatogo(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 695
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña TG', '695', subtotal))
            self.ecantidad.delete(0, END)


    def tomahack(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1650
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('TOMA HACK', '1650', subtotal))
            self.ecantidad.delete(0, END)


    def burguerpicana(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa', '220', subtotal))
            self.ecantidad.delete(0, END)


    def burguerpicatogo(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa Togo', '120', subtotal))
            self.ecantidad.delete(0, END)


    def rodipass(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 0
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Passport', '0', subtotal))
            self.ecantidad.delete(0, END)


    def rodicorte(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 0
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Cortesia', '0', subtotal))
            self.ecantidad.delete(0, END)
    
    
    def postre_cumple(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Postre Especial', '95', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
