from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ventanas.formularios.formulario_tickets import FormularioTickets


class FormularioLogin:

    def ingresar(self):
        if self.eusuario.get() == 'Jorge' and self.epass.get() == '1234':
            try:
                vTickets = Tk()
                vTickets.title('Generacion de Tickets')
                vTickets.geometry('700x500')
                vTickets.resizable(height = False, width = False)
                FormularioTickets(vTickets)
    
            except Exception as e:
                print("Existe un error : ", e)

        else:
            messagebox.showerror('Inicio de Sesion', 'Datos incorrectos')
        self.eusuario.delete(0, END)
        self.epass.delete(0, END)
        

    def __init__(self, master):

        usuario = StringVar()
        password = StringVar()

        self.lusuario = Label(master, text = 'Usuario', font = ('Arial', 12, 'bold'))
        self.lpass = Label(master, text = 'Contraseña', font = ('Arial', 12, 'bold'))
        self.eusuario = Entry(master, textvariable = usuario)
        self.epass = Entry(master, textvariable = password, show = '*')
        self.lusuario.place(x = 150, y = 150)
        self.lpass.place(x = 150, y = 210)
        self.eusuario.place(x = 150, y = 180)
        self.epass.place(x = 150, y = 240)
        self.bingresar = ttk.Button(master, text = 'Ingresar', command = self.ingresar)
        self.bingresar.place(x = 170, y = 270)
