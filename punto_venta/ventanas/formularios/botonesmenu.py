from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from formularios.repositorio_conexion import RepositorioConexionSQLite
import mysql.connector


class BonotonesMenu(RepositorioConexionSQLite):

    def botonrodizio(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 560
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio', '600', subtotal))
            self.ecantidad.delete(0, END)

        
    def botonrodiziol(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 400
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local', '400', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodiziom(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 280
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Menor', '300', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodizioml(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local Menor', '200', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodiziotg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 525
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Togo', '525', subtotal))
            self.ecantidad.delete(0, END)

    def botonpicana(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña', '950', subtotal))
            self.ecantidad.delete(0, END)


    def botonpicanatg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 695
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña TG', '695', subtotal))
            self.ecantidad.delete(0, END)


    def botontomahack(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('TOMA HACK', '1950', subtotal))
            self.ecantidad.delete(0, END)


    def botonburguer(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa', '220', subtotal))
            self.ecantidad.delete(0, END)
    

    def rodiziopassport(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 0
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Passport', '0', subtotal))
            self.ecantidad.delete(0, END)


    def rodiziocortesia(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 0
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Cortesia', '0', subtotal))
            self.ecantidad.delete(0, END)


    def botonburguertg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa Togo', '120', subtotal))
            self.ecantidad.delete(0, END)


    def botonaguap(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Agua Panna', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botontopoc(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Topo Chico', '95', subtotal))
            self.ecantidad.delete(0, END)


    def botonlimonada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 50
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Limonada', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botonnaranjada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 50
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Naranjada', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botoncoca(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola', '40', subtotal))
            self.ecantidad.delete(0, END)

    
    def botoncocad(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola Dieta', '40', subtotal))
            self.ecantidad.delete(0, END)

        
    def botonsprite(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sprite', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonfresca(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Fresca', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonmundet(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mundet', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonpinada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piñada', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botonmojitov(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito S/A', '75', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonpituv(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña S/A', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botonpacifico(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonultra(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Ultra', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botonpacificol(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Ligth', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botoncorona(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Corona', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonvictoria(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Victoria', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonartesanal(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cerveza Artesanal', '95', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonegramodelo(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 85
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negra Modelos', '85', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonmojito(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito', '160', subtotal))
            self.ecantidad.delete(0, END)


    def botonmezcalitaj(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Jamaica', '165', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonmezcalitam(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '165', subtotal))
            self.ecantidad.delete(0, END)


    def botoncaipirina(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña', '180', subtotal))
            self.ecantidad.delete(0, END)


    def botoncopadevino(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Cal y Canto', '165', subtotal))
            self.ecantidad.delete(0, END)


    def bsanmartino(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('San Martino', '800', subtotal))
            self.ecantidad.delete(0, END)
        
    
    def mojitotinto(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito Vino Tinto', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def mojitosabores(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito Sabores', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def guanabanagin(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)


    def martinicoffe(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coffe Martini', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritarodizio(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margarita Rodizio', '180', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritamango(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Mango', '185', subtotal))
            self.ecantidad.delete(0, END)
    
    def margaritaguanabana(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)

        
    def margaritamaracuya(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritatradicional(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritacadillac(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 265
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Cadillac', '265', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitatradicional(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita', '180', subtotal))
            self.ecantidad.delete(0, END)


    def mezcalitamango(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Mango', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitamaracuya(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitaguanabana(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)


    def pitumango(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Mango', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def pitumaracuya(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)


    def pituguanabana(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def negroni(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negroni', '220', subtotal))
            self.ecantidad.delete(0, END)

    
    def gintonic(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gin Tonic', '220', subtotal))
            self.ecantidad.delete(0, END)

    
    def oldfashion(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Old Fashion', '220', subtotal))
            self.ecantidad.delete(0, END)


    def clericottinto(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 145
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot', '145', subtotal))
            self.ecantidad.delete(0, END)

    
    def clericotrosado(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot Rosado', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def clericotblueberry(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot Blue Berry', '185', subtotal))
            self.ecantidad.delete(0, END)


    def casamadero_3v(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Madero 3v BLEND', '1250', subtotal))
            self.ecantidad.delete(0, END)

    
    def casamadero(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Madero CAB/SAU', '1250', subtotal))
            self.ecantidad.delete(0, END)
    

    def piccolo(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1080
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piccolo BLEND', '1080', subtotal))
            self.ecantidad.delete(0, END)

    
    def criosblend(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 980
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS BLEND', '840', subtotal))
            self.ecantidad.delete(0, END)
        

    def criosmalbec(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS MALBEC', '1100', subtotal))
            self.ecantidad.delete(0, END)

    
    def crioscab(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1020
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS CAB/SAU', '1020', subtotal))
            self.ecantidad.delete(0, END)

    
    def marcobonfante(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 960
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Marco Bonfante BARBERA', '960', subtotal))
            self.ecantidad.delete(0, END)

    
    def neroavola(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1050
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Nero de Avola', '1050', subtotal))
            self.ecantidad.delete(0, END)
    

    def mongrasssyr(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1000
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass CAB/SYR', '1000', subtotal))
            self.ecantidad.delete(0, END)

    
    def mongrassblend(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass Premium BLEND', '1450', subtotal))
            self.ecantidad.delete(0, END)

    
    def mongrasscab(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1060
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass CAB/SAU', '1060', subtotal))
            self.ecantidad.delete(0, END)


    def decoy(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1600
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('DECOY PINOT NOIR', '1600', subtotal))
            self.ecantidad.delete(0, END)

    
    def lomita(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1020
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('La Lomita CAB/SAU', '1020', subtotal))
            self.ecantidad.delete(0, END)

    
    def castacardon(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casta Cardon BLEND', '1100', subtotal))
            self.ecantidad.delete(0, END)

    
    def harasdepirque(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1040
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Haras de Pirque BLEND', '1040', subtotal))
            self.ecantidad.delete(0, END)


    def harasgran(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Haras de Pirque Gran Reserva CAB/SAU', '1140', subtotal))
            self.ecantidad.delete(0, END)

    
    def minimalista(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 870
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Minimalista MALBEC', '870', subtotal))
            self.ecantidad.delete(0, END)

    
    def domino(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 980
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('DOMINO BLEND', '980', subtotal))
            self.ecantidad.delete(0, END)

    
    def abbout(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1030
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('ABBOUT PINOT NOIR', '1030', subtotal))
            self.ecantidad.delete(0, END)

    
    def bellaretta(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 830
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bellaretta CAB/SAU', '830', subtotal))
            self.ecantidad.delete(0, END)


    def carlidge(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Carlidge & Brown CAB', '1200', subtotal))
            self.ecantidad.delete(0, END)

    
    def botagua(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bot de Agua', '40', subtotal))
            self.ecantidad.delete(0, END)

    
    def gnarlyhead(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gnarly Head CAB', '1200', subtotal))
            self.ecantidad.delete(0, END)

    
    def santacristina(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1350
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Santa Cristina CHIANTI SUPERIORE', '1350', subtotal))
            self.ecantidad.delete(0, END)

    
    def colezionemolte(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Colezione MOLTEPULCIANO', '700', subtotal))
            self.ecantidad.delete(0, END)
    

    def caracter(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caracter MALBEC', '700', subtotal))
            self.ecantidad.delete(0, END)


    def tierraadentro(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tierra Adentro BLEND', '1100', subtotal))
            self.ecantidad.delete(0, END)


    def misassou(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mirassou CAB/SAU', '700', subtotal))
            self.ecantidad.delete(0, END)
    

    def kruguer(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Kruguer CAB/TEM', '1450', subtotal))
            self.ecantidad.delete(0, END)

    
    def care(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1150
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CARE', '1150', subtotal))
            self.ecantidad.delete(0, END)

    
    def cetto(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 850
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Luis Cetto MERLOT', '850', subtotal))
            self.ecantidad.delete(0, END)

    
    def calycanto(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 795
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cal y Canto', '795', subtotal))
            self.ecantidad.delete(0, END)

    
    def cigliano(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cigliano CHIANTI CLASICO', '1200', subtotal))
            self.ecantidad.delete(0, END)


    def coparosado(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Rosado', '165', subtotal))
            self.ecantidad.delete(0, END)


    def copablanco(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Blanco', '165', subtotal))
            self.ecantidad.delete(0, END)
    

    def cavacordova(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 920
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cava Cordova Chardonnay', '920', subtotal))
            self.ecantidad.delete(0, END)
    

    def anniespecial(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 870
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Anni Especial Sauvignon Blanc', '870', subtotal))
            self.ecantidad.delete(0, END)

    
    def islanegra(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Isla Negra Sauvignon Blanc', '800', subtotal))
            self.ecantidad.delete(0, END)
    
    def tantehue(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 750
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tantehue Chardonnay', '750', subtotal))
            self.ecantidad.delete(0, END)

    
    def micheltorino(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 850
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Michel Torino Torrentes', '850', subtotal))
            self.ecantidad.delete(0, END)
    

    def bonina(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bonina Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def raza(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Raza Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def porta(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Porta 6 Portugal', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def rincones(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 580
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rincones Rose', '580', subtotal))
            self.ecantidad.delete(0, END)

    
    def espumosopaxx(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Espumoso Paax Dulce', '800', subtotal))
            self.ecantidad.delete(0, END)

    
    def espumosopaxx_2(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Espumoso Paax Brut Rose', '800', subtotal))
            self.ecantidad.delete(0, END)


    def gavilan_reyes(self):
            if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
                messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
            else:
                subtotal = float(self.ecantidad.get()) * 185
                self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gavilan Reyes', '185', subtotal))
                self.ecantidad.delete(0, END)

    
    def sangria(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 110
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sangria', '110', subtotal))
            self.ecantidad.delete(0, END)

    
    def pina_colada(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piña Colada', '140', subtotal))
            self.ecantidad.delete(0, END)


    def limpiar(self):
        for i in self.captura.get_children():
            self.captura.delete(i)
    
    #Botones de mesas
    def mesa1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))         
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa5(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '5')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '5'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa6(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '6')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '6'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa7(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '7')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '7'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    
    def mesa8(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '8')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '8'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa9(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '9')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '9'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa10(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '10')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '10'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa11(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '11')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '11'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa12(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '12')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '12'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa13(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '13')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '13'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac2(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava2')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava2'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac4(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava4')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava4'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()


    def __init__(self, v):

        cantidad = IntVar()
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
        lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

        self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
        self.ecantidad = Entry(v, textvariable = cantidad)
        self.emesa = ttk.Combobox(v, value = lista_mesas)
        self.emesero = ttk.Combobox(v, value = lista_meseros)
