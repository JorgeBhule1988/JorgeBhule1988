import mysql.connector
from conexioSQL import RepositorioConexionSQLite


class Insersion(RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()
        
    def contruir_tabla(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tb_punto_venta (
                folio int(111111) NOT NULL,
                cantidad int(100) DEFAULT NULL,
                producto varchar(100) DEFAULT NULL,
                mesero varchar(100) DEFAULT NULL,
                mesa varchar(100) DEFAULT NULL,
                total float(111111) DEFAULT NULL,
                PRIMARY KEY (folio)
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
        except :
            error=1
        return error   

    def insertar(self) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tb_punto_venta
            (folio, cantidad, producto, mesero, mesa, total)
            VALUES(1, 5, 'Copa de Vino', 'Jorge', '10', 925);
            """
            #registros = (persona.folio, persona.cantidad, persona.producto,
            #             persona.mesero, persona.mesa, persona.total)

            cursor.execute(mySql_insert_query)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado

    def consultar(self) -> list:
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select * from tb_punto_venta"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
                print("FOLIO = ", row[0])
                print("CANT = ", row[1])
                print("PRODUCTO = ", row[2])
                print("MESERO = ", row[3])
                print("MESA = ", row[4])
                print("TOTAL = ", row[5])

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

agregar = Insersion()
print(agregar.consultar())
