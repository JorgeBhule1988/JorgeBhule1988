import mysql.connector

def seleccionar():

    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')

    while True:
        try:
            print('\t ##########BUSCADOR############ ')
            print('\t Seleccione el tipo de busqueta ')
            print('\t 1 - CURP ##################### ')
            print('\t 2 - Nombre ################### ')
            print('\t 3 - Todos los registros ###### ')
            print('\t 0 - Salir #################### ')
            opcion = int(input('\t Seleccione una opcion valida: '))
            if opcion == 0:
                print('\t Que le vaya bonito!! ')
                if connection.is_connected():
                    connection.close()
                    print("MySQL Conexion Cerrada")
                    break
            elif opcion < 0 or opcion > 3:
                print('\t Elije una opcion valida!! ')
            else:
                break
        except ValueError as e:
            print('\t Dato invalido,', e)
        else:
            continue

    
    if opcion == 1:
        sql_select_Query = "select id, curp from jorge_serna_persona"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # busqueda de todos los registros
        records = cursor.fetchall()
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
        print("Imprimiendo cada registro ")
        for row in records:
            print("ID: ", row[0], "CURP: ", row[1])
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
    elif opcion == 2:
        sql_select_Query = "select id, nombre from jorge_serna_persona"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # busqueda de todos los registros
        records = cursor.fetchall()
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
        for row in records:
            print("ID: ", row[0], "Nombre: ", row[1])
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
    elif opcion == 3:
        sql_select_Query = "select * from jorge_serna_persona"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # busqueda de todos los registros
        records = cursor.fetchall()
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
        for row in records:
            print("ID: ", row[0], "CURP: ", row[1], "Nombre: ", row[2], 
                  "Edad: ", row[3], "Correo: ", row[4], "Telefono: ", row[5]) 
        print("\nTotal de numero de registros en la tabla: ", cursor.rowcount)
    
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL cconexion esta cerrada")
