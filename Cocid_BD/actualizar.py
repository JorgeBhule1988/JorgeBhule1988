import mysql.connector

def actualizacion():
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    cursor = connection.cursor()

    print("Antes de actualizar el registro ")
    seleccion = int(input('Que ID desea Actualizar: '))
    sql_select_query = """select * from jorge_serna_persona where id = {} """.format(seleccion)
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # actualizacion de la fila
    campo = input('Que campo desea Actualizar: curp, nombre, edad, correo, telefono: ')
    cambio = input('Escribe en nuevo dato: ') 
    sql_update_query = """Update jorge_serna_persona set {} = '{}' where id = {}""".format(campo, cambio, seleccion)
    cursor.execute(sql_update_query)
    connection.commit()
    print("Actualizacion de registro satisfactorio")

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL cconexion esta cerrada")
