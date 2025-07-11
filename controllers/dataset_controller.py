import pandas as pd
from models.dataset_model import DatasetModel
from config.config import EXCEL_DATASET_PATH

class DatasetController:
    def __init__(self):
        self.model = DatasetModel()

    def importar_dataset(self):
        try:
            df = pd.read_excel(EXCEL_DATASET_PATH)
            datos = df.to_dict(orient="records")
            resultado = self.model.insertar_viviendas(datos)
            print(f"{len(resultado)} viviendas insertadas.")
            return resultado
        except Exception as e:
            print(f"Error al importar dataset: {e}")
            return []
