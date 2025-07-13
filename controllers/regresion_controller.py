from models.regresion_model import RegresionModel
from models.tipo_vivienda_model import TipoViviendaModel
from models.base_model import BaseModel
from utils.data_util import DataUtil
from config.config import COLLECTION_NAME

class RegresionController:
    def __init__(self):
        self.modelo = RegresionModel()
        self.base_model = BaseModel(COLLECTION_NAME)
        self.tipo_model = TipoViviendaModel()

    def entrenar_modelo(self):
        try:
            viviendas = self.base_model.obtener_viviendas()
            tipos = self.tipo_model.obtener_tipos()
            
            df = DataUtil.preparar_dataframe(viviendas, tipos)
            if df is None:
                print(" No se pudo preparar el DataFrame.")
                return

            X = df[["area"]].values
            y = df["precio"].values

            self.modelo.entrenar_modelo(X, y)
            print("✅ Modelo entrenado y guardado correctamente.")
        except Exception as e:
            print(f" Error al entrenar el modelo: {e}")
