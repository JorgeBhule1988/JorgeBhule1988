import mysql.connector
from mysql.connector import Error
class Persona:

    def __init__(self, curp: str, nombre: str, edad: int, correo: str, telefono: int):
        try:
            self.connection = mysql.connector.connect(host='proweb-corp.com',
                                            database='prowebco_cocid',
                                            user='prowebco_alumnos_cocid',
                                            password='qpF5n,QDotkU')
        except Error as e:
            print("Error mientras se conectaba MySQL", e)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("MySQL cconexion esta cerrada")    
        self.curp = curp
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
