import mysql.connector
from tkinter import *
from tkinter import ttk
from repositorio_conexion import RepositorioConexionSQLite
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Estadisticas(RepositorioConexionSQLite):
 
    def graficar(self):
        
        dict_ventas = {
            'Erick': self.sumaerick.get(),
            'Ricardo': self.sumarich.get(),
            'Frank': self.sumafrank.get(),
            'Lino': self.sumalino.get()
        }

        meseros = dict_ventas.keys()
        datos = dict_ventas.values()
        
        figura = plt.Figure(figsize=(6, 6), dpi=100)
        lienzo_figura = FigureCanvasTkAgg(figura)
        lienzo_figura.get_tk_widget().place(x = 570, y = 45)
        ax1 = figura.add_subplot()
        ax1.set_title('Estadistica de Venta')
        if self.combograficos.get() == 'barh':
            ax1.barh(list(meseros), list(datos)) 
            ax1.set_ylabel('Ventas')
            ax1.set_xlabel('Meseros')
        elif self.combograficos.get() == 'bar':
            ax1.bar(meseros, datos) 
            ax1.set_ylabel('Ventas')
            ax1.set_xlabel('Meseros')
        elif self.combograficos.get() == 'plot':
            ax1.plot(meseros, datos) 
            ax1.set_ylabel('Ventas')
            ax1.set_xlabel('Meseros')
        elif self.combograficos.get() == 'scatter':
            ax1.scatter(meseros, datos)
            ax1.set_ylabel('Ventas')
            ax1.set_xlabel('Meseros')
        elif self.combograficos.get() == 'fill_between':
            ax1.fill_between(meseros, datos) 
            ax1.set_ylabel('Ventas')
            ax1.set_xlabel('Meseros')
        elif self.combograficos.get() == 'pie':
            ax1.pie(x = list(datos), labels = list(meseros))


    def consultar(self):
        self.limpiar()
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select * from tabla_tickets WHERE mesero like '{}'".format((self.ebusfecha.get() + '%'))
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.tree.insert('', END, text = row[0], values = (row[1], row[2], row[3], row[4], row[5]))

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()


    def limpiar(self):
            for i in self.tree.get_children():
                self.tree.delete(i)
    
    

    def ventameseros(self):

        ventaerick = 0
        ventarich = 0
        ventafrank = 0
        ventalino = 0
        if self.ebusfecha.get() == 'Erick':
            for i in self.tree.get_children():
                item = self.tree.item(i)
                records = item['values'][3]
                ventaerick += float(records)
                self.sumaerick.delete(0, END)
                self.sumaerick.insert(END, ventaerick)
        elif self.ebusfecha.get() == 'Ricardo':
            for i in self.tree.get_children():
                item = self.tree.item(i)
                records = item['values'][3]
                ventarich += float(records)
                self.sumarich.delete(0, END)
                self.sumarich.insert(END, ventarich)
        elif self.ebusfecha.get() == 'Frank':
            for i in self.tree.get_children():
                item = self.tree.item(i)
                records = item['values'][3]
                ventafrank += float(records)
                self.sumafrank.delete(0, END)
                self.sumafrank.insert(END, ventafrank)
        elif self.ebusfecha.get() == 'Lino':
            for i in self.tree.get_children():
                item = self.tree.item(i)
                records = item['values'][3]
                ventalino += float(records)
                self.sumalino.delete(0, END)
                self.sumalino.insert(END, ventalino)



    def __init__(self, v):
        super().__init__()

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

        lista_busqueda = ['mesero']
        lista_meseros = ['Erick', 'Ricardo', 'Frank', 'Lino', '06/04/2022', '08/04/2022']
        Label(v, text = 'Elije un tipo de busqueda:', font = ('Arial', 12, 'bold')).place(x = 0, y = 10)
        Label(v, text = 'Erick:', font = ('Arial', 12, 'bold')).place(x = 0, y = 400)
        Label(v, text = 'Ricardo:', font = ('Arial', 12, 'bold')).place(x = 0, y = 450)
        Label(v, text = 'Frank:', font = ('Arial', 12, 'bold')).place(x = 0, y = 500)
        Label(v, text = 'Lino:', font = ('Arial', 12, 'bold')).place(x = 0, y = 550)
        self.tipobus = ttk.Combobox(v, width = 15, values = lista_busqueda)
        self.tipobus.place(x = 205, y = 10)
        self.ebusfecha = ttk.Combobox(v, values = lista_meseros, width = 15)
        self.ebusfecha.place(x = 335, y = 10)
        self.sumaerick = Entry(v, width = 15)
        self.sumaerick.place(x = 80, y = 400)
        self.sumarich = Entry(v, width = 15)
        self.sumarich.place(x = 80, y = 450)
        self.sumafrank = Entry(v, width = 15)
        self.sumafrank.place(x = 80, y = 500)
        self.sumalino = Entry(v, width = 15)
        self.sumalino.place(x = 80, y = 550)
      

        bCorte = ttk.Button(v, text = 'Consultar', command = self.consultar)
        bCorte.place(x = 470, y = 10)
        ttk.Button(v, text = 'Calcular', command = self.ventameseros).place(x = 0, y = 600)
        
        

        Label(v, text = 'Bienbenido, elija su estilo de grafica', font = ('Arial', 14, 'bold')).place(x = 700, y = 10)
        lista_graficos = ['bar', 'barh', 'plot', 'scatter', 'fill_between', 'pie']
        labelopciones = Label(v, text = 'Elige un Grafico:', font = ('Arial', 10, 'bold'))
        labelopciones.place(x = 700, y = 700)
        self.combograficos = ttk.Combobox(v, values = lista_graficos)
        self.combograficos.place(x = 820, y = 700)
        botongraficos = ttk.Button(v, text = 'Grafica', command = self.graficar)
        botongraficos.place(x = 980, y = 700)


def ventana2():
    vcorte = Tk()
    vcorte.title('Estadisticas')
    vcorte.geometry('1200x750')
    vcorte.resizable(width = False, height = False)
    form = Estadisticas(vcorte)

    vcorte.mainloop()
