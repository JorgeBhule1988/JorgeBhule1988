import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table

class FormVinoDesigner(tk.Toplevel):

    def __init__(self):
        super().__init__()
        
    
    def init_conf(self):

        self.configurar_ventana()
        self.frame_principal()
        self.frameprincipalpanel1()
        self.frameprincipalpanel2()
        self.frameprincipalsecundario()
        self.tablaestadistica()
        self.figurahistovino()
        self.graficabarravino()

    
    def configurar_ventana(self):

        self.title('Estadisticas de Vino')
        w, h = 1024, 700
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg = 'black')
        self.state('zoomed')
        utl.centrar_ventana(self, w, h)

    
    def frame_principal(self):

        self.frame_zona_principal = tk.Frame(self, bd = 1, height = 200, relief = tk.SOLID, bg = 'white')
        self.frame_zona_principal.pack(side = 'top', fill = tk.BOTH)


    def frameprincipalpanel1(self):

        self.frame_zona_principal_panel1 = tk.Frame(self.frame_zona_principal, bd = 1, height = 300, width = 200, relief = tk.SOLID, bg = 'green')
        self.frame_zona_principal_panel1.pack(side = 'left', fill = tk.X)

    
    def frameprincipalpanel2(self):

        self.frame_zona_principal_panel2 = tk.Frame(self.frame_zona_principal, bd = 1, height = 300, relief = tk.SOLID, bg = 'white')
        self.frame_zona_principal_panel2.pack(side = 'left', fill = tk.X, expand = "yes")


    def frameprincipalsecundario(self):

        self.frame_zona_principal_secundario = tk.Frame(self, bd = 1, height = 300, relief = tk.SOLID, bg = 'red')
        self.frame_zona_principal_secundario.pack(side = 'top', fill = tk.BOTH, expand = "yes") 


    def tablaestadistica(self):

        self.tabladatosDfest = Table(self.frame_zona_principal_panel1, showtoolbar = True, showstatusbar = False, width = 200, height = 200, rows = 8)
        self.tabladatosDfest.show()


    def figurahistovino(self):

        self.figura_histograma_vino = plt.Figure(figsize = (80, 5), dpi = 80)
        self.figura_canvas_vino = FigureCanvasTkAgg(self.figura_histograma_vino, self.frame_zona_principal_panel2)
        self.figura_canvas_vino.get_tk_widget().pack(side = tk.LEFT, fill = tk.BOTH)


    def graficabarravino(self):

        self.figura_barra_vino = plt.Figure(figsize = (300, 20), dpi = 80)
        self.canvas_barra_vino = FigureCanvasTkAgg(self.figura_barra_vino, self.frame_zona_principal_secundario)
        self.figura_canvas_vino.get_tk_widget().pack(side = tk.LEFT, fill = tk.BOTH, ipady = 50)
