class Ticket:

    def __init__(self, folio: int, cantidad: int, producto: str, mesero: str,
                mesa: str, total: float):
            self.folio = folio
            self.cantidad = cantidad
            self.producto = producto
            self.mesero = mesero
            self.mesa = mesa
            self.total = total
    

    def mostrar_info(self):
        print('FOLIO: ', self.folio)
        print('CANTIDAD: ', self.cantidad)
        print('PRODCUTO: ', self.producto)
        print('MESERO: ', self.mesero)
        print('MESA: ', self.mesa)
        print('TOTAL: ', self.total)
