import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    
    mySql_insert_query = """INSERT INTO jorge_serna_persona (
                            id, curp, nombre, edad, correo, telefono)
                            VALUES (3, 'SEML800222249', 'Luis', 42, 'Monago_07@hotmail.com', 6241322792)
                            """
    
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Fue registrado satisfactoriamente ")
    cursor.close()
except mysql.connector.Error as error:
    print(f"Fallo la insercion: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL Conexion Cerrada")
