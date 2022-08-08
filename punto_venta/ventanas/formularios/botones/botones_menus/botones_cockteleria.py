from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BotonesCockteleria:
    
    def mojito(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito', '160', subtotal))
            self.ecantidad.delete(0, END)


    def mezcalitaj(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Jamaica', '165', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitam(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '165', subtotal))
            self.ecantidad.delete(0, END)


    def caipirina(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña', '180', subtotal))
            self.ecantidad.delete(0, END)

    
    def mojitotinto1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito Vino Tinto', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def mojitosabores1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito Sabores', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def guanabanagin1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)


    def martinicoffe1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coffe Martini', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritarodizio1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margarita Rodizio', '180', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritamango1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Mango', '185', subtotal))
            self.ecantidad.delete(0, END)
    
    def margaritaguanabana1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)

        
    def margaritamaracuya1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritatradicional1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def margaritacadillac1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 265
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Margatita Cadillac', '265', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitatradicional1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 180
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita', '180', subtotal))
            self.ecantidad.delete(0, END)


    def mezcalitamango1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Mango', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitamaracuya1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def mezcalitaguanabana1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)


    def pitumango1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Mango', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def pitumaracuya1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Maracuya', '185', subtotal))
            self.ecantidad.delete(0, END)


    def pituguanabana1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña Guanabana', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def negroni1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negroni', '220', subtotal))
            self.ecantidad.delete(0, END)

    
    def gintonic1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gin Tonic', '220', subtotal))
            self.ecantidad.delete(0, END)

    
    def oldfashion1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Old Fashion', '220', subtotal))
            self.ecantidad.delete(0, END)


    def clericottinto1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 145
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot', '145', subtotal))
            self.ecantidad.delete(0, END)

    
    def clericotrosado1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot Rosado', '185', subtotal))
            self.ecantidad.delete(0, END)

    
    def clericotblueberry1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Clericot Blue Berry', '185', subtotal))
            self.ecantidad.delete(0, END)
    

    def gavilan_reyes1(self):
            if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
                messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
            else:
                subtotal = float(self.ecantidad.get()) * 185
                self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Gavilan Reyes', '185', subtotal))
                self.ecantidad.delete(0, END)

    
    def sangria1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 110
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sangria', '110', subtotal))
            self.ecantidad.delete(0, END)

    
    def pina_colada1(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piña Colada', '140', subtotal))
            self.ecantidad.delete(0, END)


    def __init__(self, v):

            cantidad = IntVar()
            lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
            lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

            self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
            self.ecantidad = Entry(v, textvariable = cantidad)
            self.emesa = ttk.Combobox(v, value = lista_mesas)
            self.emesero = ttk.Combobox(v, value = lista_meseros)
