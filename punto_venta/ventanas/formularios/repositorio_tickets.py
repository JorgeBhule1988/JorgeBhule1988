import mysql.connector
from formularios_punto_de_venta.repositorio_conexion import RepositorioConexionSQLite
from formularios_punto_de_venta.tickets import Tickets, Tickets2, Producto

class RepositorioTickets(RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()


    def contruir_tabla1(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tabla_venta_diaria (
                numero INTEGER PRIMARY KEY AUTOINCREMENT,
                mesero varchar(100) NOT NULL,
                mesa varchar(100) NOT NULL,
                fecha varchar(100) NOT NULL,
                total int(100) NOT NULL,
                tipopago varchar(100) NOT NULL
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
            print("Creacion de la tabla satisfatoriamente ")
        except :
            error=1
            print(f"Fallo la creacion de la tabla en MySQL: {error}")
        return error
    

    def contruir_tabla2(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tabla_tickets_principal (
                numero INTEGER PRIMARY KEY AUTOINCREMENT,
                mesero varchar(100) NOT NULL,
                mesa varchar(100) NOT NULL,
                fecha varchar(100) NOT NULL,
                cantidad int(100) NOT NULL,
                producto varchar(100) NOT NULL,
                precio_unitario int(100) NOT NULL,
                total int(100) NOT NULL
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
            print("Creacion de la tabla satisfatoriamente ")
        except :
            error=1
            print(f"Fallo la creacion de la tabla en MySQL: {error}")
        return error
    

    def contruir_tabla3(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tabla_cobro (
                numero INTEGER PRIMARY KEY AUTOINCREMENT,
                mesero varchar(100) NOT NULL,
                mesa varchar(100) NOT NULL,
                fecha varchar(100) NOT NULL,
                cantidad int(100) NOT NULL,
                producto varchar(100) NOT NULL,
                precio_unitario int(100) NOT NULL,
                total int(100) NOT NULL
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
            print("Creacion de la tabla satisfatoriamente ")
        except :
            error=1
            print(f"Fallo la creacion de la tabla en MySQL: {error}")
        return error

    
    def construir_tabla4(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tabla_producto (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                categoria varchar(100) NOT NULL,
                precio_unitario int(100) NOT NULL,
                stock int(100) NOT NULL,
                existencia varchar(100) NOT NULL
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
            print("Creacion de la tabla satisfatoriamente ")
        except :
            error=1
            print(f"Fallo la creacion de la tabla en MySQL: {error}")
        return error


    def insertar(self, tickets: Tickets) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tabla_venta_diaria
            (numero, mesero, mesa, fecha, total, tipopago)
            VALUES(NULL, ?, ?, ?, ?, ?);
            """
            registros = (tickets.mesero, tickets.mesa, tickets.fecha, tickets.total, tickets.tipopago)

            cursor.execute(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado
    

    def insertar2(self, tickets: Tickets2) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tabla_tickets_principal
            (numero, mesero, mesa, fecha, cantidad, producto, precio_unitario, total)
            VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);
            """
            registros = [(tickets.mesero, tickets.mesa, tickets.fecha, tickets.cantidad, tickets.producto, tickets.precio_unitario, tickets.total)]

            cursor.executemany(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado
    

    def insertar3(self, tickets: Tickets2) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tabla_cobro
            (numero, mesero, mesa, fecha, cantidad, producto, precio_unitario, total)
            VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);
            """
            registros = [(tickets.mesero, tickets.mesa, tickets.fecha, tickets.cantidad, tickets.producto, tickets.precio_unitario, tickets.total)]

            cursor.executemany(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado
    

    def insertar4(self, producto: Producto) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tabla_producto
            (id_producto, nombre, categoria, precio_unitario, stock, existencia)
            VALUES(NULL, ?, ?, ?, ?, ?);
            """
            registros = (producto.id_producto, producto.nombre, producto.categoria, producto.precio_unitario, producto.stock, producto.existencia)

            cursor.execute(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado

    def eliminarcobro(self, mesa):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_cobro
            WHERE mesa = ?;
            """            
            eliminar = (mesa,)
            cursor.execute(mySql_eliminar_query, eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Fallo la eliminacion {error}")
        finally:
            self.cerrar_conexion()

        return afectado

    
    def eliminarproducto(self, producto):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_cobro
            WHERE producto = ?;
            """            
            eliminar = (producto,)
            cursor.execute(mySql_eliminar_query, eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Fallo la eliminacion {error}")
        finally:
            self.cerrar_conexion()

        return afectado

    
    def eliminarproducto2(self, producto):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_tickets_principal
            WHERE producto = ?;
            """            
            eliminar = (producto,)
            cursor.execute(mySql_eliminar_query, eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Fallo la eliminacion {error}")
        finally:
            self.cerrar_conexion()

        return afectado
