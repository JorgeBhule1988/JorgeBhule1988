from tkinter import *
from tkinter import ttk
from formularios_punto_de_venta.repositorio_conexion import RepositorioConexionSQLite
import mysql.connector


class BotonesMesas(RepositorioConexionSQLite):

    def Limpiarticket(self):
        for i in self.captura.get_children():
            self.captura.delete(i)


    def mesa1_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))         
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la la consulta {error}")
        #finally:
        #    self.cerrar_conexion()

    
    def mesa3_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa5_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '5')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '5'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa6_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '6')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '6'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa7_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '7')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '7'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    
    def mesa8_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '8')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '8'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa9_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '9')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '9'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa10_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '10')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '10'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa11_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '11')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '11'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa12_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '12')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '12'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa13_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '13')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '13'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac1_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac2_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava2')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava2'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac3_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac4_1(self):
        self.Limpiarticket()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava4')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava4'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()


    def __init__(self, v):


        cantidad = IntVar()
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
        lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

        self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
        self.ecantidad = Entry(v, textvariable = cantidad)
        self.emesa = ttk.Combobox(v, value = lista_mesas)
        self.emesero = ttk.Combobox(v, value = lista_meseros)
