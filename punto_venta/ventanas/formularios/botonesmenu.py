from tkinter import *
from tkinter import ttk


class Formulariobotones():

    def botonrodizio(self):
        subtotal = float(self.ecantidad.get()) * 560
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio', '560', subtotal))
        self.ecantidad.delete(0, END)
    
    def botonrodiziol(self):
        subtotal = float(self.ecantidad.get()) * 400
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local', '400', subtotal))
        self.ecantidad.delete(0, END)


    def botonrodiziom(self):
        subtotal = float(self.ecantidad.get()) * 280
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Menor', '280', subtotal))
        self.ecantidad.delete(0, END)


    def botonrodizioml(self):
        subtotal = float(self.ecantidad.get()) * 200
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local Menor', '200', subtotal))
        self.ecantidad.delete(0, END)


    def botonrodiziotg(self):
        subtotal = float(self.ecantidad.get()) * 525
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Togo', '525', subtotal))
        self.ecantidad.delete(0, END)


    def botonpicana(self):
        subtotal = float(self.ecantidad.get()) * 950
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña', '950', subtotal))
        self.ecantidad.delete(0, END)


    def botonpicanatg(self):
        subtotal = float(self.ecantidad.get()) * 695
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña Togo', '695', subtotal))
        self.ecantidad.delete(0, END)


    def botontomahack(self):
        subtotal = float(self.ecantidad.get()) * 1850
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('TomaHack', '1850', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonburguer(self):
        subtotal = float(self.ecantidad.get()) * 220
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa', '220', subtotal))
        self.ecantidad.delete(0, END)


    def botonburguertg(self):
        subtotal = float(self.ecantidad.get()) * 120
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa Togo', '120', subtotal))
        self.ecantidad.delete(0, END)
    

    def botonaguap(self):
        subtotal = float(self.ecantidad.get()) * 75
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Agua Panna', '75', subtotal))
        self.ecantidad.delete(0, END)


    def botontopoc(self):
        subtotal = float(self.ecantidad.get()) * 95
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Topo Chico', '95', subtotal))
        self.ecantidad.delete(0, END)


    def botonlimonada(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Limonada', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botonnaranjada(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Naranjada', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botoncoca(self):
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola', '50', subtotal))
        self.ecantidad.delete(0, END)

    
    def botoncocad(self):
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola Dieta', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botonsprite(self):
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sprite', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botonfresca(self):
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Fresca', '50', subtotal))
        self.ecantidad.delete(0, END)
        
    def __init__(self, v):
        
        cant = StringVar()
        self.ecantidad = Entry(v, textvariable = cant)
        self.ecantidad.place()
        self.captura = ttk.Treeview(v, columns = ('#0', '#1', '#2', '#3'))
