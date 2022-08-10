from tkinter import *
from tkinter import ttk

class FormularioBotones:
    
    def valores_boton(self):

        self.tree.insert('', END, text = str(self.enombre.get()), values = ('5'))
        self.tree.delete(0, END)


    def crear_boton(self):
        
        self.botondinamico = Button(self.frame, text = self.enombre.get(), height = 5, width = 12, command = self.valores_boton)
        self.botondinamico.place(x = 0, y = 0)

    def datos_boton(self):
        
        w = Tk()
        w.geometry('300x300')

        nombre = StringVar()

        self.nombre = Label(w, text = 'Nombre')
        self.nombre.place(x = 0, y = 0)
        self.enombre = Entry(w, textvariable = nombre, width = 20)
        self.enombre.place(x = 100, y = 0)

        self.boton = ttk.Button(w, text = 'Crear', command = self.crear_boton)
        self.boton.place(x = 0, y = 40)

        w.mainloop()


    def __init__(self, v):

        super().__init__()
        self.frame = Frame(v, height = 500, width = 500)
        self.frame.place(x = 0, y = 0)
        self.agregar = ttk.Button(self.frame, text = 'Agregar un boton', width = 20, command= self.datos_boton)
        self.agregar.place(x = 300, y = 400)

        self.tree = ttk.Treeview(self.frame, height=5, columns=('#0'))
        self.tree.place(x = 0, y = 100)
        self.tree.heading('#0', text = 'Producto', anchor=CENTER)
        self.tree.heading('#1', text = 'Cantidad', anchor=CENTER)


def ventana():

    ventana = Tk()
    ventana.title('tratar de hacer un boton')
    ventana.geometry('500x500')
    form = FormularioBotones(ventana)

    ventana.mainloop()
    
ventana()
