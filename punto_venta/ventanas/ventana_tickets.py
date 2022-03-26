from tkinter import *
from formularios.formulario_tickets import FormularioTickets


try:
    vTickets = Tk()
    vTickets.title('Generacion de Tickets')
    vTickets.geometry('700x500')
    vTickets.resizable(height = False, width = False)
    form = FormularioTickets(vTickets)

    vTickets.mainloop()

except Exception as e:
    print("Existe un error : ", e)
