from tkinter import *
from tkinter import ttk


class BonotonesMenu:

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
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña TG', '695', subtotal))
        self.ecantidad.delete(0, END)


    def botontomahack(self):
        subtotal = float(self.ecantidad.get()) * 1950
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('TOMA HACK', '1950', subtotal))
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
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Limonada', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botonnaranjada(self):
        subtotal = float(self.ecantidad.get()) * 50
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Naranjada', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botoncoca(self):
        subtotal = float(self.ecantidad.get()) * 40
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola', '50', subtotal))
        self.ecantidad.delete(0, END)

    
    def botoncocad(self):
        subtotal = float(self.ecantidad.get()) * 40
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola Dieta', '60', subtotal))
        self.ecantidad.delete(0, END)

        
    def botonsprite(self):
        subtotal = float(self.ecantidad.get()) * 40
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sprite', '40', subtotal))
        self.ecantidad.delete(0, END)


    def botonfresca(self):
        subtotal = float(self.ecantidad.get()) * 40
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Fresca', '40', subtotal))
        self.ecantidad.delete(0, END)


    def botonmundet(self):
        subtotal = float(self.ecantidad.get()) * 40
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mundet', '40', subtotal))
        self.ecantidad.delete(0, END)


    def botonpinada(self):
        subtotal = float(self.ecantidad.get()) * 75
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piñada', '75', subtotal))
        self.ecantidad.delete(0, END)


    def botonmojitov(self):
        subtotal = float(self.ecantidad.get()) * 75
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito S/A', '75', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonpituv(self):
        subtotal = float(self.ecantidad.get()) * 75
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña S/A', '75', subtotal))
        self.ecantidad.delete(0, END)


    def botonpacifico(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico', '60', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonpacificos(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Suave', '60', subtotal))
        self.ecantidad.delete(0, END)


    def botonpacificol(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Ligth', '60', subtotal))
        self.ecantidad.delete(0, END)

    
    def botoncorona(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Corona', '60', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonvictoria(self):
        subtotal = float(self.ecantidad.get()) * 60
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Victoria', '60', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonartesanal(self):
        subtotal = float(self.ecantidad.get()) * 95
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cerveza Artesanal', '95', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonegramodelo(self):
        subtotal = float(self.ecantidad.get()) * 85
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negra Modelos', '80', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonmojito(self):
        subtotal = float(self.ecantidad.get()) * 140
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito', '140', subtotal))
        self.ecantidad.delete(0, END)


    def botonmezcalitaj(self):
        subtotal = float(self.ecantidad.get()) * 165
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Jamaica', '165', subtotal))
        self.ecantidad.delete(0, END)

    
    def botonmezcalitam(self):
        subtotal = float(self.ecantidad.get()) * 165
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '165', subtotal))
        self.ecantidad.delete(0, END)


    def botoncaipirina(self):
        subtotal = float(self.ecantidad.get()) * 165
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña', '165', subtotal))
        self.ecantidad.delete(0, END)


    def botocasamadero(self):
        subtotal = float(self.ecantidad.get()) * 1250
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bot Vino Casa Madero', '1250', subtotal))
        self.ecantidad.delete(0, END)


    def botoncopadevino(self):
        subtotal = float(self.ecantidad.get()) * 185
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino', '185', subtotal))
        self.ecantidad.delete(0, END)


    def botoncavalrose(self):
        subtotal = float(self.ecantidad.get()) * 950
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cavall Rose', '950', subtotal))
        self.ecantidad.delete(0, END)
        
    def __init__(self, v):
        
        cant = StringVar()
        self.ecantidad = Entry(v, textvariable = cant)
        self.ecantidad.place()
        self.captura = ttk.Treeview(v, columns = ('#0', '#1', '#2', '#3'))
