from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BotonesVinoTinto:

    def copadevino(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino Cal y Canto', '165', subtotal))
            self.ecantidad.delete(0, END)


    def bsanmartino1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 800
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('San Martino', '800', subtotal))
            self.ecantidad.delete(0, END)


    def casamadero_3v1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Madero 3v BLEND', '1250', subtotal))
            self.ecantidad.delete(0, END)

    
    def casamadero1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Madero CAB/SAU', '1250', subtotal))
            self.ecantidad.delete(0, END)
    

    def piccolo1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1080
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piccolo BLEND', '1080', subtotal))
            self.ecantidad.delete(0, END)

    
    def criosblend1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 980
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS BLEND', '840', subtotal))
            self.ecantidad.delete(0, END)
        

    def criosmalbec1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS MALBEC', '1100', subtotal))
            self.ecantidad.delete(0, END)

    
    def crioscab1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1020
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CRIOS CAB/SAU', '1020', subtotal))
            self.ecantidad.delete(0, END)

    
    def marcobonfante1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 960
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Marco Bonfante BARBERA', '960', subtotal))
            self.ecantidad.delete(0, END)

    
    def neroavola1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1050
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Nero de Avola', '1050', subtotal))
            self.ecantidad.delete(0, END)
    

    def mongrasssyr1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1000
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass CAB/SYR', '1000', subtotal))
            self.ecantidad.delete(0, END)

    
    def mongrassblend1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass Premium BLEND', '1450', subtotal))
            self.ecantidad.delete(0, END)

    
    def mongrasscab1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1060
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mongrass CAB/SAU', '1060', subtotal))
            self.ecantidad.delete(0, END)


    def decoy1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1600
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('DECOY PINOT NOIR', '1600', subtotal))
            self.ecantidad.delete(0, END)

    
    def lomita1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1020
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('La Lomita CAB/SAU', '1020', subtotal))
            self.ecantidad.delete(0, END)

    
    def castacardon1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casta Cardon BLEND', '1100', subtotal))
            self.ecantidad.delete(0, END)

    
    def harasdepirque1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1040
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Haras de Pirque BLEND', '1040', subtotal))
            self.ecantidad.delete(0, END)


    def harasgran1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Haras de Pirque Gran Reserva CAB/SAU', '1140', subtotal))
            self.ecantidad.delete(0, END)

    
    def minimalista1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 870
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Minimalista MALBEC', '870', subtotal))
            self.ecantidad.delete(0, END)

    
    def domino1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 980
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('DOMINO BLEND', '980', subtotal))
            self.ecantidad.delete(0, END)

    
    def abbout1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1030
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('ABBOUT PINOT NOIR', '1030', subtotal))
            self.ecantidad.delete(0, END)

    
    def bellaretta1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 830
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bellaretta CAB/SAU', '830', subtotal))
            self.ecantidad.delete(0, END)


    def carlidge1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Carlidge & Brown CAB', '1200', subtotal))
            self.ecantidad.delete(0, END)

       
    def gnarlyhead1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gnarly Head CAB', '1200', subtotal))
            self.ecantidad.delete(0, END)

    
    def santacristina1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1350
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Santa Cristina CHIANTI SUPERIORE', '1350', subtotal))
            self.ecantidad.delete(0, END)

    
    def colezionemolte1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Colezione MOLTEPULCIANO', '700', subtotal))
            self.ecantidad.delete(0, END)
    

    def caracter1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caracter MALBEC', '700', subtotal))
            self.ecantidad.delete(0, END)


    def tierraadentro1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tierra Adentro BLEND', '1100', subtotal))
            self.ecantidad.delete(0, END)


    def misassou1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 700
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mirassou CAB/SAU', '700', subtotal))
            self.ecantidad.delete(0, END)
    

    def kruguer1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Kruguer CAB/TEM', '1450', subtotal))
            self.ecantidad.delete(0, END)

    
    def care1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1150
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('CARE', '1150', subtotal))
            self.ecantidad.delete(0, END)

    
    def cetto1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 850
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Luis Cetto MERLOT', '850', subtotal))
            self.ecantidad.delete(0, END)

    
    def calycanto1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 795
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cal y Canto', '795', subtotal))
            self.ecantidad.delete(0, END)

    
    def cigliano1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cigliano CHIANTI CLASICO', '1200', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

                cantidad = IntVar()
                lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
                lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

                self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
                self.ecantidad = Entry(v, textvariable = cantidad)
                self.emesa = ttk.Combobox(v, value = lista_mesas)
                self.emesero = ttk.Combobox(v, value = lista_meseros)
