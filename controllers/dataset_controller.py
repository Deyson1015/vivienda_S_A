import pandas as pd
from models.dataset_model import DatasetModel
from config.config import DATASET_PATH

class DatasetController:
    def __init__(self):
        self.model = DatasetModel()

    def importar_viviendas(self):
    
        try:
            ids_insertados = self.model.insertar_viviendas()
            print(f"{len(ids_insertados)} viviendas insertadas.")
            return ids_insertados
        except Exception as e:
            print(f"Error al importar viviendas y tipos: {e}")
            return []
