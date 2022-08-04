import mysql.connector
from tkinter import *
from tkinter import ttk
from formularios.repositorio_conexion import RepositorioConexionSQLite


class FormularioCosultar(RepositorioConexionSQLite):

    def consultar(self):
        self.limpiar()
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            #if self.tipobus.get() == 'TODOS':
            #    sql_select_query = "select * from tabla_venta_diaria"
            #    cursor = self.connection.cursor()
            #    cursor.execute(sql_select_query)            
            #    records = cursor.fetchall()
            #    for row in records:
            #        self.tree.insert('', END, text = row[0], values = (row[1], row[2], row[3], row[4], row[5]))

            sql_select_query = "select * from tabla_venta_diaria WHERE {} like '{}'".format(self.tipobus.get(), (self.ebusfecha.get() + '%'))
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.tree.insert('', END, text = row[0], values = (row[1], row[2], row[3], row[4], row[5]))

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        


    def sumatotales(self):
        sumbruto = 0
        sumgasto = 0
        resiva = 0
        totalneto = 0
        for i in self.tree.get_children():
            item = self.tree.item(i)
            records = item['values'][3]
            sumbruto += float(records)
            resiva = float(sumbruto // 1.16) * 0.16
            totalneto = float(sumbruto) - float(resiva)
            self.sumabruto.delete(0, END)
            self.sumabruto.insert(END, sumbruto)
            self.sumaiva.delete(0, END)
            self.sumaiva.insert(END, resiva)
            self.sumaneto.delete(0, END)
            self.sumaneto.insert(END, totalneto)
        
        for i in self.treeG.get_children():
            item = self.treeG.item(i)
            records = item['values'][1]
            sumgasto += float(records)
            self.gasto.delete(0, END)
            self.gasto.insert(END, sumgasto)
            

    
    def limpiar(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def gastos(self):

        self.treeG.insert('', END, text = self.efecha.get(), 
                        values = (self.eproveedor.get(), str(self.etotal.get()), self.etipop.get()))
        self.efecha.delete(0, END)
        self.eproveedor.delete(0, END)
        self.etotal.delete(0, END)
        self.etipop.delete(0, END)

    def __init__(self, v):
        super().__init__()

        fecha = StringVar()
        total = IntVar()
        busfecha = StringVar()

        self.tree = ttk.Treeview(v, height=15, columns=('#0', '#1', '#2', '#3', '#4'))
        self.tree.place(x = 0, y = 40)
        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'FOLIO', anchor=CENTER)
        self.tree.column('#1', width = 150)
        self.tree.heading('#1', text = 'MESERO', anchor=CENTER)
        self.tree.column('#2', width = 50)
        self.tree.heading('#2', text = 'MESA', anchor=CENTER)
        self.tree.column('#3', width = 100)
        self.tree.heading('#3', text = 'FECHA', anchor=CENTER)
        self.tree.column('#4', width = 100)
        self.tree.heading('#4', text = 'TOTAL', anchor=CENTER)
        self.tree.column('#5', width = 95)
        self.tree.heading('#5', text = 'TIPO DE PAGO', anchor=CENTER)

        deslizarv = ttk.Scrollbar(v, orient = 'vertical', command = self.tree.yview)
        deslizarv.place(x = 528, y = 65, relheight = 0.4)
        deslizarv.config(command = self.tree.yview)
        self.tree.configure(yscrollcommand = deslizarv.set)
        
        #Treeview gastos
        self.treeG = ttk.Treeview(v, height=10, columns=('#0', '#1', '#2'))
        self.treeG.place(x = 0, y = 400)
        self.treeG.column('#0', width = 100)
        self.treeG.heading('#0', text = 'FECHA', anchor=CENTER)
        self.treeG.column('#1', width = 175)
        self.treeG.heading('#1', text = 'PROVEEDOR', anchor=CENTER)
        self.treeG.column('#2', width = 75)
        self.treeG.heading('#2', text = 'TOTAL', anchor=CENTER)
        self.treeG.column('#3', width = 100)
        self.treeG.heading('#3', text = 'TIPO DE PAGO', anchor=CENTER)

        deslizarv = ttk.Scrollbar(v, orient = 'vertical', command = self.treeG.yview)
        deslizarv.place(x = 434, y = 420, relheight = 0.27)
        deslizarv.config(command = self.treeG.yview)
        self.treeG.configure(yscrollcommand = deslizarv.set)
        
        
        lista_busqueda = ['fecha', 'mesero']
        lista_proveedores = ['CITY CLUB', 'WALMART', 'PALMAS', 'CAR SIN', 'KOWI', 'FRUT LIZ', 'LIZARRAGA', 'EUROPEA', 'COCA COLA', 'AVOCADO', 'OTROS']
        lista_tipo = ['EFECTIVO', 'TARJETA']
        Label(v, text = 'Elije un tipo de busqueda:', font = ('Arial', 12, 'bold')).place(x = 0, y = 10)
        Label(v, text = 'Ingresa tus gastos', font = ('Arial', 12, 'bold')).place(x = 150, y = 370)
        Label(v, text = 'FECHA', font = ('Arial', 10, 'bold')).place(x = 455, y = 400)
        Label(v, text = 'PROVEEDOR', font = ('Arial', 10, 'bold')).place(x = 455, y = 450)
        Label(v, text = 'TOTAL', font = ('Arial', 10, 'bold')).place(x = 455, y = 500)
        Label(v, text = 'TIPO PAGO', font = ('Arial', 10, 'bold')).place(x = 455, y = 550)
        Label(v, text = 'EFECTIVO', font = ('Arial', 10, 'bold')).place(x = 10, y = 640)
        Label(v, text = 'TARJETA', font = ('Arial', 10, 'bold')).place(x = 90, y = 640)
        Label(v, text = 'GASTOS', font = ('Arial', 10, 'bold')).place(x = 170, y = 640)
        Label(v, text = 'TOTAL BRUTO', font = ('Arial', 10, 'bold')).place(x = 250, y = 640)
        Label(v, text = 'IVA', font = ('Arial', 10, 'bold')).place(x = 390, y = 640)
        Label(v, text = 'TOTAL NETO', font = ('Arial', 10, 'bold')).place(x = 450, y = 640)
        self.tipobus = ttk.Combobox(v, width = 15, values = lista_busqueda)
        self.tipobus.place(x = 205, y = 10)
        self.ebusfecha = Entry(v, textvariable = busfecha, width = 15)
        self.ebusfecha.place(x = 335, y = 10)
        self.efecha = Entry(v, textvariable = fecha, width = 14)
        self.efecha.place(x = 455, y = 425)
        self.eproveedor = ttk.Combobox(v, values = lista_proveedores, width = 11)
        self.eproveedor.place(x = 455, y = 475)
        self.etotal = Entry(v, textvariable = total, width = 14)
        self.etotal.place(x = 455, y = 525)
        self.etipop = ttk.Combobox(v, values = lista_tipo, width = 11)
        self.etipop.place(x = 455, y = 575)
        self.sumabruto = Entry(v, width = 15)
        self.sumabruto.place(x = 256, y = 665)
        self.sumaiva = Entry(v, width = 10)
        self.sumaiva.place(x = 373, y = 665)
        self.sumaneto = Entry(v, width = 15)
        self.sumaneto.place(x = 445, y = 665)
        self.gasto = Entry(v, width = 10)
        self.gasto.place(x = 170, y = 665)
        bCorte = ttk.Button(v, text = 'Consultar', command = self.consultar)
        bCorte.place(x = 470, y = 10)
        ttk.Button(v, text = 'Agregar', command = self.gastos).place(x = 465, y = 600)
        ttk.Button(v, text = 'Calcular', command = self.sumatotales).place(x = 0, y = 700)
        

def ventana():
    vcorte = Tk()
    vcorte.title('Corte Diario')
    vcorte.geometry('550x750')
    vcorte.resizable(width = False, height = False)
    form = FormularioCosultar(vcorte)


    vcorte.mainloop()
