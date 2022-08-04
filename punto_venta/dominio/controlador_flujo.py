from formularios.repositorio_tickets import RepositorioTickets


def insertar_tickets(tickets):
    return RepositorioTickets().insertar(tickets)


def insertar_tickets2(tickets):
    return RepositorioTickets().insertar2(tickets)


def insertar_tickets3(tickets):
    return RepositorioTickets().insertar3(tickets)


#def consultar_persona():    
#    return RepositorioTickets().consultar()


def eliminar_tickets(mesa):    
    return RepositorioTickets().eliminarcobro(mesa)

def eliminar_fila_cobro(producto):
    return RepositorioTickets().eliminarproducto(producto)


def eliminar_fila_cobro2(producto):
    return RepositorioTickets().eliminarproducto2(producto)    


def construir():    
    return RepositorioTickets().contruir_tabla()


def construir2():    
    return RepositorioTickets().contruir_tabla2()


def construir3():    
    return RepositorioTickets().contruir_tabla3()
