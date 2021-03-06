import mysql.connector
from formularios.repositorio_conexion import RepositorioConexionSQLite
from formularios.tickets import Tickets, Tickets2

class RepositorioTickets(RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()


    def contruir_tabla(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tabla_ticktes (
                numero int(1111111) DEFAULT NULL,
                mesero varchar(100) DEFAULT NULL,
                mesa varchar(100) DEFAULT NULL,
                fecha varchar(100) DEFAULT NULL,
                cant int(100) DEFAULT NULL,
                producto varchar(100) DEFAULT NULL,
                precio_unitario int(100) DEFAULT NULL,
                total int(100) DEFAULT NULL,
                PRIMARY KEY (folio)
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
                CREATE TABLE tabla_tickets_2 (
                numero INTEGER AUTO INCREMENT,
                mesero varchar(100) NOT NULL,
                mesa varchar(100) NOT NULL,
                fecha varchar(100) NOT NULL,
                cantidad int(100) NOT NULL,
                producto varchar(100) NOT NULL,
                tipo varchar(100) NOT NULL,
                precio_unitario int(100) NOT NULL,
                total int(100) NOT NULL,
                PRIMARY KEY (numero)
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
                CREATE TABLE tabla_tickets_cobro (
                numero INTEGER AUTO INCREMENT,
                mesero varchar(100) NOT NULL,
                mesa varchar(100) NOT NULL,
                fecha varchar(100) NOT NULL,
                cantidad int(100) NOT NULL,
                producto varchar(100) NOT NULL,
                precio_unitario int(100) NOT NULL,
                total int(100) NOT NULL,
                PRIMARY KEY (numero)
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

            mySql_insert_query = """INSERT INTO tabla_tickets
            (folio, mesero, mesa, fecha, total, tipopago)
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

            mySql_insert_query = """INSERT INTO tabla_tickets_2
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

            mySql_insert_query = """INSERT INTO tabla_tickets_cobro
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
    

    def eliminarcobro(self, mesa):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_tickets_cobro
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
