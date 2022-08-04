from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from formularios.repositorio_conexion import RepositorioConexionSQLite
import mysql.connector


class BonotonesMenu(RepositorioConexionSQLite):

    def botonrodizio(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 560
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio', '560', subtotal))
            self.ecantidad.delete(0, END)

        
    def botonrodiziol(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 400
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local', '400', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodiziom(self):
        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 280
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Menor', '280', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodizioml(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 200
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Local Menor', '200', subtotal))
            self.ecantidad.delete(0, END)


    def botonrodiziotg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 525
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Rodizio Togo', '525', subtotal))
            self.ecantidad.delete(0, END)

    def botonpicana(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña', '950', subtotal))
            self.ecantidad.delete(0, END)


    def botonpicanatg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 695
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Picaña TG', '695', subtotal))
            self.ecantidad.delete(0, END)


    def botontomahack(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('TOMA HACK', '1950', subtotal))
            self.ecantidad.delete(0, END)


    def botonburguer(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 220
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa', '220', subtotal))
            self.ecantidad.delete(0, END)


    def botonburguertg(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 120
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Hamburguesa Togo', '120', subtotal))
            self.ecantidad.delete(0, END)


    def botonaguap(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Agua Panna', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botontopoc(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Topo Chico', '95', subtotal))
            self.ecantidad.delete(0, END)


    def botonlimonada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 50
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Limonada', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botonnaranjada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 50
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Naranjada', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botoncoca(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola', '40', subtotal))
            self.ecantidad.delete(0, END)

    
    def botoncocad(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Coca Cola Dieta', '40', subtotal))
            self.ecantidad.delete(0, END)

        
    def botonsprite(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Sprite', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonfresca(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Fresca', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonmundet(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 40
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mundet', '40', subtotal))
            self.ecantidad.delete(0, END)


    def botonpinada(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Piñada', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botonmojitov(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito S/A', '75', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonpituv(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 75
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña S/A', '75', subtotal))
            self.ecantidad.delete(0, END)


    def botonpacifico(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonpacificos(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Suave', '60', subtotal))
            self.ecantidad.delete(0, END)


    def botonpacificol(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Pacifico Ligth', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botoncorona(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Corona', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonvictoria(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 60
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Victoria', '60', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonartesanal(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 95
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cerveza Artesanal', '95', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonegramodelo(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 85
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Negra Modelos', '85', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonmojito(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 140
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mojito', '140', subtotal))
            self.ecantidad.delete(0, END)


    def botonmezcalitaj(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Jamaica', '165', subtotal))
            self.ecantidad.delete(0, END)

    
    def botonmezcalitam(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 165
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Mezcalita Maracuya', '165', subtotal))
            self.ecantidad.delete(0, END)


    def botoncaipirina(self):
        subtotal = float(self.ecantidad.get()) * 165
        self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Caipiriña', '165', subtotal))
        self.ecantidad.delete(0, END)


    def botocasamadero(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 1250
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Bot Vino Casa Madero', '1250', subtotal))
            self.ecantidad.delete(0, END)


    def botoncopadevino(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 185
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Copa de Vino', '185', subtotal))
            self.ecantidad.delete(0, END)


    def botoncavalrose(self):

        if(len(self.emesero.get()) == 0) or (len(self.emesa.get()) == 0) or (len(self.ecantidad.get()) == 0):
            messagebox.showwarning(message = 'Falta seleccionar el mesero o el numero de mesa o la cantidad', title = 'Warning')
        else:
            subtotal = float(self.ecantidad.get()) * 950
            self.captura.insert('', END, text = str(self.ecantidad.get()), values = ('Cavall Rose', '950', subtotal))
            self.ecantidad.delete(0, END)

    
    def limpiar(self):
        for i in self.captura.get_children():
            self.captura.delete(i)
    
    #Botones de mesas
    def mesa1(self):
        self.limpiar()
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
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '3')
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
    

    def mesa5(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '5')
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

    
    def mesa6(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '6')
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

    
    def mesa7(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '7')
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
    
    def mesa8(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '8')
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
    

    def mesa9(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '9')
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

    
    def mesa10(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '10')
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
    

    def mesa11(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '11')
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

    
    def mesa12(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '12')
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

    
    def mesa13(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '13')
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

    
    def mesac1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava1')
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

    
    def mesac2(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava2')
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

    
    def mesac3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava3')
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

    
    def mesac4(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava4')
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
