class Tickets:

    folio: int = None
    mesero: str = None
    mesa: str = None
    fecha: str = None
    total: int = None
    tipopago: str = None

    
    def __init__(self) -> None:
        pass

    
    def asignar(self, folio, mesero, mesa, fecha, total, tipopago) -> None:
        self.folio = folio
        self.mesero = mesero
        self.mesa = mesa
        self.fecha = fecha
        self.total = total
        self.tipopago = tipopago
        return self


    def mostrar_info(self) -> None:
        print("FOLIO : ", self.folio)
        print("MESERO : ", self.mesero)
        print("MESA : ", self.mesa)
        print("FECHA : ", self.fecha)
        print("TOTAL : ", self.total)
        print('TIPO PAGO: ', self.tipopago)
        
    def __str__(self) -> str:
        return ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.folio, self.mesero, self.mesa, self.fecha, self.total, self.tipopago))


class Tickets2:

    numero: int = None
    mesero: str = None
    mesa: str = None
    fecha: str = None
    cantidad: int = None
    producto: int = None
    precio_unitario = None
    total: str = None
    
    def __init__(self) -> None:
        pass

    
    def asignar(self, numero, mesero, mesa, fecha, cantidad, producto, precio_unitario, total) -> None:
        self.numero = numero
        self.mesero = mesero
        self.mesa = mesa
        self.fecha = fecha
        self.cantidad = cantidad
        self.producto = producto
        self.precio_unitario = precio_unitario
        self.total = total
        return self


    def mostrar_info(self) -> None:
        print("FOLIO : ", self.numero)
        print("MESERO : ", self.mesero)
        print("MESA : ", self.mesa)
        print("FECHA : ", self.fecha)
        print("CANTIDAD : ", self.cantidad)
        print("PRODUCTO: ", self.producto)
        print("PRECIO UNITARIO: ", self.precio_unitario)
        print("TOTAL : ", self.total)
        
        
    def __str__(self) -> str:
        return ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.numero, self.mesero, self.mesa, self.fecha, 
                                                                self.cantidad, self.producto, self.precio_unitario, self.total))


class Producto:

    id_producto: int = None
    nombre: str = None
    categoria: str = None
    precio_unitario: str = None
    stock: int = None
    existencia: str = None

    
    def __init__(self) -> None:
        pass

    
    def asignar(self, id_producto, nombre, categoria, precio_unitario, stock, existencia) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario = precio_unitario
        self.stock = stock
        self.existencia = existencia
        return self


    def mostrar_info(self) -> None:
        print("ID PRODCUTO : ", self.id_producto)
        print("NOMBRE : ", self.nombre)
        print("CATEGORIA : ", self.categoria)
        print("PRECIO UNITARIO : ", self.precio_unitario)
        print("STOCK : ", self.stock)
        print('EXISTENCIAS: ', self.existencia)
        
    def __str__(self) -> str:
        return ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.id_producto, self.nombre, self.categoria, self.precio_unitario, self.stock, self.existencia))
