import numpy as np
import pandas as pd
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
