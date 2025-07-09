# models/vivienda_model.py
import sys
import pandas as pd
sys.path.append('./dataset')  # Para importar tu archivo de carga
from dataset.guardar_df import obtener_dataframe  # Ya tiene el DataFrame cargado desde Excel

class ViviendaModel:
    def __init__(self):
        self.df = obtener_dataframe()

    def insertar_viviendas_en_mongo(self, conexion):
        for _, fila in self.df.iterrows():
            documento = fila.to_dict()  
            conexion.insertar(documento)


    def obtener_resumen_estadistico(self):
        resumen = self.df.describe()
        total = len(self.df)
        return resumen, total
