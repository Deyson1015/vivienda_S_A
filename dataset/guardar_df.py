import os
import pandas as pd

def obtener_dataframe():
    ruta = os.path.join(os.path.dirname(__file__), 'dataset_vivienda.xlsx' )
    df = pd.read_excel(ruta, header=0)
    return df
