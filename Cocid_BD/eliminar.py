import mysql.connector

def eliminacion():
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    cursor = connection.cursor()
    print("Registro a eliminar")
    sql_select_query = """select * from jorge_serna_persona"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    for row in record:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

    # eliminar registro
    borrar = int(input('Que ID deseas eliminar: '))
    sql_Delete_query = """Delete from jorge_serna_persona where id = {}""".format(borrar)
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('numero de registro eliminado', cursor.rowcount)

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexion cerrada")
