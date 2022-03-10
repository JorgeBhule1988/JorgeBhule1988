import mysql.connector
from Persona import Persona


class Insertar:

    def __init__(self):

        self.connection = mysql.connector.connect(host='proweb-corp.com',
                                            database='prowebco_cocid',
                                            user='prowebco_alumnos_cocid',
                                            password='qpF5n,QDotkU')
        self.cursor = self.connection.cursor()
    
    def agregra(self):


        id = int(input('dame el ID: '))
        curp = input('Dame la CURP: ')
        nombre = input('Dame el nombre: ')
        edad = int(input('Dame la edad: '))
        correo = input('Dame un correo: ')
        telefono = int(input('Dame un numero telefonico: '))
        Persona(curp, nombre, edad, correo, telefono)
        usuario = Persona(curp, nombre, edad, correo, telefono)                                    
    
        mySql_insert_query = """INSERT INTO jorge_serna_persona (
                                id, curp, nombre, edad, correo, telefono)
                                VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
                                """.format(id, usuario.curp, usuario.nombre, usuario.edad, usuario.correo, usuario.telefono)
    
        self.cursor = self.connection.cursor()
        self.cursor.execute(mySql_insert_query)
        self.connection.commit()
        print(self.cursor.rowcount, "Fue registrado satisfactoriamente ")
        self.cursor.close()

agregar = Insertar()
