from formularios.repositorio_tickets import RepositorioTickets

def insertar_tickets(tickets):
    return RepositorioTickets().insertar(tickets)


def construir():    
    return RepositorioTickets().contruir_tabla()
