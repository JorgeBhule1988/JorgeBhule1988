import pandas as pd
from presentacion.app_designer import AppDesigner
from util.constant import PATH_FILE


class App(AppDesigner):

    df = None

    def __init__(self):
        super().__init__()
        self.initialize_component()
