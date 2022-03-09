import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    
    sql_select_Query = "select * from jorge_serna_persona"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # busqueda de todos los registros
    records = cursor.fetchall()
    print("Total de numero de registros en la tabla: ", cursor.rowcount)
    print()
    print("Imprimiendo cada registro ")
    for row in records:
        print("ID = ", row[0])
        print("CURP = ", row[1])
        print("NOMBRE = ", row[2])
        print("EDAD = ", row[3])
        print("CORREO = ", row[4])
        print("TELEFONO = ", row[5])
except mysql.connector.Error as error:
    print(f"Error al leer los datos en la base de datos: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL Conexion Cerrada")
