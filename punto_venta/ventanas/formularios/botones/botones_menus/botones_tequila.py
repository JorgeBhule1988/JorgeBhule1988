from tkinter import *
from tkinter import ttk, messagebox

class BotonesTequila:

    def jimadorrep1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Jimador Reposado', '100', subtotal))
            self.ecantidad.delete(0, END)


    def jimadorblan1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Jimador Blanco', '100', subtotal))
            self.ecantidad.delete(0, END)


    def hornitosrep1(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hornitos Reposado', '120', subtotal))
            self.ecantidad.delete(0, END)

    
    def hornitosblack1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hornitos Black Barrel', '140', subtotal))
            self.ecantidad.delete(0, END)
    

    def tradicionalblanco1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tradicional Blanco', '120', subtotal))
            self.ecantidad.delete(0, END)

    
    def tradicionalrep1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tradicional Reposado', '120', subtotal))
            self.ecantidad.delete(0, END)
        

    def centenario1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Centenario Añejo', '100', subtotal))
            self.ecantidad.delete(0, END)

    
    def anejo_1800_1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('1800 Añejo', '140', subtotal))
            self.ecantidad.delete(0, END)

    
    def herradurarep1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 160
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Herradura Reposado', '160', subtotal))
            self.ecantidad.delete(0, END)

    
    def cazadores1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cazadores', '100', subtotal))
            self.ecantidad.delete(0, END)
    

    def cazadoresane1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cazadores Añejo', '120', subtotal))
            self.ecantidad.delete(0, END)

    
    def donjulioblanco1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Julio Blanco', '180', subtotal))
            self.ecantidad.delete(0, END)

    
    def donjuliorep1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Julio Reposado', '200', subtotal))
            self.ecantidad.delete(0, END)


    def donjulio_70_1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 245
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Julio 70', '245', subtotal))
            self.ecantidad.delete(0, END)

    
    def herraduraane1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Herradura Añejo', '200', subtotal))
            self.ecantidad.delete(0, END)

    
    def codigorep1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 190
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Codigo Reposado', '190', subtotal))
            self.ecantidad.delete(0, END)

    
    def tequilacasa1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tequila de la Casa', '100', subtotal))
            self.ecantidad.delete(0, END)


    def virreyes1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 100
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Vireyes Reposado', '100', subtotal))
            self.ecantidad.delete(0, END)

    
    def tresgeneariones1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 130
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('3 Generaciones', '130', subtotal))
            self.ecantidad.delete(0, END)

    
    def reysol1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 600
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rey Sol', '600', subtotal))
            self.ecantidad.delete(0, END)

    
    def casadragones1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Dragones Añejo', '450', subtotal))
            self.ecantidad.delete(0, END)

    
    def casadragonesblanco1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Casa Dragones Blanco', '250', subtotal))
            self.ecantidad.delete(0, END)


    def selectsuprema1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 450
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Seleccion Suprema', '450', subtotal))
            self.ecantidad.delete(0, END)

       
    def maestrodobel1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 350
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Maestro Dobel Cristalino', '350', subtotal))
            self.ecantidad.delete(0, END)

    
    def cristalino_1800_1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 280
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('1800 Cristalino', '280', subtotal))
            self.ecantidad.delete(0, END)

    
    def milenio_1800_1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 400
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('1800 Milenio', '400', subtotal))
            self.ecantidad.delete(0, END)
    

    def loco1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 350
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Tequila Loco', '350', subtotal))
            self.ecantidad.delete(0, END)


    def donjulio_1942_1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 320
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Don Julio 1942', '320', subtotal))
            self.ecantidad.delete(0, END)


    def claseazul1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 385
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clase Azul', '385', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
