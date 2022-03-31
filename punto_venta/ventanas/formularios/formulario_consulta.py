import mysql.connector
from tkinter import *
from tkinter import ttk
from repositorio_conexion import RepositorioConexionSQLite


class FormularioCosultar(RepositorioConexionSQLite):

    def consultar(self):
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select * from tabla_tickets"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.tree.insert('', END, text = row[0], values = (row[1], row[2], row[3], row[4], row[5]))

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()


    def opcionbusqueda(self):
        pass

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
        proveedor = StringVar()
        total = IntVar()
        tipo = StringVar()

        self.tree = ttk.Treeview(v, height=15, columns=('#0', '#1', '#2', '#3'))
        self.tree.place(x = 0, y = 40)
        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'FOLIO', anchor=CENTER)
        self.tree.heading('#1', text = 'MESERO', anchor=CENTER)
        self.tree.column('#2', width = 100)
        self.tree.heading('#2', text = 'MESA', anchor=CENTER)
        self.tree.column('#3', width = 100)
        self.tree.heading('#3', text = 'TOTAL', anchor=CENTER)
        self.tree.column('#4', width = 100)
        self.tree.heading('#4', text = 'TIPO DE PAGO', anchor=CENTER)
        
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
        
        
        #lista_busqueda = ['FECHA', 'MESERO']
        Label(v, text = 'Elije un tipo de busqueda:', font = ('Arial', 12, 'bold')).place(x = 0, y = 10)
        Label(v, text = 'Ingresa tus gastos', font = ('Arial', 12, 'bold')).place(x = 150, y = 370)
        Label(v, text = 'FECHA', font = ('Arial', 10, 'bold')).place(x = 455, y = 400)
        Label(v, text = 'PROVEEDOR', font = ('Arial', 10, 'bold')).place(x = 455, y = 450)
        Label(v, text = 'TOTAL', font = ('Arial', 10, 'bold')).place(x = 455, y = 500)
        Label(v, text = 'EFECTIVO', font = ('Arial', 10, 'bold')).place(x = 10, y = 640)
        Label(v, text = 'TARJETA', font = ('Arial', 10, 'bold')).place(x = 90, y = 640)
        Label(v, text = 'GASTOS', font = ('Arial', 10, 'bold')).place(x = 170, y = 640)
        Label(v, text = 'TOTAL BRUTO', font = ('Arial', 10, 'bold')).place(x = 250, y = 640)
        Label(v, text = 'IVA', font = ('Arial', 10, 'bold')).place(x = 390, y = 640)
        Label(v, text = 'TOTAL NETO', font = ('Arial', 10, 'bold')).place(x = 450, y = 640)
        self.efecha = Entry(v, textvariable = fecha, width = 14)
        self.efecha.place(x = 455, y = 425)
        self.eproveedor = Entry(v, textvariable = proveedor, width = 14)
        self.eproveedor.place(x = 455, y = 475)
        self.etotal = Entry(v, textvariable = total, width = 14)
        self.etotal.place(x = 455, y = 525)
        self.etipop = Entry(v, textvariable = tipo, width = 14)
        self.etipop.place(x = 455, y = 575)
        bCorte = ttk.Button(v, text = 'Consultar', command = self.consultar)
        bCorte.place(x = 470, y = 10)
        ttk.Button(v, text = 'Agregar', command = self.gastos).place(x = 465, y = 600)
        


vcorte = Tk()
vcorte.title('Corte Diario')
vcorte.geometry('550x750')
vcorte.resizable(width = False, height = False)
form = FormularioCosultar(vcorte)


vcorte.mainloop()
