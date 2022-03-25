from tkinter import *
from formularios_punto_de_venta.formulario_ticket import FormularioTickets


try:
    vTickets = Tk()
    vTickets.title('Generacion de Tickets')
    vTickets.geometry('700x500')
    vTickets.resizable(height = False, width = False)
    #logo = PhotoImage(file = 'logo.png')
    #lfondo = Label(vTickets, image = logo)
    #lfondo.place(x = 0, y = 0, relheight = 1, relwidth = 1)
    form = FormularioTickets(vTickets)

    vTickets.mainloop()

except Exception as e:
    print("Existe un error : ", e)
