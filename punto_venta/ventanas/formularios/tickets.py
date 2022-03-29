class Tickets:

    folio: int = None
    mesero: str = None
    mesa: str = None
    fecha: str = None
    total: str = None
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
