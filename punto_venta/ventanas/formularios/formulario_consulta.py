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


    def __init__(self, v):
        super().__init__()

        self.tree = ttk.Treeview(v, height=20, columns=('#0', '#1', '#2', '#3'))
        self.tree.place(x = 0, y = 0)
        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'FOLIO', anchor=CENTER)
        self.tree.heading('#1', text = 'MESERO', anchor=CENTER)
        self.tree.column('#2', width = 100)
        self.tree.heading('#2', text = 'MESA', anchor=CENTER)
        self.tree.column('#3', width = 100)
        self.tree.heading('#3', text = 'TOTAL', anchor=CENTER)
        self.tree.column('#4', width = 100)
        self.tree.heading('#4', text = 'TIPO DE PAGO', anchor=CENTER)

        bCorte = ttk.Button(v, text = 'Corte Diario', command = self.consultar)
        bCorte.place(x = 0, y = 450)
        breporte = ttk.Button(v, text = 'Imprimir Corte')
        lEfectivo = Label(v, text = 'EFECTIVO')
        lTarjeta = Label(v, text = 'TARJETA')
        ltotalventa  = Label(v, text = 'VENTA TOTAL')
        breporte.place(x = 90, y = 450)
        lEfectivo.place(x = 180, y = 450)


vcorte = Tk()
vcorte.title('Corte Diario')
vcorte.geometry('550x700')
vcorte.resizable(width = False, height = False)
form = FormularioCosultar(vcorte)


vcorte.mainloop()
checar = FormularioCosultar()
checar.consultar() 
