def eliminarfila(self):
        
        curItem = self.captura_tree.focus()
        fila = self.captura_tree.item(curItem)
        afectados = controlador.eliminar_fila_cobro(fila["text"])
        afectados1 = controlador.eliminar_fila_cobro2(fila["text"])

        
def nuevo_ticket(self):

        self.emesero.delete(0, END)
        self.emesa.delete(0, END)
        self.etotalpesos.delete(0, END)
        self.etotaldolares.delete(0, END)
        self.epago.delete(0, END)
        self.etipo_pago.delete(0, END)
        self.ecambio.delete(0, END)
        self.esubtotal.delete(0, END)
        self.eiva.delete(0, END)
        self.enombre_product.delete(0, END)
        self.eprecio_unit.delete(0, END)
        self.eserv_sugerido.delete(0, END)
        self.etotal_sugerido.delete(0, END)
        regitro = self.captura.get_children()
        regitro_1 = self.captura_tree.get_children()
        for i in regitro:
            self.captura.delete(i)
        for i in regitro_1:
            self.captura_tree.delete(i)
        
        self.etotalpesos.config(state = 'disable')
        self.etotaldolares.config(state = 'disable')
        self.epago.config(state = 'disable')
        self.etipo_pago.config(state = 'disable')
        self.ecambio.config(state = 'disable')
        self.bguardar.config(state = 'disable')
        self.cobrart.config(state = 'disable')
        self.cerrarmesa.config(state = 'disable')
        self.esubtotal.config(state = 'disable')
        self.eiva.config(state = 'disable')
        self.eimprimir.config(state = 'disable')

def sumartotales(self):
        suma = 0
        sumadolares = 0
        for i in self.captura_tree.get_children():
            item = self.captura_tree.item(i)
            records = item['values'][3]
            suma += float(records)
            sumadolares = round(float(suma / 19), 2)
            self.etotalpesos.delete(0, END)
            self.etotalpesos.insert(END, suma)
            self.etotaldolares.delete(0, END)
            self.etotaldolares.insert(END, sumadolares)
        subtotal = round(float(suma / 1.16), 2)
        iva = round(float(subtotal * .16), 2)
        self.esubtotal.delete(0, END)
        self.esubtotal.insert(END, subtotal)
        self.eiva.delete(0, END)
        self.eiva.insert(END, iva)
        
        
