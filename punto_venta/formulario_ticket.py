from tkinter import *
from tkinter import ttk
import datetime


class FormularioTickets:
    
    def regresar(self):
        pass
        

    def Limpiarticket(self):
        regitro = self.captura.selection() #captura.get_children()
        for i in regitro:
            self.captura.delete(i)


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


    def sumartotales(self):
        suma = 0
        sumadolares = 0
        for i in self.captura.get_children():
            item = self.captura.item(i)
            records = item['values'][2]
            suma += float(records)
            sumadolares = float(suma // 19)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)


    def __init__(self, window):

        cantidad = IntVar()

        #creacion de la vista de los productos
        self.captura = ttk.Treeview(window, height=20, columns=('#0', '#1', '#2'))
        self.captura.place(x = 0, y = 250)
        self.captura.column('#0', width = 50)
        self.captura.heading('#0', text = 'Cant', anchor=CENTER)
        self.captura.heading('#1', text = 'Producto', anchor=CENTER)
        self.captura.column('#2', width = 100)
        self.captura.heading('#2', text = 'Precio Unit', anchor=CENTER)
        self.captura.column('#3', width = 100)
        self.captura.heading('#3', text = 'Total', anchor=CENTER)
        
        #formato de fecha actual
        fecha_actual = datetime.datetime.now()
        formato_fecha = datetime.datetime.strftime(fecha_actual, '%d/%m/%Y')
        
        # Creacion de etiquetas
        self.lmesero = Label(window, text = 'Mesero', font = ('Arial', 12, 'bold'))
        self.lmesa = Label(window, text = 'Mesa', font = ('Arial', 12, 'bold'))
        self.lcantidad = Label(window, text = 'Cant', font = ('Arial', 12, 'bold'))
        self.ltotalpesos = Label(window, text = 'Total', font = ('Arial', 12, 'bold'))
        self.ltotaldolares = Label(window, text = 'Total Dolares', font = ('Arial', 12, 'bold'))
        self.lfecha_label = Label(window, text = 'Fecha', font = ('Arial', 12, 'bold'))
        self.lfecha_actual = Label(window, text = formato_fecha, font = ('Arial', 12, 'bold'))
        
        #Posiciones de Etiquetas
        self.lmesero.place(x = 0, y = 10)
        self.lmesa.place(x = 300, y = 10)
        self.lcantidad.place(x = 300, y = 200)
        self.lfecha_label.place(x = 550, y = 10)
        self.lfecha_actual.place(x = 550, y = 40)
        self.ltotalpesos.place(x = 550, y = 100)
        self.ltotaldolares.place(x = 550, y = 170)

        #Creacion de cajas de texto
        self.ecantidad = Entry(window, textvariable = cantidad, width = 16)
        self.emesero = Entry(window, width = 35)
        self.emesa = Entry(window, width = 15)
        self.etotalpesos = Entry(window)
        self.etotaldolares = Entry(window)

        #Posiciones de las cajas de texto
        self.ecantidad.place(x = 350, y = 200)
        self.emesero.place(x = 70, y = 10)
        self.emesa.place(x = 350, y = 10)
        self.etotalpesos.place(x = 550, y = 130)
        self.etotaldolares.place(x = 550, y = 200)

        #creacion de botones
        self.brodizio = Button(window, text = 'Rodizio', height = 3, width = 8, command = self.botonrodizio)
        self.brodiziol = Button(window, text = 'RodizioL', height = 3, width = 8, command = self.botonrodiziol)
        self.brodiziom = Button(window, text = 'RodizioM', height = 3, width = 8, command = self.botonrodiziom)
        self.brodiziolm = Button(window, text = 'RodizioLM', height = 3, width = 8, command = self.botonrodizioml)
        self.brodiziotg = Button(window, text = 'RodizioTG', height = 3, width = 8, command = self.botonrodiziotg)
        self.bpicana = Button(window, text = 'Picaña', height = 3, width = 8, command = self.botonpicana)
        self.bpicanatg = Button(window, text = 'PicañaTG', height = 3, width = 8, command = self.botonpicanatg)
        self.btomahack = Button(window, text = 'Tomahack', height = 3, width = 8, command = self.botontomahack)
        self.bburguer = Button(window, text = 'Burguer', height = 3, width = 8, command = self.botonburguer)
        self.bburguertg = Button(window, text = 'BurguerTG', height = 3, width = 8, command = self.botonburguertg)
        self.bbotagua = Button(window, text = 'Agua Panna', height = 3, width = 8, command = self.botonaguap)
        self.btopochico = Button(window, text = 'Topochico', height = 3, width = 8, command = self.botontopoc)
        self.blimonada = Button(window, text = 'Limonada', height = 3, width = 8, command = self.botonlimonada)
        self.bnaranjada = Button(window, text = 'Naranjada', height = 3, width = 8, command = self.botonnaranjada)
        self.bcoca = Button(window, text = 'Coca Cola', height = 3, width = 8, command = self.botoncoca)
        self.bcocad = Button(window, text = 'Coca Dieta', height = 3, width = 8, command = self.botoncocad)
        self.bsprite = Button(window, text = 'Sprite', height = 3, width = 8, command = self.botonsprite)
        self.bfresca = Button(window, text = 'Fresca', height = 3, width = 8, command = self.botonfresca)

        #Posiciones de botones del menu
        self.brodizio.place(x = 0, y = 40)
        self.brodiziol.place(x = 70, y = 40)
        self.brodiziom.place(x = 140, y = 40)
        self.brodiziolm.place(x = 210, y = 40)
        self.brodiziotg.place(x = 280, y = 40)
        self.bpicana.place(x = 350, y = 40)
        self.bpicanatg.place(x = 420, y = 40)
        self.btomahack.place(x = 0, y = 100)
        self.bburguer.place(x = 70, y = 100)
        self.bburguertg.place(x = 140, y = 100)
        self.bbotagua.place(x = 210, y = 100)
        self.btopochico.place(x = 280, y = 100)
        self.blimonada.place(x = 350, y = 100)
        self.bnaranjada.place(x = 420, y = 100)
        self.bcoca.place(x = 0, y = 160)
        self.bcocad.place(x = 70, y = 160)
        self.bsprite.place(x = 140, y = 160)
        self.bfresca.place(x = 210, y = 160)

        #Creacion de boton acciones
        self.bguardar = ttk.Button(window, text = 'Total', command = self.sumartotales)
        self.bguardar.place(x = 550, y = 250)
        self.blimpiar = ttk.Button(window, text = 'Limpiar Ticket', command = self.Limpiarticket)
        self.blimpiar.place(x = 550, y = 300)
        self.bback = ttk.Button(window, text = 'Regresar', command = self.regresar)
        self.bback.place(x = 550, y = 350)
