from tkinter import *
from tkinter import ttk, messagebox
from formularios.formulario_estadistica import ventana2
from formularios.botones.botonesmenu import BonotonesMenu
import datetime
from tkinter.ttk import Notebook
import dominio.controlador.controlador_flujo as controlador
from dominio.tickets import Tickets, Tickets2
from formularios.formulario_consulta import ventana
from formularios.formulario_agregar_producto import FormularioAgregarProducto
from formularios.formulario_inventario import FormularioInventario


class FormularioTickets(BonotonesMenu):

    def construir(self):
        error = controlador.construir1()
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
        
        error = controlador.construir4()
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
        
        if (float(self.epago.get()) < float(self.etotalpesos.get())):
            messagebox.showwarning(message = f'La cantidad {self.epago.get()} es menor a la cantidad a cobrar, ingrese una cantidad valida')
            self.epago.delete(0, END)
        elif (len(self.etipo_pago.get()) < 1):
            messagebox.showwarning(message = 'Falta capturar el metodo de pago')
        else:
            cobro = float(self.epago.get()) - float(self.etotalpesos.get())
            self.ecambio.delete(0, END)
            self.ecambio.insert(END, cobro)

            afectados =controlador.insertar_tickets(t)
            if(afectados == 0):
                messagebox.showerror(message=f"Error al guardar verifique la clave que no este repetida", title="Error")    
            else :
                messagebox.showinfo(message=f"Guardado con exito {afectados} registro", title="Salvar") 
        
            self.bguardar.config(state = 'disable')
            self.cerrarmesa.config(state = 'normal')
            self.cobrart.config(state = 'disable')
        

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
        
        if self.emesa.get() == '1':
            self.bmesa1.config(state = 'normal', image = self.imagenverde1)
        elif self.emesa.get() == '3':
            self.bmesa3.config(state = 'normal', image = self.imagenverde2)
        elif self.emesa.get() == '5':
            self.bmesa5.config(state = 'normal', image = self.imagenverde5)
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
        elif self.emesa.get() == 'CasaB1':
            self.bmesacb1.config(state = 'normal', bg = 'green')
        elif self.emesa.get() == 'CasaB2':
            self.bmesacb2.config(state = 'normal', bg = 'green')

        self.nuevo_ticket()


    def liberarmesa(self):
    
        afectados = controlador.eliminar_tickets(self.emesa.get())
        if(afectados == 0):
            messagebox.showerror(message=f"Error al eliminar verifique la clave que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Elimino con exito {afectados} registro", title="Eliminar")

        if self.emesa.get() == '1':
            self.bmesa1.config(state = 'disable', image = self.imagenrojo1)
        elif self.emesa.get() == '3':
            self.bmesa3.config(state = 'disable', image = self.imagenrojo2)
        elif self.emesa.get() == '5':
            self.bmesa5.config(state = 'disable', image = self.imagenrojo5)
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
        elif self.emesa.get() == 'CasaB1':
            self.bmesacb1.config(state = 'disable', bg = 'red')
        elif self.emesa.get() == 'CasaB2':
            self.bmesacb2.config(state = 'disable', bg = 'red')

        self.nuevo_ticket()
        
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.config(state = 'disable')
        self.epago.config(state = 'disable')
        self.etipo_pago.config(state = 'disable')
        self.ecambio.config(state = 'disable')
        self.bguardar.config(state = 'disable')
        self.cobrart.config(state = 'disable')
        self.cerrarmesa.config(state = 'disable')
        self.esubtotal.config(state = 'disable')
        self.eiva.config(state = 'disable')
        self.eimprimir.config(state = 'disable')
    

    def eliminarfila(self):
        
        curItem = self.captura.focus()
        fila = self.captura.item(curItem)
        afectados = controlador.eliminar_fila_cobro(fila["values"][0])
        afectados1 = controlador.eliminar_fila_cobro2(fila["values"][0])
        if(afectados == 0 and afectados1 == 0):
            messagebox.showinfo(message = f'Elimino con exito {afectados}{afectados1} registros', title = 'Eliminar')
        else:
            messagebox.showerror(message = 'Error al eliminar verifique la clave no este repetida', title = 'Error')
        self.celiminar.config(state = 'disable')


    def nuevo_ticket(self):

        self.emesero.delete(0, END)
        self.emesa.delete(0, END)
        self.etotalpesos.delete(0, END)
        self.etotaldolares.delete(0, END)
        self.epago.delete(0, END)
        self.etipo_pago.delete(0, END)
        self.ecambio.delete(0, END)
        self.esubtotal.delete(0, END)
        self.eiva.delete(0, END)
        self.enombre_product.delete(0, END)
        self.eprecio_unit.delete(0, END)
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
        self.esubtotal.config(state = 'disable')
        self.eiva.config(state = 'disable')
        self.eimprimir.config(state = 'disable')


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
            sumadolares = float(suma // 18)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)
        subtotal = float(suma / 1.19)
        iva = float(subtotal * .16)
        self.esubtotal.delete(0, END)
        self.esubtotal.insert(END, subtotal)
        self.eiva.delete(0, END)
        self.eiva.insert(END, iva)

        self.eimprimir.config(state = 'normal')
 
       
    def preguntar(self):
        questions = messagebox.askquestion('Cobrar Ticket', 'Quieres realizar un cobro?')
        if questions == 'yes':
            self.etotalpesos.config(state = 'normal')
            self.etotaldolares.config(state = 'normal')
            self.bguardar.config(state = 'normal')
            self.esubtotal.config(state = 'normal')
            self.eiva.config(state = 'normal')
        else:
            self.etotalpesos.config(state = 'disable')
            self.etotaldolares.config(state = 'disable')
            self.epago.config(state = 'disable')
            self.etipo_pago.config(state = 'disable')
            self.ecambio.config(state = 'disable')
            self.bguardar.config(state = 'disable')
            self.cobrart.config(state = 'disable')
            self.cerrarmesa.config(state = 'disable')
            self.esubtotal.config(state = 'disable')
            self.eiva.config(state = 'disable')


    def altaproducto(self):
        
        FormularioAgregarProducto(self.fproducto2)
 
    
    def inventarioproducto(self):
        
        FormularioInventario(self.frame15)


    def agregar_producto(self):
        
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * float(self.eprecio_unit.get())
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = (str(self.enombre_product.get()), str(self.eprecio_unit.get()), subtotal))
            self.ecantidad.delete(0, END)
            self.enombre_product.delete(0, END)
            self.eprecio_unit.delete(0, END)


    def cancel_pregunta(self):

        if self.clave.get() == 'Jorge1988':
            self.celiminar.config(state = 'normal')
        else:
            messagebox.showinfo(message = 'Clave incorrecta')
        self.ventana_cancel.destroy()


    def questdelete(self):

        question = messagebox.askquestion('Cancelar', 'Vas a eliminar un producto?')
        if question == 'yes':
            self.ventana_cancel = Tk()
            self.ventana_cancel.geometry('150x150+90+90')
            self.ventana_cancel.config(bg = '#FBB03B')
            Label(self.ventana_cancel, text = 'Clave de Cancelación', font = ('Arial', 10, 'bold'), bg = '#FBB03B').place(x = 4, y = 10)
            self.clave = Entry(self.ventana_cancel, width = 20)
            self.clave.config(show = '*')
            self.clave.place(x = 13, y = 40)
            Button(self.ventana_cancel, text = 'Aceptar', width = 15, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cancel_pregunta).place(x = 15, y = 80)
            self.ventana_cancel.mainloop()
        else:    
            self.celiminar.config(state = 'disable')


    def imprimirticket(self):

        questions = messagebox.askquestion('Imprimir', 'Imprimir Ticket?')
        if questions == 'yes':
            c = Conector()
            c.establecerJustificacion(AlineacionCentro)
            c.imagenLocal("C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\LOGO.png")
            c.establecerJustificacion(AlineacionIzquierda)
            c.textoConAcentos("Rodizio Grill\n")
            c.establecerEnfatizado(1)
            c.textoConAcentos("Domicilio: Calle Niños Heroes S/N Col. Centro\n")
            c.establecerEnfatizado(1)
            c.textoConAcentos(f"Mesero: {self.emesero.get()} \n")
            c.establecerEnfatizado(1)
            c.textoConAcentos(f'Mesa: {self.emesa.get()} \n')
            c.establecerEnfatizado(1)
            c.textoConAcentos(f'Fecha: {self.formato_fecha} \n')
            #c.establecerEnfatizado(1)
            #c.textoConAcentos(f'Mesa: {self.hora_formato} \n')
            c.establecerEnfatizado(1)
            c.textoConAcentos(f'Cant  Producto  Precio  Total\n')
            c.establecerEnfatizado(1)
            for i in self.captura.get_children():
                item = self.captura.item(i)
                cant = item['text']
                prod = item['values'][0]
                prec = item['values'][1]
                subt = item['values'][2]
                c.textoConAcentos(f'{cant} {prod} {prec} {subt} \n')
                c.establecerEnfatizado(1)
            c.textoConAcentos(f"SubTotal: {self.esubtotal.get()} \n")
            c.establecerEnfatizado(1)
            c.textoConAcentos(f"IVA: {self.eiva.get()} \n")
            c.establecerEnfatizado(1)
            c.establecerTamanioFuente(2, 2)
            c.textoConAcentos(f'Total Pesos: {self.etotalpesos.get()} \n')
            c.establecerTamanioFuente(1, 1)
            c.textoConAcentos(f'Total DLL: {self.etotaldolares.get()} \n')
            #c.imagenLocal("C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\IMG_5558.jpg")
            c.feed(5)
            c.cortar()
            c.abrirCajon()
            print("Imprimiendo...")
            # Recuerda cambiar por el nombre de tu impresora
            respuesta = c.imprimirEn("TM-T88IV")
            if respuesta == True:
                print("Impresión correcta")
            else:
                print(f"Error. El mensaje es: {respuesta}")
                
        self.epago.config(state = 'normal')
        self.etipo_pago.config(state = 'normal')
        self.ecambio.config(state = 'normal')
        self.cobrart.config(state = 'normal')
        self.cerrarmesa.config(state = 'normal')
        self.bguardar.config(state = 'disable')
        self.cerrarmesa.config(state = 'disable')
        self.eimprimir.config(state = 'disable')
    

    def obtener_hora(self):

        hora = strftime('%H:%M:%S')
        x = self.lhora.winfo_height()
        t = int((x-5)*0.32)
        self.lhora.config(text = hora, font = ('Radioland', t))
        self.lhora.config(font = ('Arial', 12, 'bold'))
        self.lhora.after(10, self.obtener_hora)


    def cambio_total(self):
        
        suma = 0
        sumadolares = 0

        if self.servicio.get() == '10':
            resultado = float(self.etotalpesos.get()) * .1
            suma = float(self.etotalpesos.get()) + resultado
            sumadolares = float(suma // 18)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)
            subtotal = float(suma / 1.19)
            iva = float(subtotal * .16)
            self.esubtotal.delete(0, END)
            self.esubtotal.insert(END, subtotal)
            self.eiva.delete(0, END)
            self.eiva.insert(END, iva)
        elif self.servicio.get() == '15':
            resultado = float(self.etotalpesos.get()) * .1
            suma = float(self.etotalpesos.get()) + resultado
            sumadolares = float(suma // 18)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)
            subtotal = float(suma / 1.19)
            iva = float(subtotal * .16)
            self.esubtotal.delete(0, END)
            self.esubtotal.insert(END, subtotal)
            self.eiva.delete(0, END)
            self.eiva.insert(END, iva)
        elif self.servicio.get() == '20':
            resultado = float(self.etotalpesos.get()) * .1
            suma = float(self.etotalpesos.get()) + resultado
            sumadolares = float(suma // 18)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)
            subtotal = float(suma / 1.19)
            iva = float(subtotal * .16)
            self.esubtotal.delete(0, END)
            self.esubtotal.insert(END, subtotal)
            self.eiva.delete(0, END)
            self.eiva.insert(END, iva)
        self.ventana_secundaria.destroy()


    def agregar_propina(self):

        self.ventana_secundaria = Tk()
        self.ventana_secundaria.geometry('200x150+180+180')

        servicio_sugerido = ['0', '10', '15', '20']
        self.framesecunadio = Frame(self.ventana_secundaria, height = 200, width = 200, bg = '#FBB03B')
        self.framesecunadio.place(x = 0, y = 0)
        Label(self.framesecunadio, text = 'Propina Sugerida', font = ('Arial', 12, 'bold'), bg = '#FBB03B').place(x = 35, y = 15)
        self.servicio = ttk.Combobox(self.framesecunadio, value = servicio_sugerido, width = 15)
        self.servicio.place(x = 50, y = 50)
        Button(self.framesecunadio, text = 'Agregar', width = 15, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cambio_total).place(x = 50, y = 85)
        self.ventana_secundaria.mainloop()


    def __init__(self, window):

        cantidad = ['1' , '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
        
        frametabla = Frame(window)
        frametabla.pack(side = LEFT, fill = BOTH)
        frametabla.config(height = 550, width = 1000)

        self.imagenprincipal = PhotoImage(file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\BACK_FRAME.png')
        Label(frametabla, image = self.imagenprincipal).place(x = 0, y = 0)

        #creacion de la vista de los productos
        self.captura = ttk.Treeview(frametabla, height= 9, columns=('#0', '#1', '#2'))
        self.captura.place(x = 5, y = 460)
        self.captura.column('#0', width = 50)
        self.captura.heading('#0', text = 'Cant', anchor=CENTER)
        self.captura.heading('#1', text = 'Producto', anchor=CENTER)
        self.captura.column('#2', width = 100)
        self.captura.heading('#2', text = 'Precio Unit', anchor=CENTER)
        self.captura.column('#3', width = 100)
        self.captura.heading('#3', text = 'Total', anchor=CENTER)

        #Scrollbar Treeview
        deslizarv = ttk.Scrollbar(frametabla, orient = 'vertical', command = self.captura.yview)
        deslizarv.place(x = 436, y = 461, relheight = 0.3)
        deslizarv.config(command = self.captura.yview)
        self.captura.configure(yscrollcommand = deslizarv.set)
        
        #formato de fecha actual
        fecha_actual = datetime.datetime.now()
        self.formato_fecha = datetime.datetime.strftime(fecha_actual, '%b/%d/%Y')
        #self.hora_formato = datetime.datetime.strftime(fecha_actual, '%H:%M:%S')
        self.dia = strftime('%A')

        if self.dia =='Monday':
            self.dia = 'Lunes'
        elif self.dia =='Tuesday':
            self.dia = 'Martes'
        elif self.dia =='Wednesday':
            self.dia = 'Miercoles'
        elif self.dia =='Thursday':
            self.dia = 'Jueves'
        elif self.dia =='Friday':
            self.dia = 'Viernes'
        elif self.dia =='Saturday':
            self.dia = 'Sábado'
        elif self.dia =='Sunday':
            self.dia = 'Domingo'
        
        fcobro = Frame(window, height = 360, width = 280, bg = 'blue')
        fcobro.place(x = 1000, y = 360)
        Label(fcobro, image = self.imagenprincipal).place(x = 0, y = 0)

        fmenu = Frame(window, height = 360, width = 280, bg = 'red') #Frame de los botones de mesas
        fmenu.place(x = 1000, y = 0)
        Label(fmenu, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(fmenu, text = 'Seleccion de Mesas', font = ('Arial', 12, 'bold'), bg = '#FBB03B').place(x = 75, y = 5)
        self.fproducto2 = Frame(window, height = 310, width = 540, bg = 'red')
        self.fproducto2.place(x = 460, y = 390)
        Label(self.fproducto2, image = self.imagenprincipal).place(x = 0, y = 0)

        #botones de seleccion de mesas de seleccion
        self.imagenrojo1 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\roja_mesa_1.png')
        self.imagenrojo2 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\roja_mesa_3.png')
        self.imagenrojo5 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\roja_mesa_5.png')
        self.imagenverde1 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\MESA_VERDE_1.png')
        self.imagenverde2 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\verde_mesa_3.png')
        self.imagenverde5 = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\verde_mesa_5.png')
        self.bmesa1 = Button(fmenu, height = 37, width = 80, command = self.mesa1)
        self.bmesa1.place(x = 5, y = 30)
        self.bmesa1.config(state='disable', image = self.imagenrojo1)
        self.bmesa3 = Button(fmenu, height = 37, width = 80, command = self.mesa3)
        self.bmesa3.place(x = 98, y = 30)
        self.bmesa3.config(state='disable', image = self.imagenrojo2)
        self.bmesa5 = Button(fmenu, height = 37, width = 80, command = self.mesa5)
        self.bmesa5.place(x = 190, y = 30)
        self.bmesa5.config(state='disable', image = self.imagenrojo5)
        self.bmesa6 = Button(fmenu, text = '6', height = 2, width = 5, command = self.mesa6)
        #self.bmesa6.place(x = 150, y = 40)
        self.bmesa6.config(state='disable', bg = 'red')
        self.bmesa7 = Button(fmenu, text = '7', height = 2, width = 5, command = self.mesa7)
        #self.bmesa7.place(x = 200, y = 40)
        self.bmesa7.config(state='disable', bg = 'red')
        self.bmesa8 = Button(fmenu, text = '8', height = 2, width = 5, command = self.mesa8)
        #self.bmesa8.place(x = 0, y = 85)
        self.bmesa8.config(state='disable', bg = 'red')
        self.bmesa9 = Button(fmenu, text = '9', height = 2, width = 5, command = self.mesa9)
        #self.bmesa9.place(x = 50, y = 85)
        self.bmesa9.config(state='disable', bg = 'red')
        self.bmesa10 = Button(fmenu, text = '10', height = 2, width = 5, command = self.mesa10)
        #self.bmesa10.place(x = 100, y = 85)
        self.bmesa10.config(state='disable', bg = 'red')
        self.bmesa11 = Button(fmenu, text = '11', height = 2, width = 5, command = self.mesa11)
        #self.bmesa11.place(x = 150, y = 85)
        self.bmesa11.config(state='disable', bg = 'red')
        self.bmesa12 = Button(fmenu, text = '12', height = 2, width = 5, command = self.mesa12)
        #self.bmesa12.place(x = 200, y = 85)
        self.bmesa12.config(state='disable', bg = 'red')
        self.bmesa13 = Button(fmenu, text = '13', height = 2, width = 5, command = self.mesa13)
        #self.bmesa13.place(x = 0, y = 130)
        self.bmesa13.config(state='disable', bg = 'red')
        self.bmesacv1 = Button(fmenu, text = 'CV1', height = 2, width = 5, command = self.mesac1)
        #self.bmesacv1.place(x = 50, y = 130)
        self.bmesacv1.config(state='disable', bg = 'red')
        self.bmesacv2 = Button(fmenu, text = 'CV2', height = 2, width = 5, command = self.mesac2)
        #self.bmesacv2.place(x = 100, y = 130)
        self.bmesacv2.config(state='disable', bg = 'red')
        self.bmesacv3 = Button(fmenu, text = 'CV3', height = 2, width = 5, command = self.mesac3)
        #self.bmesacv3.place(x = 150, y = 130)
        self.bmesacv3.config(state='disable', bg = 'red')
        self.bmesacv4 = Button(fmenu, text = 'CV4', height = 2, width = 5, command = self.mesac4)
        #self.bmesacv4.place(x = 200, y = 130)
        self.bmesacv4.config(state='disable', bg = 'red')
        self.bmesacb1 = Button(fmenu, text = 'Casa Bonita 1', height = 2, width = 15, command = self.mesacasab1)
        #self.bmesacb1.place(x = 0, y = 175)
        self.bmesacb1.config(state='disable', bg = 'red')
        self.bmesacb2 = Button(fmenu, text = 'Casa Bonita 2', height = 2, width = 15, command = self.mesacasab2)
        #self.bmesacb2.place(x = 120, y = 175)
        self.bmesacb2.config(state='disable', bg = 'red')

        # Creacion de etiquetas
        self.lmesero = Label(frametabla, text = 'Mesero', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lmesa = Label(frametabla, text = 'Mesa', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lcantidad = Label(frametabla, text = 'Cant', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.ldia = Label(frametabla, text = self.dia, font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.ltotalpesos = Label(fcobro, text = 'Total Pesos', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.ltotaldolares = Label(fcobro, text = 'Total Dolares', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lfecha_actual = Label(window, text = self.formato_fecha, font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lhora = Label(frametabla, font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lpago = Label(fcobro, text = 'Cobrar', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.ltipo_pago = Label(fcobro, text = 'Tipo de Pago', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lcambio = Label(fcobro, text = 'Cambio', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lsubtocal = Label(fcobro, text = 'Subtotal', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.liva = Label(fcobro, text = 'IVA', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        
        
        #Posiciones de Etiquetas
        self.lmesero.place(x = 3, y = 10)
        self.lmesa.place(x = 300, y = 10)
        self.lcantidad.place(x = 470, y = 10)
        self.ldia.place(x = 580, y = 10)
        self.lfecha_actual.place(x = 660, y = 10)
        self.lhora.place(x = 790, y = 10)
        self.lsubtocal.place(x = 3, y = 3)
        self.liva.place(x = 3, y = 40)
        self.ltotalpesos.place(x = 3, y = 80)
        self.ltotaldolares.place(x = 3, y = 120)
        
        tipo_p = ['EFECTIVO', 'DOLARES', 'TARJETA']
        lista_meseros = ['DIEGO HERNANDEZ', 'MIGUEL CORONA', 'MANUEL FLORES']
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2',
                       'Cava3', 'Cava4', 'CasaB1', 'CasaB2']

        #Creacion de cajas de texto
        self.ecantidad = ttk.Combobox(frametabla, values = cantidad, width = 3)
        self.emesero = ttk.Combobox(frametabla, values = lista_meseros, width = 30)
        self.emesa = ttk.Combobox(frametabla, value = lista_mesas, width = 15)
        self.etotalpesos = Entry(fcobro, width = 10)
        self.etotaldolares = Entry(fcobro, width = 10)
        self.epago = Entry(fcobro, width = 10)
        self.etipo_pago = ttk.Combobox(fcobro, width = 7, values = tipo_p)
        self.ecambio = Entry(fcobro, width = 10)
        self.esubtotal = Entry(fcobro, width = 10)
        self.eiva = Entry(fcobro, width = 10)

        #Posiciones de las cajas de texto
        self.ecantidad.place(x = 525, y = 10)
        self.emesero.place(x = 70, y = 10)
        self.emesa.place(x = 350, y = 10)
        self.esubtotal.place(x = 120, y = 3)
        self.esubtotal.config(state = 'disable')
        self.eiva.place(x = 120, y = 37)
        self.eiva.config(state = 'disable')
        self.etotalpesos.place(x = 120, y = 77)
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.place(x = 120, y = 117)
        self.etotaldolares.config(state = 'disable')
        self.lpago.place(x = 3, y = 160)
        self.ltipo_pago.place(x = 3, y = 200)
        self.lcambio.place(x = 3, y = 240)
        self.epago.place(x = 120, y = 157)
        self.epago.config(state = 'disable')
        self.etipo_pago.place(x = 120, y = 197)
        self.etipo_pago.config(state = 'disable')
        self.ecambio.place(x = 120, y = 237)
        self.ecambio.config(state = 'disable')
        
        #Notebook
        pmenu = Notebook(frametabla, height = 300, width = 1000)
        pmenu.place(x = 0, y = 35)
        frame1 = Frame(pmenu, height = 138, width = 900)
        frame2 = Frame(pmenu, height = 138, width = 900)
        frame3 = Frame(pmenu, height = 138, width = 900)
        frame4 = Frame(pmenu, height = 138, width = 900)
        frame5 = Frame(pmenu, height = 138, width = 900)
        frame6 = Frame(pmenu, height = 138, width = 900)
        frame7 = Frame(pmenu, height = 138, width = 900)
        frame8 = Frame(pmenu, height = 138, width = 900)
        frame9 = Frame(pmenu, height = 138, width = 900)
        frame10 = Frame(pmenu, height = 138, width = 900)
        frame11 = Frame(pmenu, height = 138, width = 900)
        frame12 = Frame(pmenu, height = 138, width = 900)
        frame13 = Frame(pmenu, height = 138, width = 900)
        frame14 = Frame(pmenu, height = 138, width = 900)
        self.frame15 = Frame(pmenu, height = 138, width = 900)
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
        frame14.place(x = 0, y = 35)
        self.frame15.place(x = 0, y = 35)
        pmenu.add(frame1, text='COMIDA')
        pmenu.add(frame2, text='BEBIDA S/A')
        pmenu.add(frame3, text='CERVEZAS')
        pmenu.add(frame4, text='COCKTELERIA')
        pmenu.add(frame5, text='BVTINTO')
        pmenu.add(frame6, text='BVTINTO')
        pmenu.add(frame7, text = 'BVBLANCO')
        pmenu.add(frame8, text='BVBROSADO')
        pmenu.add(frame9, text='RON')
        pmenu.add(frame10, text='VODKA')
        pmenu.add(frame11, text='WHISKY')
        pmenu.add(frame12, text='TEQUILA')
        pmenu.add(frame13, text='MEZCAL')
        pmenu.add(frame14, text='DIJESTIVOS')
        pmenu.add(self.frame15, text = 'OTROS')

        Label(frame1, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame2, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame3, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame4, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame5, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame6, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame7, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame8, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame9, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame10, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame11, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame12, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame13, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(frame14, image = self.imagenprincipal).place(x = 0, y = 0)
        Label(self.frame15, image = self.imagenprincipal).place(x = 0, y = 0)


        #creacion de botones
        self.brodizio = Button(frame1, text = 'RODIZIO', height = 5, width = 12, command = self.botonrodizio)
        self.brodizio.config(bg = '#D67B03', font = ('Arial', 9, 'bold'))
        self.brodiziol = Button(frame1, text = 'RODIZIO \n LOCAL', height = 5, width = 12, command = self.botonrodiziol)
        self.brodiziol.config(bg = '#D67B03', font = ('Arial', 9, 'bold'))
        self.brodiziom = Button(frame1, text = 'Rodizio Menor', height = 5, width = 12, command = self.botonrodiziom)
        self.brodiziom.config(bg = '#D67B03', font = ('Arial', 9, 'bold'))
        self.brodiziolm = Button(frame1, text = 'Rodizio \n Local Menor', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonrodizioml)
        self.brodiziotg = Button(frame1, text = 'RodizioToGo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonrodiziotg)
        self.bpicana = Button(frame1, text = 'Picaña', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpicana)
        self.bpicanatg = Button(frame1, text = 'PicañaToGo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpicanatg)
        self.btomahack = Button(frame1, text = 'TOMA HAWK', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botontomahack)
        self.bburguer = Button(frame1, text = 'Burguer', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonburguer)
        self.bburguertg = Button(frame1, text = 'BurguerToGo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonburguertg)
        self.brodiziopass = Button(frame1, text = 'Rodizio \n Passport', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.rodiziopassport)
        self.brodiziocort = Button(frame1, text = 'Rodizio \n cortesia', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.rodiziocortesia)
        self.rodiziodesc = Button(frame1, text = 'Rodizio \n 20% Desc', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.rodizio20descuento)
        self.postreesp = Button(frame1, text = 'Postre \n Cumpleaños', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpostre)
        self.bbotagua = Button(frame2, text = 'Agua Panna', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'),command = self.botonaguap)
        self.btopochico = Button(frame2, text = 'Topochico', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'),command = self.botontopoc)
        self.blimonada = Button(frame2, text = 'Limonada', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'),command = self.botonlimonada)
        self.bnaranjada = Button(frame2, text = 'Naranjada', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonnaranjada)
        self.bcoca = Button(frame2, text = 'Coca Cola', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botoncoca)
        self.bcocad = Button(frame2, text = 'Coca Dieta', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botoncocad)
        self.bsprite = Button(frame2, text = 'Sprite', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonsprite)
        self.bfresca = Button(frame2, text = 'Fresca', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonfresca)
        self.bmundet = Button(frame2, text = 'Mundet', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonmundet)
        self.bpinada = Button(frame2, text = 'Piñada', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpinada)
        self.bmojv = Button(frame2, text = 'Mojito S/A', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonmojitov)
        self.bpituv = Button(frame2, text = 'Caipiriña S/A', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpituv)
        self.pacifico = Button(frame3, text = 'Pacifico', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpacifico)
        self.pacificos = Button(frame3, text = 'Ultra', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonultra)
        self.pacificol = Button(frame3, text = 'Pacifico Ligth', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonpacificol)
        self.corona = Button(frame3, text = 'Corona', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botoncorona)
        self.victoria = Button(frame3, text = 'Victoria', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonvictoria)
        self.artesanal = Button(frame3, text = 'Artesanal', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonartesanal)
        self.negram = Button(frame3, text = 'Negra Modelo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonegramodelo)
        self.bmezcalitaj = Button(frame4, text = 'Mezcalita \n Jamaica', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonmezcalitaj)
        self.mojito = Button(frame4, text = 'Mojito', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botonmojito)
        self.bpitu = Button(frame4, text = 'Caipiriña', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botoncaipirina)
        self.bcvino = Button(frame5, text = 'Copa de Vino', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botoncopadevino)
        self.santam = Button(frame7, text = 'San Martino', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.bsanmartino)
        self.mojitovt = Button(frame4, text = 'Mojito Tinto', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mojitotinto)
        self.mojitos = Button(frame4, text = 'Mojito Frutas', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mojitosabores)
        self.guanagin = Button(frame4, text = 'Guanabana \n Gin', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.guanabanagin)
        self.coffe = Button(frame4, text = 'Coffe Martini', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.martinicoffe)
        self.mezcamara = Button(frame4, text = 'Mezcalita \n Maracuya', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mezcalitamaracuya)
        self.mezcamango = Button(frame4, text = 'Mezcalita \n Mango', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mezcalitamango)
        self.mezcagua = Button(frame4, text = 'Mezcalita \n Guanabana', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mezcalitaguanabana)
        self.mezcatrad = Button(frame4, text = 'Mezcalita', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mezcalitatradicional)
        self.margatrad = Button(frame4, text = 'Margarita', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.margaritatradicional)
        self.margamara = Button(frame4, text = 'Margarita \n Maracuya', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.margaritamaracuya)
        self.margamango = Button(frame4, text = 'Margarita \n Mango', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.margaritamango)
        self.margaguana = Button(frame4, text = 'Margarita \n Guanabana', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.margaritaguanabana)
        self.margacadi = Button(frame4, text = 'Margarita \n Cadillac', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.margaritacadillac)
        self.pitumara = Button(frame4, text = 'Caipiriña \n Maracuya', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.pitumaracuya)
        self.pituman = Button(frame4, text = 'Caipiriña \n Mango', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.pitumango)
        self.pituguaba = Button(frame4, text = 'Caipiriña \n Guanabana', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.pituguanabana)
        self.negro = Button(frame4, text = 'Negroni', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.negroni)
        self.ginto = Button(frame4, text = 'Gin Tonic', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.gintonic)
        self.oldf = Button(frame4, text = 'Old Fashion', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.oldfashion)
        self.cleritinto = Button(frame4, text = 'Clericot', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.clericottinto)
        self.clerirosa = Button(frame4, text = 'Clericot Rosado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.clericotrosado)
        self.cleriblu = Button(frame4, text = 'Clericot \n Blue Berry', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.clericotblueberry)
        self.gavilan = Button(frame4, text = 'Gavilan Reyes', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.gavilan_reyes)
        self.sangriaa = Button(frame4, text = 'Sangria', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.sangria)
        self.pinac = Button(frame4, text = 'Piña Colada', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.pina_colada)
        self.cvrosado = Button(frame8, text = 'Copa de Vino \n Rosado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.coparosado)
        self.cvblanco = Button(frame7, text = 'Copa de Vino \n Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.copablanco)
        self.cmaderocs = Button(frame5, text = 'Casa Madero \n CAB/SAU', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.casamadero)
        self.cmadero_3v = Button(frame5, text = 'Casa Madero \n 3V', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.casamadero_3v)
        self.picco = Button(frame5, text = 'Piccolo Blend', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.piccolo)
        self.criosb = Button(frame5, text = 'CRIOS BLEND', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.criosblend)
        self.criosm = Button(frame5, text = 'CRIOS MALBEC', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.criosmalbec)
        self.crioscs = Button(frame5, text = 'CRIOS CAB/SAU', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.crioscab)
        self.marcob = Button(frame5, text = 'Marco Bonfante', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.marcobonfante)
        self.neroa = Button(frame5, text = 'Nero de Avola', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.neroavola)
        self.monsyr = Button(frame6, text = 'Mongrass \n SYRAH', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mongrasssyr)
        self.monble = Button(frame5, text = 'Mongrass \n BLEND', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mongrassblend)
        self.moncab = Button(frame5, text = 'Mongrass \n CAB', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mongrasscab)
        self.decoypn = Button(frame5, text = 'Decoy \n Pinot Noir', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.decoy)
        self.lomacab = Button(frame5, text = 'La Lomita \n CAB/SAU', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.lomita)
        self.casta = Button(frame5, text = 'Casta Cardon', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.castacardon)
        self.harasp = Button(frame5, text = 'Haras de Pirque \n Blend', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.harasdepirque)
        self.harasg = Button(frame5, text = 'Haras de Pirque \n Gran Reserva', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.harasgran)
        self.mini = Button(frame5, text = 'Minimalista \n Malbec', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.minimalista)
        self.dominob = Button(frame5, text = 'Domino', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.domino)
        self.abbo = Button(frame6, text = 'Abbout \n Pinot Noir', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.abbout)
        self.bella = Button(frame5, text = 'Bellareta', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.bellaretta)
        self.carl = Button(frame5, text = 'Carlidge', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.carlidge)
        self.gnarly = Button(frame5, text = 'Gnarlyhead', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.gnarlyhead)
        self.santa = Button(frame5, text = 'Santa Cristina', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.santacristina)
        self.colezione = Button(frame5, text = 'Collezione', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.colezionemolte)
        self.carat = Button(frame5, text = 'Caracter', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.caracter)
        self.tierra = Button(frame5, text = 'Tierra Adentro', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tierraadentro)
        self.misa = Button(frame5, text = 'Misassou', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.misassou)
        self.krug = Button(frame5, text = 'Kruguer', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.kruguer)
        self.carre = Button(frame5, text = 'CARE', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.care)
        self.dluis = Button(frame6, text = 'Don Luis Cetto \n Merlot', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cetto)
        self.calcanto = Button(frame6, text = 'Cal y Canto', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.calycanto)
        self.cigli = Button(frame6, text = 'Cigliano \n Chianti Clasico', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cigliano)
        self.aguanat = Button(frame2, text = 'Bot de Agua \n Natural', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.botagua)
        self.tutto = Button(frame5, text = 'Tutto Bene', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tutto_bene)
        self.bcipressi = Button(frame5, text = 'Borgo Cipressi \n Merlot', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cipressi)
        self.cavac = Button(frame7, text = 'Cava Cordova', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cavacordova)
        self.annie = Button(frame7, text = 'Anni Especial', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.anniespecial)
        self.islan = Button(frame7, text = 'Isla Negra', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.islanegra)
        self.tante = Button(frame7, text = 'Tantehue', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tantehue)
        self.michel = Button(frame7, text = 'Michel Torino', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.micheltorino)
        self.rinco = Button(frame8, text = 'Rincones Rose', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.rincones)
        self.boni = Button(frame8, text = 'Bonina Portugal', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.bonina)
        self.razap = Button(frame8, text = 'Raza Portugal', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.raza)
        self.porta6 = Button(frame8, text = 'Porta 6 Portugal', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.porta)
        self.paaxd = Button(frame8, text = 'Espumoso Paax \n Dulce', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.espumosopaxx)
        self.paaxbr = Button(frame8, text = 'Espumoso Paax \n Brut Rose', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.espumosopaxx_2)
        self.rbarcardi = Button(frame9, text = 'Bacardi Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.ronbaca)
        self.rbarcardiane = Button(frame9, text = 'Bacardi Añejo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.ronbacaane)
        self.rhabana = Button(frame9, text = 'Habana \n Club 7 Años', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.habanaclub)
        self.rflor = Button(frame9, text = 'Flor de Caña \n 12 Años', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.flor_cana)
        self.rmalibu = Button(frame9, text = 'Malibu', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.malibu)
        self.rcapitan = Button(frame9, text = 'Captain Morgan', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.captain)
        self.rzacapa = Button(frame9, text = 'Zacapa \n 23 Años', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.zacapa)
        self.vtitos = Button(frame10, text = 'Titos', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.titos)
        self.vadsolut = Button(frame10, text = 'Adsolut', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.adsolut)
        self.vcitron = Button(frame10, text = 'Adsolut Citron', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.citron)
        self.vpear = Button(frame10, text = 'Adsolut Pear', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.pear)
        self.vmandarin = Button(frame10, text = 'Adsolut Mandarin', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mandarin)
        self.vketel = Button(frame10, text = 'Ketel One', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.ketelone)
        self.vgrey = Button(frame10, text = 'Grey Goose', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.greygoose)
        self.vsmirnoff = Button(frame10, text = 'Smirnoff', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.smirnoff)
        self.wroyal = Button(frame11, text = 'Crown Royal', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.crown)
        self.wred = Button(frame11, text = 'Red Label', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.red_label)
        self.wblack = Button(frame11, text = 'Black Label', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.black_label)
        self.wmaker = Button(frame11, text = 'Makers Mark', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.makers_mark)
        self.wjack = Button(frame11, text = 'Jack Daniels', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.jack_daniel)
        self.wjim = Button(frame11, text = 'Jim Beam', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.jim_beam)
        self.wwood = Button(frame11, text = 'Woodford', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.woodford)
        self.wmaca = Button(frame11, text = 'Macallan \n 12 Años', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.macallan)
        self.wsanto = Button(frame11, text = 'Santori', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.santori)
        self.tjimadorr = Button(frame12, text = 'Jimador \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.jimador_reposado)
        self.tjimadorb = Button(frame12, text = 'Jimador \n Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.jimador_blanco)
        self.thornitos = Button(frame12, text = 'Hornitos', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.hornitos_reposado)
        self.tblack = Button(frame12, text = 'Hornitos \n Black Barrel', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.blackbarrel)
        self.tcasa = Button(frame12, text = 'Tequila \n de la Casa', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tequila_casa)
        self.ttradicionalb = Button(frame12, text = 'Tradicional \n Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tradicional_blanco)
        self.ttradicionalr = Button(frame12, text = 'Tradicional \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tradicional_reposado)
        self.tcentenario = Button(frame12, text = 'Centenario', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.centenario_anejo)
        self.tanejo1800 = Button(frame12, text = '1800 Añejo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.anejo_1800)
        self.tcristalino1800 = Button(frame12, text = '1800 \n Cristalino', height = 5, bg = '#D67B03', font = ('Arial', 9, 'bold'), width = 12, command = self.cristalino_1800)
        self.tmilenio1800 = Button(frame12, text = '1800 \n Milenio', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.milenio_1800)
        self.therradurar = Button(frame12, text = 'Herradura \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.herradura_reposado)
        self.therraduraa = Button(frame12, text = 'Herradura \n Añejo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.herradura_anejo)
        self.tcazadores = Button(frame12, text = 'Cazadores', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cazadores)
        self.tcazadoresa = Button(frame12, text = 'Cazadores \n Añejo', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cazadores_anejo)
        self.tdonjuliob = Button(frame12, text = 'Don Julio \n Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.don_julio_blanco)
        self.tdonjulior = Button(frame12, text = 'Don Julio \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.don_julio_reposado)
        self.tdonjulio70 = Button(frame12, text = 'Don Julio 70', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.don_julio_70)
        self.tdonjulio1942 = Button(frame12, text = 'Don Julio 1942', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.don_julio_1942)
        self.tcodigo = Button(frame12, text = 'Codigo \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.codigo_reposado)
        self.tvirey = Button(frame12, text = 'Vireyes \n Reposado', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.vireyes)
        self.ttresg = Button(frame12, text = 'Tres \n Generaciones', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.tres_generaciones)
        self.treysol = Button(frame12, text = 'Rey Sol', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.rey_sol)
        self.tcasadrag = Button(frame12, text = 'Casa Dragones', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.casa_dragones)
        self.tcasablanco = Button(frame12, text = 'Casa Dragones \n Blanco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.casa_dragones_blanco)
        self.tseleccion = Button(frame12, text = 'Seleccion \n Suprema', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.seleccion_suprema)
        self.tloco = Button(frame12, text = 'Loco', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.loco_blanco)
        self.tdobel = Button(frame12, text = 'Maestro Dobel \n Cristalino', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.maestro_dobel)
        self.tclase = Button(frame12, text = 'Clase Azul', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.clase_azul)
        self.mconejos = Button(frame13, text = '400 Conejos', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.cuatroconejos)
        self.msuceso = Button(frame13, text = 'Buen Suceso', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.buensuceso)
        self.maleron = Button(frame13, text = 'Aleron', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.aleron)
        self.mmitre = Button(frame13, text = 'Mitre', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.mitre)
        self.mcasa = Button(frame13, text = 'Mezcal \n de la Casa', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.casamezcal)
        self.dkalhua = Button(frame14, text = 'Kalhua', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.kalua)
        self.dlicor = Button(frame14, text = 'Licor 43', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.licor_43)
        self.dbaileys = Button(frame14, text = 'Baileys', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.baileys)
        self.ddisarono = Button(frame14, text = 'Disarono', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.disarono)
        self.dzambuca = Button(frame14, text = 'Zambuca', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.zambuca)
        self.dnegro = Button(frame14, text = 'Zambuca Negro', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.zambuca_negro)
        self.dgrand = Button(frame14, text = 'Grand Marnier', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.grandmarnier)
        self.dfrangelico = Button(frame14, text = 'Frangelico', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.frangelico)
        self.dcour = Button(frame14, text = 'Courvusier VS', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.courvusier)
        self.dazteca = Button(frame14, text = 'Azteca', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.azteca)
        self.dchichon = Button(frame14, text = 'Chichon', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.chichon)
        self.dsouth = Button(frame14, text = 'Souther Comfort', height = 5, width = 12, bg = '#D67B03', font = ('Arial', 9, 'bold'), command = self.south)

        #Posiciones de botones del menu
        self.brodizio.place(x = 0, y = 3)
        self.brodiziol.place(x = 100, y = 3)
        self.brodiziom.place(x = 200, y = 3)
        self.brodiziolm.place(x = 300, y = 3)
        self.brodiziotg.place(x = 400, y = 3)
        self.bpicana.place(x = 500, y = 3)
        self.bpicanatg.place(x = 600, y = 3)
        self.btomahack.place(x = 700, y = 3)
        self.bburguer.place(x = 800, y = 3)
        self.bburguertg.place(x = 0, y = 93)
        self.brodiziopass.place(x = 100, y = 93)
        self.brodiziocort.place(x = 200, y = 93)
        self.rodiziodesc.place(x = 300, y = 93)
        self.postreesp.place(x = 400, y = 93)
        self.bbotagua.place(x = 0, y = 3)
        self.aguanat.place(x = 100, y = 3)
        self.btopochico.place(x = 200, y = 3)
        self.blimonada.place(x = 300, y = 3)
        self.bnaranjada.place(x = 400, y = 3)
        self.bcoca.place(x = 500, y = 3)
        self.bcocad.place(x = 600, y = 3)
        self.bsprite.place(x = 700, y = 3)
        self.bfresca.place(x = 800, y = 3)
        self.bmundet.place(x = 0, y = 93)
        self.bpinada.place(x = 100, y = 93)
        self.bmojv.place(x = 200, y = 93)
        self.bpituv.place(x = 300, y = 93)
        self.pacifico.place(x = 0, y = 3)
        self.pacificos.place(x = 100, y = 3)
        self.pacificol.place(x = 200, y = 3)
        self.corona.place(x = 300, y = 3)
        self.victoria.place(x = 400, y = 3)
        self.artesanal.place(x = 500, y = 3)
        self.negram.place(x = 600, y = 3)
        self.bmezcalitaj.place(x = 0, y = 3)
        self.bpitu.place(x = 100, y = 3)
        self.mojito.place(x = 200, y = 3)
        self.mojitovt.place(x = 300, y = 3)
        self.mojitos.place(x = 400, y = 3)
        self.mezcamara.place(x = 500, y = 3)
        self.mezcamango.place(x = 600, y = 3)
        self.mezcagua.place(x = 700, y = 3)
        self.mezcatrad.place(x = 800, y = 3)
        self.margatrad.place(x = 0, y = 93)
        self.margamara.place(x = 100, y = 93)
        self.margamango.place(x = 200, y = 93)
        self.margaguana.place(x = 300, y = 93)
        self.margacadi.place(x = 400, y = 93)
        self.pitumara.place(x = 500, y = 93)
        self.pituman.place(x = 600, y = 93)
        self.pituguaba.place(x = 700, y = 93)
        self.negro.place(x = 800, y = 93)
        self.ginto.place(x = 0, y = 183)
        self.oldf.place(x = 100, y = 183)
        self.cleritinto.place(x = 200, y = 183)
        self.clerirosa.place(x = 300, y = 183)
        self.cleriblu.place(x = 400, y = 183)
        self.gavilan.place(x = 500, y = 183)
        self.sangriaa.place(x = 600, y = 183)
        self.pinac.place(x = 700, y = 183)
        self.bcvino.place(x = 0, y = 3)
        self.cmaderocs.place(x = 100, y = 3)
        self.cmadero_3v.place(x = 200, y = 3)
        self.picco.place(x = 300, y = 3)
        self.criosb.place(x = 400, y = 3)
        self.criosm.place(x = 500, y = 3)
        self.crioscs.place(x = 600, y = 3)
        self.marcob.place(x = 700, y = 3)
        self.neroa.place(x = 800, y = 3)
        self.monsyr.place(x = 300, y = 3)
        self.monble.place(x = 0, y = 93)
        self.moncab.place(x = 100, y = 93)
        self.decoypn.place(x = 200, y = 93)
        self.lomacab.place(x = 300, y = 93)
        self.casta.place(x = 400, y = 93)
        self.harasg.place(x = 500, y = 93)
        self.harasp.place(x = 600, y = 93)
        self.mini.place(x = 700, y = 93)
        self.dominob.place(x = 800, y = 93)
        self.abbo.place(x = 400, y = 3)
        self.bella.place(x = 0, y = 183)
        self.carl.place(x = 100, y = 183)
        self.gnarly.place(x = 200, y = 183)
        self.colezione.place(x = 300, y = 183)
        self.carat.place(x = 400, y = 183)
        self.tierra.place(x = 500, y = 183)
        self.misa.place(x = 600, y = 183)
        self.krug.place(x = 700, y = 183)
        self.carre.place(x = 800, y = 183)
        self.dluis.place(x = 0, y = 3)
        self.calcanto.place(x = 100, y = 3)
        self.cigli.place(x = 200, y = 3)
        self.tutto.place(x = 900, y = 3)
        self.bcipressi.place(x = 900, y = 93)
        self.cvblanco.place(x = 0, y = 3)
        self.santam.place(x = 100, y = 3)
        self.cavac.place(x = 200, y = 3)
        self.annie.place(x = 300, y = 3)
        self.islan.place(x = 400, y = 3)
        self.tante.place(x = 500, y = 3)
        self.michel.place(x = 600, y = 3)
        self.cvrosado.place(x = 0, y = 3)
        self.rinco.place(x = 100, y = 3)
        self.boni.place(x = 200, y = 3)
        self.razap.place(x = 300, y = 3)
        self.porta6.place(x = 400, y = 3)
        self.paaxd.place(x = 500, y = 3)
        self.paaxbr.place(x = 600, y = 3)
        self.rbarcardi.place(x = 0, y = 3)
        self.rbarcardiane.place(x = 100, y = 3)
        self.rhabana.place(x = 200, y = 3)
        self.rflor.place(x = 300, y = 3)
        self.rmalibu.place(x = 400, y = 3)
        self.rcapitan.place(x = 500, y = 3)
        self.rzacapa.place(x = 600, y = 3)
        self.vtitos.place(x = 0, y = 3)
        self.vadsolut.place(x = 100, y = 3)
        self.vcitron.place(x = 200, y = 3)
        self.vpear.place(x = 300, y = 3)
        self.vmandarin.place(x = 400, y = 3)
        self.vketel.place(x = 500, y = 3)
        self.vgrey.place(x = 600, y = 3)
        self.vsmirnoff.place(x = 700, y = 3)
        self.wroyal.place(x = 0, y = 3)
        self.wred.place(x = 100, y = 3)
        self.wblack.place(x = 200, y = 3)
        self.wmaker.place(x = 300, y = 3)
        self.wjack.place(x = 400, y = 3)
        self.wjim.place(x = 500, y = 3)
        self.wwood.place(x = 600, y = 3)
        self.wmaca.place(x = 700, y = 3)
        self.wsanto.place(x = 800, y = 3)
        self.tcasa.place(x = 0, y = 3)
        self.tjimadorr.place(x = 100, y = 3)
        self.tjimadorb.place(x = 200, y = 3)
        self.thornitos.place(x = 300, y = 3)
        self.tblack.place(x = 400, y = 3)
        self.ttradicionalb.place(x = 500, y = 3)
        self.ttradicionalr.place(x = 600, y = 3)
        self.tcentenario.place(x = 700, y = 3)
        self.tcazadores.place(x = 800, y = 3)
        self.tcazadoresa.place(x = 700, y = 183)
        self.therradurar.place(x = 0, y = 93)
        self.therraduraa.place(x = 100, y = 93)
        self.tdonjuliob.place(x = 200, y = 93)
        self.tdonjulior.place(x = 300, y = 93)
        self.tdonjulio70.place(x = 400, y = 93)
        self.tcodigo.place(x = 500, y = 93)
        self.tvirey.place(x = 600, y = 93)
        self.ttresg.place(x = 700, y = 93)
        self.treysol.place(x = 800, y = 93)
        self.tcasadrag.place(x = 800, y = 183)
        self.tcasablanco.place(x = 0, y = 183)
        self.tseleccion.place(x = 100, y = 183)
        self.tloco.place(x = 200, y = 183)
        self.tdobel.place(x = 300, y = 183)
        self.tanejo1800.place(x = 400, y = 183)
        self.tcristalino1800.place(x = 500, y = 183)
        self.tmilenio1800.place(x = 600, y = 183)
        self.tclase.place(x = 900, y = 3)
        self.tdonjulio1942.place(x = 900, y = 93)
        self.mconejos.place(x = 0, y = 3)
        self.msuceso.place(x = 100, y = 3)
        self.maleron.place(x = 200, y = 3)
        self.mmitre.place(x = 300, y = 3)
        self.mcasa.place(x = 400, y = 3)
        self.dkalhua.place(x = 0, y = 3)
        self.dlicor.place(x = 100, y = 3)
        self.dbaileys.place(x = 200, y = 3)
        self.ddisarono.place(x = 300, y = 3)
        self.dzambuca.place(x = 400, y = 3)
        self.dnegro.place(x = 500, y = 3)
        self.dgrand.place(x = 600, y = 3)
        self.dfrangelico.place(x = 700, y = 3)
        self.dcour.place(x = 800, y = 3)
        self.dazteca.place(x = 0, y = 93)
        self.dchichon.place(x = 100, y = 93)
        self.dsouth.place(x = 200, y = 93)

        mprincipal = Menu(window)
        minicio = Menu(mprincipal, tearoff = 0)
        minicio.add_command(label = 'Salir', command = window.destroy)
        minicio.add_command(label = 'Construir Tabla', command = self.construir)
        mprincipal.add_cascade(label = 'Inicio', menu = minicio)

        corte = Menu(mprincipal, tearoff = 0)
        corte.add_command(label = 'Corte del dia', command = ventana)
        corte.add_command(label = 'Estadisticas')
        mprincipal.add_cascade(label = 'Corte', menu = corte)

        servicios = Menu(mprincipal,tearoff = 0)
        servicios.add_command(label = 'Add Propina', command = self.agregar_propina)
        servicios.add_command(label = 'Descuento')
        mprincipal.add_cascade(label = 'Servicios Extras', menu = servicios)
        window.config(menu = mprincipal)

        self.lname_product = Label(self.frame15, text = 'Producto', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.lprice_unit = Label(self.frame15, text = 'Precio Uni.', font = ('Arial', 12, 'bold'), bg = '#FBB03B')
        self.enombre_product = Entry(self.frame15, width = 15)
        self.eprecio_unit = Entry(self.frame15, width = 15)

        self.lname_product.place(x = 5, y = 270)
        self.lprice_unit.place(x = 185, y = 270)
        self.enombre_product.place(x = 85, y = 270)
        self.eprecio_unit.place(x = 280, y = 270)

        #Creacion de boton acciones
        self.imagencaja_registradora = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\CajaRegistradora.png')
        self.imagenSuma = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\Signo_Suma.png')
        self.bguardar = Button(fcobro, image = self.imagenSuma, height = 70, width = 70, command = self.sumartotales)
        self.bguardar.place(x = 200, y = 90)
        self.bguardar.config(state = 'disable')
        self.imagenLimpiar = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\LimpiarFila.png')
        self.blimpiar = Button(frametabla, image = self.imagenLimpiar, height = 50, width = 145, command = self.Limpiarticket)
        self.blimpiar.place(x = 160, y = 365)
        self.cproducto = Button(frametabla, text = 'Cancelar Producto', width = 62, command = self.questdelete)
        self.cproducto.config(bg = '#FBB03B', font = ('Arial', 8, 'bold'), fg = 'blue')
        self.cproducto.place(x = 5, y = 423)
        self.imagenEliminar = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\Eliminar.png')
        self.celiminar = Button(frametabla, image = self.imagenEliminar, height = 50, width = 60, command = self.eliminarfila)
        self.celiminar.config(state = 'disable')
        self.celiminar.place(x = 385, y = 365)
        self.imagenAgregar = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\Agregar.png')
        self.cerrart = Button(frametabla, image = self.imagenAgregar, height = 50, width = 60, command = self.generart)
        self.cerrart.place(x = 315, y = 365)
        self.quest = Button(fcobro, image = self.imagencaja_registradora, height = 70, width = 70, command = self.preguntar)
        self.quest.place(x = 200, y = 3)
        self.imagenpagar = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\Billetes.png')
        self.cobrart = Button(fcobro, image = self.imagenpagar, height = 40, width = 130, command = self.cobrarticket)
        self.cobrart.place(x = 5, y = 262)
        self.cobrart.config(state = 'disable')
        self.imagenLiberar_mesa = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\bloquearmesa.png')
        self.cerrarmesa = Button(fcobro, image = self.imagenLiberar_mesa, height = 40, width = 130, command = self.liberarmesa)
        self.cerrarmesa.place(x = 142, y = 262)
        self.cerrarmesa.config(state = 'disable')
        self.imagenNuevo_Ticket = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\imagenticket.png')
        self.nuevot = Button(frametabla, image = self.imagenNuevo_Ticket, height = 50, width = 145, command = self.nuevo_ticket)
        self.nuevot.place(x = 5, y = 365)
        self.alta_producto = ttk.Button(window, text = 'Alta Producto', width = 43)
        self.alta_producto.place(x = 460, y = 363)
        self.binventario = ttk.Button(window, text = 'Inventario Producto', width = 43)
        self.binventario.place(x = 730, y = 363)
        self.palomitaimagen = PhotoImage(file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\palomita.png')
        self.aproducto = ttk.Button(self.frame15, text = 'Agregar', width = 10, command = self.agregar_producto)
        self.aproducto.place(x = 380, y = 265)
        self.aproducto.config(image = self.palomitaimagen)
        self.imagenimpresora = PhotoImage( file = 'C:\\Users\\cicat\\OneDrive\\Escritorio\\jorge2\\puntoventa\\ventanas_punto_de_venta\\imagenes\\impresora.png')
        self.eimprimir = Button(fcobro, image = self.imagenimpresora, height = 70, width = 70, command = self.imprimirticket)
        self.eimprimir.config(state = 'disable')
        self.eimprimir.place(x = 200, y = 177)
        self.obtener_hora()