def seleccionar(self, click):
        #selection = self.captura.identify('item', click.x, click.y)
        column = self.captura_tree.identify_column(click.x)
        column_index = int(column[1:]) - 1
        selected_iid = self.captura_tree.focus()
        self.selected_values = self.captura_tree.item(selected_iid)
        if column == '#1':
            selected_text = self.selected_values.get('values')[0]
        #else:
            #selected_text = self.selected_values.get('values')[column_index]
        column_box = self.captura_tree.bbox(selected_iid, '#1')
        entry_edit = ttk.Spinbox(self.captura_tree, from_ = 1, to = 30, width = column_box[2])
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid
        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, END)
        entry_edit.focus()
        entry_edit.bind('<FocusOut>', self.on_focus_out)
        entry_edit.bind('<Return>', self.on_enter_pressed)
        entry_edit.place(x = column_box[0], y = column_box[1], w = column_box[2], h = column_box[3])


    def on_enter_pressed(self, click):
        self.new_text = click.widget.get()
        self.selected_iid = click.widget.editing_item_iid
        column_index = click.widget.editing_column_index
        if column_index == 0:
            self.current_values_1 = self.captura_tree.item(self.selected_iid).get('values')
            self.current_values_1[0] = self.new_text
            self.captura_tree.item(self.selected_iid, values = self.current_values_1)
            text_2 = self.selected_values.get('values')[2]
            resultado_1 = int(self.new_text) * int(text_2)
            self.current_values = self.captura_tree.item(self.selected_iid).get('values')
            self.current_values[3] = resultado_1
            self.captura_tree.item(self.selected_iid, values = self.current_values)
        #else:
        #    current_values = self.captura.item(selected_iid).get('values')
        #    current_values[column_index] = new_text
        #    self.captura.item(selected_iid, values = current_values)
        click.widget.destroy()


    def on_focus_out(self, click):
        click.widget.destroy()


    def actualizar_producto(self):

        curItem = self.captura_tree.focus()
        fila = self.captura_tree.item(curItem)
        print(fila)
        afectados = controlador.actualizar_tabla(fila["values"][0], fila["values"][3], fila["text"])
        afectados1 = controlador.actualizar_tabla_1(fila["values"][0], fila["values"][3], fila["text"])
        
   #def seleccionar_eliminar_fila(self, click):

  #    item = self.captura_tree.identify('item', click.x, click.y)
  #    self.eli_id.set(self.captura_tree.item(item, 'text'))
  #    self.eli_cant.set(self.captura_tree.item(item, 'values')[0])
  #    self.eli_prod.set(self.captura_tree.item(item, 'values')[1])
  #    self.eli_unit.set(self.captura_tree.item(item, 'values')[2])
  #    self.eli_total.set(self.captura_tree.item(item, 'values')[3])
  
  self.captura_tree = ttk.Treeview(self.fproducto2, height= 10, columns=('#0', '#1', '#2', '#3'))
  self.captura_tree.place(x = 5, y = 10)
  self.captura_tree.column('#0', width = 50)
  self.captura_tree.heading('#0', text = 'ID', anchor=CENTER)
  self.captura_tree.column('#1', width = 50)
  self.captura_tree.heading('#1', text = 'Cant', anchor=CENTER)
  self.captura_tree.column('#2', width = 150)
  self.captura_tree.heading('#2', text = 'Producto', anchor=CENTER)
  self.captura_tree.column('#3', width = 100)
  self.captura_tree.heading('#3', text = 'Precio Unit', anchor=CENTER)
  self.captura_tree.column('#4', width = 100)
  self.captura_tree.heading('#4', text = 'Total', anchor=CENTER)
  self.captura_tree.bind('<Double-1>', self.seleccionar)
  #self.captura_tree.bind('<Double-1>', self.seleccionar_eliminar_fila)

  #self.eli_id = StringVar()
  #self.eli_cant = StringVar()
  #self.eli_prod = StringVar()
  #self.eli_unit = StringVar()
  #self.eli_total = StringVar()
  
  ######Repositorio Ticket##########
  def eliminarproducto(self, numero):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_cobro
            WHERE numero = ?;
            """            
            eliminar = (numero,)
            cursor.execute(mySql_eliminar_query, eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Fallo la eliminacion {error}")
        finally:
            self.cerrar_conexion()

        return afectado

    
    def eliminarproducto2(self, numero):
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tabla_tickets_principal
            WHERE numero = ?;
            """            
            eliminar = (numero,)
            cursor.execute(mySql_eliminar_query, eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Fallo la eliminacion {error}")
        finally:
            self.cerrar_conexion()

        return afectado
    
    
    def modificar_tabla(self, cantidad, total, numero):
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            modificar = "UPDATE tabla_tickets_principal SET cantidad = ?, total = ? WHERE numero = ?"
            actualizar = (cantidad, total, numero,)
            cursor.execute(modificar, actualizar)
            self.connection.commit()
        except mysql.connector.Error as error:
                print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def modificar_tabla_1(self, cantidad, total, numero):
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            modificar = f"UPDATE tabla_cobro SET cantidad = '{cantidad}', total = '{total}' WHERE numero = '{numero}'"
            cursor.execute(modificar)
            self.connection.commit()
        except mysql.connector.Error as error:
                print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
            
            
    #####Controlador de Flujo#######
    
    def actualizar_tabla(cantidad, total, numero):
    return RepositorioTickets().modificar_tabla(cantidad, total, numero)


    def actualizar_tabla_1(cantidad, total, numero):
        return RepositorioTickets().modificar_tabla_1(cantidad, total, numero)
      
   #####BotonesMenu######
  
  def mesa1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa5(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '5')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '5'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa6(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '6')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '6'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa7(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '7')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '7'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    
    def mesa8(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '8')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '8'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa9(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '9')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '9'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa10(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '10')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '10'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa11(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '11')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '11'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa12(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '12')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '12'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa13(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '13')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '13'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac2(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava2')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava2'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac4(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava4')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava4'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesacasab1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'CasaB1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'CasaB1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesacasab2(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'CasaB2')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select numero, cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'CasaB2'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura_tree.insert('', END, text = row[0], values = (row[1], row[3], row[4], row[5]))         
            self.emesero.insert(END, row[2])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
            
            
    self.captura_tree = ttk.Treeview(v, columns=('#0', '#1', '#2', '#3'))
