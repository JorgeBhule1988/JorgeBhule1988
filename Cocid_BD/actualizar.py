import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    cursor = connection.cursor()

    print("Antes de actualizar el registro ")
    sql_select_query = """select * from jorge_serna_persona where id = 3"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # actualizacion de la fila 
    sql_update_query = """Update jorge_serna_persona set correo = 'monago_09@gmail.com' where id = 3"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Actualizacion de registro satisfactorio")

    print("Despues de la actualizacion de registro")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Fallo la actualizacion del registro: {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL conexion cerrada")
