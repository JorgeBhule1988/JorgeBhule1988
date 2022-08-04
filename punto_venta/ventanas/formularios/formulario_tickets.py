from tkinter import *
from tkinter import ttk, messagebox
from formularios.formulario_estadistica import ventana2
from formularios.botonesmenu import BonotonesMenu
import datetime
from tkinter.ttk import Notebook
import formularios.controlador_flujo as controlador
from formularios.tickets import Tickets, Tickets2
from formularios.formulario_consulta import ventana



class FormularioTickets(BonotonesMenu):

    def construir(self):
        error = controlador.construir()
        if(error == 1):
            messagebox.showerror(message=f"La tabla debe de existir", title="Error")  
        else:
            messagebox.showinfo(message=f"La tabla creada", title="Error")

        error = controlador.construir2()
        if(error == 1):
            messagebox.showerror(message=f"La tabla debe de existir", title="Error")  
        else:
            messagebox.showinfo(message=f"La tabla creada", title="Error")

        error = controlador.construir3()
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
        t.tipopago = self.etipo_pago.get()
        
        afectados =controlador.insertar_tickets(t)
        if(afectados == 0):
            messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados} registro", title="Salvar") 
        

        cobro = float(self.epago.get()) - float(self.etotalpesos.get())
        self.ecambio.delete(0, END)
        self.ecambio.insert(END, cobro)


    def generart(self):

        t2 = Tickets2()
        for i in self.captura.get_children():
            item = self.captura.item(i)
            t2.mesero = self.emesero.get()
            t2.mesa = self.emesa.get()
            t2.fecha = self.formato_fecha
            t2.cantidad = item['text']
            t2.producto = item['values'][0]
            t2.precio_unitario = item['values'][1] 
            t2.total = item['values'][2] 

            afectados1 = controlador.insertar_tickets2(t2)
        
        if(afectados1 == 0):
            messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados1} registro", title="Salvar")

        
        t3 = Tickets2()
        for i in self.captura.get_children():
            item = self.captura.item(i)
            t3.mesero = self.emesero.get()
            t3.mesa = self.emesa.get()
            t3.fecha = self.formato_fecha
            t3.cantidad = item['text']
            t3.producto = item['values'][0]
            t3.precio_unitario = item['values'][1] 
            t3.total = item['values'][2] 

            afectados2 =controlador.insertar_tickets3(t3)
        
        if(afectados2 == 0):
            messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados1} registro", title="Salvar")


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
        
        if self.emesa.get() == '1':
            self.bmesa1.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '3':
            self.bmesa3.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '5':
            self.bmesa5.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '6':
            self.bmesa6.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '7':
            self.bmesa7.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '8':
            self.bmesa8.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '9':
            self.bmesa9.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '10':
            self.bmesa10.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '11':
            self.bmesa11.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '12':
            self.bmesa12.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == '13':
            self.bmesa13.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == 'Cava1':
            self.bmesacv1.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == 'Cava2':
            self.bmesacv2.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == 'Cava3':
            self.bmesacv3.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == 'Cava4':
            self.bmesacv4.config(state = 'normal', bg = 'green')
        
        self.nuevo_ticket()
  

    def liberarmesa(self):
    
        afectados = controlador.eliminar_tickets(self.emesa.get())
        if(afectados == 0):
            messagebox.showerror(message=f"Error al eliminar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Elimino con exito {afectados} registro", title="Eliminar")

        if self.emesa.get() == '1':
            self.bmesa1.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '3':
            self.bmesa3.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '5':
            self.bmesa5.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '6':
            self.bmesa6.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '7':
            self.bmesa7.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '8':
            self.bmesa8.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '9':
            self.bmesa9.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '10':
            self.bmesa10.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '11':
            self.bmesa11.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '12':
            self.bmesa12.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == '13':
            self.bmesa13.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == 'Cava1':
            self.bmesacv1.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == 'Cava2':
            self.bmesacv2.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == 'Cava3':
            self.bmesacv3.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == 'Cava4':
            self.bmesacv4.config(state = 'disable', bg = 'red')

        self.nuevo_ticket()
        
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.config(state = 'disable')
        self.epago.config(state = 'disable')
        self.etipo_pago.config(state = 'disable')
        self.ecambio.config(state = 'disable')
        self.bguardar.config(state = 'disable')
        self.cobrart.config(state = 'disable')
        self.cerrarmesa.config(state = 'disable')
    

    def eliminarfila(self):
        
        curItem = self.captura.focus()
        fila = self.captura.item(curItem)
        afectados = controlador.eliminar_fila_cobro(fila["values"][0])
        afectados1 = controlador.eliminar_fila_cobro2(fila["values"][0])
        if(afectados == 0 and afectados1 == 0):
            messagebox.showinfo(message = f'Elimino con exito {afectados}{afectados1} registros', title = 'Eliminar')
        else:
            messagebox.showerror(message = 'Error al eliminar verifique la clave no este repetida', title = 'Error')


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
        
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.config(state = 'disable')
        self.epago.config(state = 'disable')
        self.etipo_pago.config(state = 'disable')
        self.ecambio.config(state = 'disable')
        self.bguardar.config(state = 'disable')
        self.cobrart.config(state = 'disable')
        self.cerrarmesa.config(state = 'disable')


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
 
       
    def preguntar(self):
        questions = messagebox.askquestion('Cobrar Ticket', 'Quieres realizar un cobro?')
        if questions == 'yes':
            self.etotalpesos.config(state = 'normal')
            self.etotaldolares.config(state = 'normal')
            self.epago.config(state = 'normal')
            self.etipo_pago.config(state = 'normal')
            self.ecambio.config(state = 'normal')
            self.bguardar.config(state = 'normal')
            self.cobrart.config(state = 'normal')
            self.cerrarmesa.config(state = 'normal')
        else:
            self.etotalpesos.config(state = 'disable')
            self.etotaldolares.config(state = 'disable')
            self.epago.config(state = 'disable')
            self.etipo_pago.config(state = 'disable')
            self.ecambio.config(state = 'disable')
            self.bguardar.config(state = 'disable')
            self.cobrart.config(state = 'disable')
            self.cerrarmesa.config(state = 'disable')


    def __init__(self, window):

        cantidad = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
        
        frametabla = Frame(window)
        frametabla.pack(side = LEFT, fill = BOTH)
        frametabla.config(height = 550, width = 750)

        #creacion de la vista de los productos
        self.captura = ttk.Treeview(frametabla, height=11, columns=('#0', '#1', '#2'))
        self.captura.place(x = 0, y = 450)
        self.captura.column('#0', width = 50)
        self.captura.heading('#0', text = 'Cant', anchor=CENTER)
        self.captura.heading('#1', text = 'Producto', anchor=CENTER)
        self.captura.column('#2', width = 100)
        self.captura.heading('#2', text = 'Precio Unit', anchor=CENTER)
        self.captura.column('#3', width = 100)
        self.captura.heading('#3', text = 'Total', anchor=CENTER)

        #Scrollbar Treeview
        deslizarv = ttk.Scrollbar(frametabla, orient = 'vertical', command = self.captura.yview)
        deslizarv.place(x = 433, y = 450, relheight = 0.5)
        deslizarv.config(command = self.captura.yview)
        self.captura.configure(yscrollcommand = deslizarv.set)
        
        #formato de fecha actual
        fecha_actual = datetime.datetime.now()
        self.formato_fecha = datetime.datetime.strftime(fecha_actual, '%b/%d/%Y')
        self.hora_formato = datetime.datetime.strftime(fecha_actual, '%H:%M:%S')
        
        fcobro = Frame(window, height = 245, width = 240)
        fcobro.place(x = 460, y = 460)
        
        fmenu = Frame(window, height = 200, width = 240) #Frame de los botones de mesas
        fmenu.place(x = 800, y = 40)

        #botones de seleccion de mesas de seleccion
        self.bmesa1 = Button(fmenu, text = '1', height = 2, width = 5, command = self.mesa1)
        self.bmesa1.place(x = 0, y = 40)
        self.bmesa1.config(state='disable', bg = 'red')
        self.bmesa3 = Button(fmenu, text = '3', height = 2, width = 5, command = self.mesa3)
        self.bmesa3.place(x = 50, y = 40)
        self.bmesa3.config(state='disable', bg = 'red')
        self.bmesa5 = Button(fmenu, text = '5', height = 2, width = 5, command = self.mesa5)
        self.bmesa5.place(x = 100, y = 40)
        self.bmesa5.config(state='disable', bg = 'red')
        self.bmesa6 = Button(fmenu, text = '6', height = 2, width = 5, command = self.mesa6)
        self.bmesa6.place(x = 150, y = 40)
        self.bmesa6.config(state='disable', bg = 'red')
        self.bmesa7 = Button(fmenu, text = '7', height = 2, width = 5, command = self.mesa7)
        self.bmesa7.place(x = 200, y = 40)
        self.bmesa7.config(state='disable', bg = 'red')
        self.bmesa8 = Button(fmenu, text = '8', height = 2, width = 5, command = self.mesa8)
        self.bmesa8.place(x = 0, y = 85)
        self.bmesa8.config(state='disable', bg = 'red')
        self.bmesa9 = Button(fmenu, text = '9', height = 2, width = 5, command = self.mesa9)
        self.bmesa9.place(x = 50, y = 85)
        self.bmesa9.config(state='disable', bg = 'red')
        self.bmesa10 = Button(fmenu, text = '10', height = 2, width = 5, command = self.mesa10)
        self.bmesa10.place(x = 100, y = 85)
        self.bmesa10.config(state='disable', bg = 'red')
        self.bmesa11 = Button(fmenu, text = '11', height = 2, width = 5, command = self.mesa11)
        self.bmesa11.place(x = 150, y = 85)
        self.bmesa11.config(state='disable', bg = 'red')
        self.bmesa12 = Button(fmenu, text = '12', height = 2, width = 5, command = self.mesa12)
        self.bmesa12.place(x = 200, y = 85)
        self.bmesa12.config(state='disable', bg = 'red')
        self.bmesa13 = Button(fmenu, text = '13', height = 2, width = 5, command = self.mesa13)
        self.bmesa13.place(x = 0, y = 130)
        self.bmesa13.config(state='disable', bg = 'red')
        self.bmesacv1 = Button(fmenu, text = 'CV1', height = 2, width = 5, command = self.mesac1)
        self.bmesacv1.place(x = 50, y = 130)
        self.bmesacv1.config(state='disable', bg = 'red')
        self.bmesacv2 = Button(fmenu, text = 'CV2', height = 2, width = 5, command = self.mesac2)
        self.bmesacv2.place(x = 100, y = 130)
        self.bmesacv2.config(state='disable', bg = 'red')
        self.bmesacv3 = Button(fmenu, text = 'CV3', height = 2, width = 5, command = self.mesac3)
        self.bmesacv3.place(x = 150, y = 130)
        self.bmesacv3.config(state='disable', bg = 'red')
        self.bmesacv4 = Button(fmenu, text = 'CV4', height = 2, width = 5, command = self.mesac4)
        self.bmesacv4.place(x = 200, y = 130)
        self.bmesacv4.config(state='disable', bg = 'red')


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
        self.lcantidad.place(x = 0, y = 400)
        self.lfecha_label.place(x = 500, y = 10)
        self.lfecha_actual.place(x = 570, y = 10)
        self.ltotalpesos.place(x = 0, y = 0)
        self.ltotaldolares.place(x = 0, y = 40)
        
        tipo_p = ['EFECTIVO', 'DOLARES', 'TARJETA']
        lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MIGUEL CORONA', 'MANUEL FLORES']
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']

        #Creacion de cajas de texto
        self.ecantidad = ttk.Combobox(frametabla, values = cantidad, width = 3)
        self.emesero = ttk.Combobox(frametabla, values = lista_meseros, width = 30)
        self.emesa = ttk.Combobox(frametabla, value = lista_mesas, width = 10)
        self.etotalpesos = Entry(fcobro, width = 15)
        self.etotaldolares = Entry(fcobro, width = 15)
        self.epago = Entry(fcobro, width = 15)
        self.etipo_pago = ttk.Combobox(fcobro, width = 12, values = tipo_p)
        self.ecambio = Entry(fcobro, width = 15)

        #Posiciones de las cajas de texto
        self.ecantidad.place(x = 55, y = 400)
        self.emesero.place(x = 70, y = 10)
        self.emesa.place(x = 350, y = 13)
        self.etotalpesos.place(x = 120, y = 0)
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.place(x = 120, y = 43)
        self.etotaldolares.config(state = 'disable')
        self.lpago.place(x = 0, y = 80)
        self.ltipo_pago.place(x = 0, y = 120)
        self.lcambio.place(x = 0, y = 160)
        self.epago.place(x = 120, y = 83)
        self.epago.config(state = 'disable')
        self.etipo_pago.place(x = 120, y = 123)
        self.etipo_pago.config(state = 'disable')
        self.ecambio.place(x = 120, y = 163)
        self.ecambio.config(state = 'disable')
        
        

        #Notebook
        pmenu = Notebook(frametabla, height = 300, width = 750)
        pmenu.place(x = 0, y = 35)
        frame1 = Frame(pmenu, height = 138, width = 750)
        frame2 = Frame(pmenu, height = 138, width = 750)
        frame3 = Frame(pmenu, height = 138, width = 750)
        frame4 = Frame(pmenu, height = 138, width = 750)
        frame5 = Frame(pmenu, height = 138, width = 750)
        frame6 = Frame(pmenu, height = 138, width = 750)
        frame7 = Frame(pmenu, height = 138, width = 750)
        frame8 = Frame(pmenu, height = 138, width = 750)
        frame9 = Frame(pmenu, height = 138, width = 750)
        frame10 = Frame(pmenu, height = 138, width = 750)
        frame11 = Frame(pmenu, height = 138, width = 750)
        frame12 = Frame(pmenu, height = 138, width = 750)
        frame13 = Frame(pmenu, height = 138, width = 750)
        frame1.place(x = 0, y = 35)
        frame2.place(x = 0, y = 35)
        frame3.place(x = 0, y = 35)
        frame4.place(x = 0, y = 35)
        frame5.place(x = 0, y = 35)
        frame6.place(x = 0, y = 35)
        frame7.place(x = 0, y = 35)
        frame8.place(x = 0, y = 35)
        frame9.place(x = 0, y = 35)
        frame10.place(x = 0, y = 35)
        frame11.place(x = 0, y = 35)
        frame12.place(x = 0, y = 35)
        frame13.place(x = 0, y = 35)
        pmenu.add(frame1, text='Comida')
        pmenu.add(frame2, text='Bebida S/A')
        pmenu.add(frame3, text='Cervezas')
        pmenu.add(frame4, text='Cockteleria')
        pmenu.add(frame5, text='BVTINTO')
        pmenu.add(frame6, text='BVBLANCO')
        pmenu.add(frame7, text='BVBROSADO')
        pmenu.add(frame8, text='RON')
        pmenu.add(frame9, text='VODKA')
        pmenu.add(frame10, text='WHISKY')
        pmenu.add(frame11, text='TEQUILA')
        pmenu.add(frame12, text='MEZCAL')
        pmenu.add(frame13, text='DIJESTIVOS')

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
        
        mprincipal = Menu(window)
        minicio = Menu(mprincipal, tearoff = 0)
        minicio.add_command(label = 'Salir', command = window.destroy)
        mprincipal.add_cascade(label = 'Inicio', menu = minicio)

        corte = Menu(mprincipal, tearoff = 0)
        corte.add_command(label = 'Corte del dia', command = ventana)
        corte.add_command(label = 'Estadisticas', command = ventana2)
        mprincipal.add_cascade(label = 'Corte', menu = corte)
        window.config(menu = mprincipal)

        #Creacion de boton acciones
        self.bguardar = ttk.Button(frametabla, text = 'Total', command = self.sumartotales)
        self.bguardar.place(x = 445, y = 400)
        self.bguardar.config(state = 'disable')
        self.blimpiar = ttk.Button(frametabla, text = 'Limpiar Ticket', command = self.Limpiarticket)
        self.blimpiar.place(x = 180, y = 400)
        self.cproducto = ttk.Button(frametabla, text = 'Cancelar Producto', command = self.eliminarfila)
        self.cproducto.place(x = 0, y = 425)
        self.cerrart = ttk.Button(frametabla, text = 'Guardar Ticket', command = self.generart)
        self.cerrart.place(x = 265, y = 400)
        self.quest = ttk.Button(frametabla, text = 'Cobrar Ticket', command = self.preguntar)
        self.quest.place(x = 355, y = 400)
        self.cobrart = ttk.Button(fcobro, text = 'Cobrar', command = self.cobrarticket)
        self.cobrart.place(x = 0, y = 200)
        self.cobrart.config(state = 'disable')
        self.cerrarmesa = ttk.Button(fcobro, text = 'Liberar Mesa', command = self.liberarmesa)
        self.cerrarmesa.place(x = 100, y = 200)
        self.cerrarmesa.config(state = 'disable')
        self.nuevot = ttk.Button(frametabla, text = 'Nuevo Ticket', command = self.nuevo_ticket)
        self.nuevot.place(x = 100, y = 400)
