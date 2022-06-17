import numpy as np
import pandas as pd
import sidetable
#import seaborn as sns
from util.generic import mod
import matplotlib.pyplot as plt
from presentacion.form_vino.form_vino_designer import FormVinoDesigner

#sns.set()

class FormVino(FormVinoDesigner):

    df = None

    def __init__(self, df):
        
        super().__init__()
        self.df = df
        self.init_conf()
        self.tabla_estadistica()
        self.analisis_vino()
    

    def tabla_estadistica(self):
        
        df_st = self.df
        df_st["General"] = "Data"
        df_std = df_st.groupby(['General'])["VinoTinto"].aggregate([np.mean, np.median, np.std, np.var, mod, pd.DataFrame.skew])
        df_std.rename(columns = {'mean': 'Media', 'median': 'Mediana', 'mod': 'Moda', "skew": "Sesgo", "std": "Desv. Est.", "var": "Varianza"}, inplace = True)
        df_std_reset = df_std.T.reset_index()
        df_std_reset.rename(columns = {'level_0': 'Nivel', 'index': 'Estadisticos', 'Data': 'Resultados'}, inplace = True)
        self.tabladatosDfest.model.df = df_std_reset[['Estadisticos', 'Resultados']]

    
    def analisis_vino(self):

        resumen_datos = self.df.stb.freg(['VinoTinto'])
        resumen_datos = resumen_datos.sort_values(by = 'VinoTinto', ascending = True)
        self.histograma_vino()
        self.barra_vino(resumen_datos)

    
    def histograma_vino(self):

        axes = self.figura_histograma_vino.subplots()
        axes.set_title("Ventas del mes de Mayo de vino", fontsize = 20)
        self.df['VinoTinto'].plot.hist(bins = 6, edgecolor = 'black', linewidth = 1.2, ax = axes)
        plt.show()

    
    def barra_vino(self, resumen_datos):

        axes = self.figura_barra_vino.subplots()
        axes.set_title("Ventas del mes de Mayo de vino", fontsize = 20)
        resumen_datos.plot.bar(x = 'VinoTinto', y = 'count', ax = axes)
        plt.show()
