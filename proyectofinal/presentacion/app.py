import pandas as pd
from presentacion.app_designer import AppDesigner
from util.constant import PATH_FILE


class App(AppDesigner):

    df = None

    def __init__(self):
        super().__init__()
        self.initialize_component()
        self.carga_df()
        self.cargar_tabla()


    def carga_df(self):

        self.df = pd.read_csv(PATH_FILE)
        self.df = self.df.replace(' ', pd.NA)
    

    def cargar_tabla(self):

        self.tabladedatosdf.model.df = self.df
