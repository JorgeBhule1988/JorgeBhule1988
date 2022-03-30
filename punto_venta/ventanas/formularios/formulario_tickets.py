from tkinter import *
from tkinter import ttk, messagebox
from formularios.botonesmenu import BonotonesMenu
import datetime
from tkinter.ttk import Notebook
import formularios.controlador_flujo as controlador
from formularios.tickets import Tickets 


class FormularioTickets(BonotonesMenu):

    def construir(self):
        error = controlador.construir()
        if(error == 1):
            messagebox.showerror(message=f"La tabla debe de existir", title="Error")  
        else:
            messagebox.showinfo(message=f"La tabla creada", title="Error")

    
    def cobrarticket(self):
        
        t = Tickets()
        t.mesero = self.emesero.get()
        t.mesa = self.emesa.get()
        t.fecha = self.formato_fecha
        t.total = self.etotalpesos.get()
        
        afectados =controlador.insertar_tickets(t)
        if(afectados == 0):
            messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados} registro", title="Salvar")   

        cobro = float(self.epago.get()) - float(self.etotalpesos.get())
        self.ecambio.insert(END, cobro)


    def generart(self):
        ticket = open('Ticket.txt', 'w')
        ticket.write('Ticket Numero: ### \n')
        ticket.write('Rodizio Grill \n')
        ticket.write('RFC: $$$$$ \n')
        ticket.write('Domicilio: ##### \n')
        ticket.write(f'Mesero: {self.emesero.get()} \n')
        ticket.write(f'Mesa: {self.emesa.get()} \n')
        ticket.write(f'Fecha: {self.formato_fecha} \n')
        ticket.write(f'Hora: {self.hora_formato} \n')
        ticket.write('Cant |\t Producto             |\t Precio |\t Total \n')
        for i in self.captura.get_children():
            item = self.captura.item(i)
            cant = item['text']
            prod = item['values'][0]
            prec = item['values'][1]
            subt = item['values'][2]
            ticket.write(f'{cant}    |\t {prod} |\t {prec}   |\t {subt} \n')
        ticket.write(f'Total Pesos: {self.etotalpesos.get()} \n')
        ticket.write(f'Total Dolares: {self.etotaldolares.get()} \n')
        ticket.write(f'Pago Con: {self.epago.get()} \n')
        ticket.write(f'Tipo de Pago: {self.etipo_pago.get()} \n')
        ticket.write(f'Cambio: {self.ecambio.get()} \n')

        self.lpago.place(x = 0, y = 80)
        self.ltipo_pago.place(x = 0, y = 120)
        self.lcambio.place(x = 0, y = 160)
        self.epago.place(x = 120, y = 83)
        self.etipo_pago.place(x = 120, y = 123)
        self.ecambio.place(x = 120, y = 163)
        self.cobrart.place(x = 80, y = 200)
        

    def nuevo_ticket(self):
        self.emesero.delete(0, END)
        self.emesa.delete(0, END)
        self.etotalpesos.delete(0, END)
        self.etotaldolares.delete(0, END)
        self.epago.delete(0, END)
        self.etipo_pago.delete(0, END)
        self.ecambio.delete(0, END)
        regitro = self.captura.get_children()
        for i in regitro:
            self.captura.delete(i)


    def Limpiarticket(self):
        regitro = self.captura.selection() #captura.get_children()
        for i in regitro:
            self.captura.delete(i)


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
        
        self.cerrart.place(x = 345, y = 215)


    def __init__(self, window):

        cantidad = IntVar()
        mesero = StringVar()
        mesa = StringVar()
        
        frametabla = Frame(window)
        frametabla.pack(side = LEFT, fill = BOTH)
        frametabla.config(height = 250, width = 450)

        #creacion de la vista de los productos
        self.captura = ttk.Treeview(frametabla, height=11, columns=('#0', '#1', '#2'))
        self.captura.place(x = 0, y = 250)
        self.captura.column('#0', width = 50)
        self.captura.heading('#0', text = 'Cant', anchor=CENTER)
        self.captura.heading('#1', text = 'Producto', anchor=CENTER)
        self.captura.column('#2', width = 100)
        self.captura.heading('#2', text = 'Precio Unit', anchor=CENTER)
        self.captura.column('#3', width = 100)
        self.captura.heading('#3', text = 'Total', anchor=CENTER)

        #Scrollbar Treeview
        deslizarv = ttk.Scrollbar(frametabla, orient = 'vertical', command = self.captura.yview)
        deslizarv.place(x = 433, y = 250, relheight = 0.5)
        deslizarv.config(command = self.captura.yview)
        self.captura.configure(yscrollcommand = deslizarv.set)
        
        #formato de fecha actual
        fecha_actual = datetime.datetime.now()
        self.formato_fecha = datetime.datetime.strftime(fecha_actual, '%d/%m/%Y')
        self.hora_formato = datetime.datetime.strftime(fecha_actual, '%H:%M:%S')
        
        fcobro = Frame(window, height = 245, width = 240)
        fcobro.place(x = 450, y = 250)
        
        fmenu = Frame(window, height = 200, width = 240) #Frame de los botones de mesas
        fmenu.place(x = 450, y = 40)

        #botones de seleccion de mesas de seleccion
        self.bmesa1 = Button(fmenu, text = '1', height = 2, width = 5, command = self.mesa1)
        self.bmesa1.place(x = 0, y = 40)
        self.bmesa3 = Button(fmenu, text = '3', height = 2, width = 5, command = self.mesa3)
        self.bmesa3.place(x = 50, y = 40)
        self.bmesa5 = Button(fmenu, text = '5', height = 2, width = 5)
        self.bmesa5.place(x = 100, y = 40)
        self.bmesa6 = Button(fmenu, text = '6', height = 2, width = 5)
        self.bmesa6.place(x = 150, y = 40)
        self.bmesa7 = Button(fmenu, text = '7', height = 2, width = 5)
        self.bmesa7.place(x = 200, y = 40)
        self.bmesa8 = Button(fmenu, text = '8', height = 2, width = 5)
        self.bmesa8.place(x = 0, y = 85)
        self.bmesa9 = Button(fmenu, text = '9', height = 2, width = 5)
        self.bmesa9.place(x = 50, y = 85)
        self.bmesa10 = Button(fmenu, text = '10', height = 2, width = 5)
        self.bmesa10.place(x = 100, y = 85)
        self.bmesa11 = Button(fmenu, text = '11', height = 2, width = 5)
        self.bmesa11.place(x = 150, y = 85)
        self.bmesa12 = Button(fmenu, text = '12', height = 2, width = 5)
        self.bmesa12.place(x = 200, y = 85)
        self.bmesa13 = Button(fmenu, text = '13', height = 2, width = 5)
        self.bmesa13.place(x = 0, y = 130)
        self.bmesacv1 = Button(fmenu, text = 'CV1', height = 2, width = 5)
        self.bmesacv1.place(x = 50, y = 130)
        self.bmesacv2 = Button(fmenu, text = 'CV2', height = 2, width = 5)
        self.bmesacv2.place(x = 100, y = 130)
        self.bmesacv3 = Button(fmenu, text = 'CV3', height = 2, width = 5)
        self.bmesacv3.place(x = 150, y = 130)
        self.bmesacv4 = Button(fmenu, text = 'CV4', height = 2, width = 5)
        self.bmesacv4.place(x = 200, y = 130)

        # Creacion de etiquetas
        self.lmesero = Label(frametabla, text = 'Mesero', font = ('Arial', 12, 'bold'))
        self.lmesa = Label(frametabla, text = 'Mesa', font = ('Arial', 12, 'bold'))
        self.lcantidad = Label(frametabla, text = 'Cant', font = ('Arial', 12, 'bold'))
        self.ltotalpesos = Label(fcobro, text = 'Total Pesos', font = ('Arial', 12, 'bold'))
        self.ltotaldolares = Label(fcobro, text = 'Total Dolares', font = ('Arial', 12, 'bold'))
        self.lfecha_label = Label(window, text = 'Fecha:', font = ('Arial', 12, 'bold'))
        self.lfecha_actual = Label(window, text = self.formato_fecha, font = ('Arial', 12, 'bold'))
        self.lpago = Label(fcobro, text = 'Cobrar', font = ('Arial', 12, 'bold'))
        self.ltipo_pago = Label(fcobro, text = 'Tipo de Pago', font = ('Arial', 12, 'bold'))
        self.lcambio = Label(fcobro, text = 'Cambio', font = ('Arial', 12, 'bold'))
        
        #Posiciones de Etiquetas
        self.lmesero.place(x = 0, y = 10)
        self.lmesa.place(x = 300, y = 10)
        self.lcantidad.place(x = 0, y = 220)
        self.lfecha_label.place(x = 500, y = 10)
        self.lfecha_actual.place(x = 570, y = 10)
        self.ltotalpesos.place(x = 0, y = 0)
        self.ltotaldolares.place(x = 0, y = 40)
        
        tipo_p = ['EFECTIVO', 'DOLARES', 'TARJETA']

        #Creacion de cajas de texto
        self.ecantidad = Entry(frametabla, textvariable = cantidad, width = 5)
        self.emesero = Entry(frametabla, textvariable = mesero, width = 35)
        self.emesa = Entry(frametabla, textvariable = mesa, width = 15)
        self.etotalpesos = Entry(fcobro, width = 15)
        self.etotaldolares = Entry(fcobro, width = 15)
        self.epago = Entry(fcobro, width = 15)
        self.etipo_pago = ttk.Combobox(fcobro, width = 12, values = tipo_p)
        self.ecambio = Entry(fcobro, width = 15)

        #Posiciones de las cajas de texto
        self.ecantidad.place(x = 55, y = 220)
        self.emesero.place(x = 70, y = 10)
        self.emesa.place(x = 350, y = 13)
        self.etotalpesos.place(x = 120, y = 0)
        self.etotaldolares.place(x = 120, y = 43)

        #Notebook
        pmenu = Notebook(frametabla, height = 138, width = 450)
        pmenu.place(x = 0, y = 35)
        frame1 = Frame(pmenu, height = 138, width = 450)
        frame2 = Frame(pmenu, height = 138, width = 450)
        frame3 = Frame(pmenu, height = 138, width = 450)
        frame4 = Frame(pmenu, height = 138, width = 450)
        frame5 = Frame(pmenu, height = 138, width = 450)
        frame6 = Frame(pmenu, height = 138, width = 450)
        frame7 = Frame(pmenu, height = 138, width = 450)
        #frame8 = Frame(pmenu, height = 138, width = 450)
        #frame9 = Frame(pmenu, height = 138, width = 450)
        #frame10 = Frame(pmenu, height = 138, width = 450)
        #frame11 = Frame(pmenu, height = 138, width = 450)
        #frame12 = Frame(pmenu, height = 138, width = 450)
        frame1.place(x = 0, y = 35)
        frame2.place(x = 0, y = 35)
        frame3.place(x = 0, y = 35)
        frame4.place(x = 0, y = 35)
        frame5.place(x = 0, y = 35)
        frame6.place(x = 0, y = 35)
        frame7.place(x = 0, y = 35)
        #frame8.place(x = 0, y = 35)
        #frame9.place(x = 0, y = 35)
        #frame10.place(x = 0, y = 35)
        #frame11.place(x = 0, y = 35)
        #frame12.place(x = 0, y = 35)
        pmenu.add(frame1, text='Comida')
        pmenu.add(frame2, text='Bebida S/A')
        pmenu.add(frame3, text='Cervezas')
        pmenu.add(frame4, text='Cockteleria')
        pmenu.add(frame5, text='BVTINTO')
        pmenu.add(frame6, text='BVBLANCO')
        pmenu.add(frame7, text='WHISKY')
        #pmenu.add(frame8, text='TEQUILA')
        #pmenu.add(frame9, text='MEZCAL')
        #pmenu.add(frame10, text='DIJESTIVOS')
        #pmenu.add(frame11, text='BOT VINO TINTO')
        #pmenu.add(frame12, text='BOT VINO BLANCO')

        #creacion de botones
        self.brodizio = Button(frame1, text = 'Rodizio', height = 3, width = 8, command = self.botonrodizio)
        self.brodiziol = Button(frame1, text = 'RodizioL', height = 3, width = 8, command = self.botonrodiziol)
        self.brodiziom = Button(frame1, text = 'RodizioM', height = 3, width = 8, command = self.botonrodiziom)
        self.brodiziolm = Button(frame1, text = 'RodizioLM', height = 3, width = 8, command = self.botonrodizioml)
        self.brodiziotg = Button(frame1, text = 'RodizioTG', height = 3, width = 8, command = self.botonrodiziotg)
        self.bpicana = Button(frame1, text = 'Picaña', height = 3, width = 8, command = self.botonpicana)
        self.bpicanatg = Button(frame1, text = 'PicañaTG', height = 3, width = 8, command = self.botonpicanatg)
        self.btomahack = Button(frame1, text = 'TOMA HACK', height = 3, width = 8, command = self.botontomahack)
        self.bburguer = Button(frame1, text = 'Burguer', height = 3, width = 8, command = self.botonburguer)
        self.bburguertg = Button(frame1, text = 'BurguerTG', height = 3, width = 8, command = self.botonburguertg)
        self.bbotagua = Button(frame2, text = 'Agua Panna', height = 3, width = 8, command = self.botonaguap)
        self.btopochico = Button(frame2, text = 'Topochico', height = 3, width = 8, command = self.botontopoc)
        self.blimonada = Button(frame2, text = 'Limonada', height = 3, width = 8, command = self.botonlimonada)
        self.bnaranjada = Button(frame2, text = 'Naranjada', height = 3, width = 8, command = self.botonnaranjada)
        self.bcoca = Button(frame2, text = 'Coca Cola', height = 3, width = 8, command = self.botoncoca)
        self.bcocad = Button(frame2, text = 'Coca Dieta', height = 3, width = 8, command = self.botoncocad)
        self.bsprite = Button(frame2, text = 'Sprite', height = 3, width = 8, command = self.botonsprite)
        self.bfresca = Button(frame2, text = 'Fresca', height = 3, width = 8, command = self.botonfresca)
        self.bmundet = Button(frame2, text = 'Mundet', height = 3, width = 8, command = self.botonmundet)
        self.bpinada = Button(frame2, text = 'Piñada', height = 3, width = 8, command = self.botonpinada)
        self.bmojv = Button(frame2, text = 'Mojito S/A', height = 3, width = 8, command = self.botonmojitov)
        self.bpituv = Button(frame2, text = 'Caipiriña S/A', height = 3, width = 8, command = self.botonpituv)
        self.pacifico = Button(frame3, text = 'Pacifico', height = 3, width = 8, command = self.botonpacifico)
        self.pacificos = Button(frame3, text = 'Pacifico S', height = 3, width = 8, command = self.botonpacificos)
        self.pacificol = Button(frame3, text = 'Pacifico L', height = 3, width = 8, command = self.botonpacificol)
        self.corona = Button(frame3, text = 'Corona', height = 3, width = 8, command = self.botoncorona)
        self.victoria = Button(frame3, text = 'Victoria', height = 3, width = 8, command = self.botonvictoria)
        self.artesanal = Button(frame3, text = 'Artesanal', height = 3, width = 8, command = self.botonartesanal)
        self.negram = Button(frame3, text = 'Negra Modelo', height = 3, width = 8, command = self.botonegramodelo)
        self.bmezcalitaj = Button(frame4, text = 'Mezcalita J', height = 3, width = 8, command = self.botonmezcalitaj)
        self.mojito = Button(frame4, text = 'Mojito', height = 3, width = 8, command = self.botonmojito)
        self.bpitu = Button(frame4, text = 'Caipiriña', height = 3, width = 8, command = self.botoncaipirina)
        self.bcasama = Button(frame5, text = 'Casa Madero', height = 3, width = 8, command = self.botocasamadero)
        self.bcvino = Button(frame5, text = 'Copa de Vino', height = 3, width = 8, command = self.botoncopadevino)
        self.bcrose = Button(frame6, text = 'Cavall Rose', height = 3, width = 8, command = self.botoncavalrose)

        #Posiciones de botones del menu
        self.brodizio.place(x = 0, y = 0)
        self.brodiziol.place(x = 70, y = 0)
        self.brodiziom.place(x = 140, y = 0)
        self.brodiziolm.place(x = 210, y = 0)
        self.brodiziotg.place(x = 280, y = 0)
        self.bpicana.place(x = 350, y = 0)
        self.bpicanatg.place(x = 0, y = 60)
        self.btomahack.place(x = 70, y = 60)
        self.bburguer.place(x = 140, y = 60)
        self.bburguertg.place(x = 210, y = 60)
        self.bbotagua.place(x = 0, y = 0)
        self.btopochico.place(x = 70, y = 0)
        self.blimonada.place(x = 140, y = 0)
        self.bnaranjada.place(x = 210, y = 0)
        self.bcoca.place(x = 280, y = 0)
        self.bcocad.place(x = 350, y = 0)
        self.bsprite.place(x = 0, y = 60)
        self.bfresca.place(x = 70, y = 60)
        self.bmundet.place(x = 140, y = 60)
        self.bpinada.place(x = 210, y = 60)
        self.bmojv.place(x = 280, y = 60)
        self.bpituv.place(x = 350, y = 60)
        self.pacifico.place(x = 0, y = 0)
        self.pacificos.place(x = 70, y = 0)
        self.pacificol.place(x = 140, y = 0)
        self.corona.place(x = 210, y = 0)
        self.victoria.place(x = 280, y = 0)
        self.artesanal.place(x = 350, y = 0)
        self.negram.place(x = 0, y = 60)
        self.bmezcalitaj.place(x = 0, y = 0)
        self.bpitu.place(x = 70, y = 0)
        self.mojito.place(x= 140, y = 0)
        self.bcasama.place(x = 0, y = 0)
        self.bcvino.place(x = 70, y = 0)
        self.bcrose.place(x = 0, y = 0)

        #Creacion de boton acciones
        self.bguardar = ttk.Button(frametabla, text = 'Total', command = self.sumartotales)
        self.bguardar.place(x = 265, y = 215)
        self.blimpiar = ttk.Button(frametabla, text = 'Limpiar Ticket', command = self.Limpiarticket)
        self.blimpiar.place(x = 180, y = 215)
        #self.bback = ttk.Button(window, text = 'Salir', command = window.destroy)
        #self.bback.place(x = 375, y = 215)
        self.cerrart = ttk.Button(frametabla, text = 'Guardar Ticket', command = self.generart)
        self.cobrart = ttk.Button(fcobro, text = 'Cobrar', command = self.cobrarticket)
        self.nuevot = ttk.Button(frametabla, text = 'Nuevo Ticket', command = self.nuevo_ticket)
        self.nuevot.place(x = 100, y = 215)
