import tkinter as tk
import util.generic as ult
from pandastable import Table


class AppDesigner(tk.Tk):

    def __init__(self):
        super().__init__()


    def estadistico_vino(self):
        pass


    def estadistico_sin_alcohol(self):
        pass


    def estadistico_locales(self):
        pass
    

    def initialize_component(self):
        
        self.config_window()
        self.framegeneral()
        self.boton_vino()
        self.boton_sin_alcohol()
        self.boton_locales()
        self.abrirdatos()
        self.tabla_datos()
        

    def config_window(self):
        self.title('Practica Final')
        w, h = 900, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg = 'white')
        ult.centrar_ventana(self, w, h)
    

    def framegeneral(self):

        self.frame_general = tk.Frame(self, bd = 0, relief = tk.SOLID, bg = 'white')
        self.frame_general.pack(side = 'top', fill = tk.BOTH, expand = "yes")

    
    def boton_vino(self):

        self.boton_est_vino = tk.Button(self.frame_general, font = ('Time', 14), bg = '#3a7ff6', bd = 0, fg = '#fff', text = 'Ver Estadisticas de Vino', command = self.estadistico_vino)
        self.boton_est_vino.pack(side = tk.TOP, fill = tk.X, padx = 10, pady = 10)
    

    def boton_sin_alcohol(self):

        self.boton_est_sin_alcohol = tk.Button(self.frame_general, font = ('Time', 14), bg = '#3a7ff6', bd = 0, fg = '#fff', text = 'Ver Estadisticas de Bebidas Sin Alcohol', command = self.estadistico_sin_alcohol)
        self.boton_est_sin_alcohol.pack(side = tk.TOP, fill = tk.X, padx = 10, pady = 10)
    

    def boton_locales(self):

        self.boton_est_locales = tk.Button(self.frame_general, font = ('Time', 14), bg = '#3a7ff6', bd = 0, fg = '#fff', text = 'Ver Estadisticas de Locales', command = self.estadistico_locales)
        self.boton_est_locales.pack(side = tk.TOP, fill = tk.X, padx = 10, pady = 10)

    
    def abrirdatos(self):

        self.frame_datos = tk.Frame(self, bd = 0, relief = tk.SOLID, bg = 'red')
        self.frame_datos.pack(side = 'top', fill = tk.BOTH, expand = "yes")

    
    def tabla_datos(self):

        self.tabladedatosdf = Table(self.frame_datos, showtoolbar = True, showstatubar = True, rows = 5)
        self.tabladedatosdf.show()
