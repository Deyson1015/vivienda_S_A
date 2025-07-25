from Backend.models.regresion_model import RegresionModel
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from Backend.controllers.dataset_controller import DatasetController

class RegresionController:
    def __init__(self):
        self.modelo = RegresionModel()
        self.base_model = DatasetController()
        self.tipo_model = TipoViviendaController()

    def entrenar_modelo(self):
        df = self.base_model.obtener_dataframe()
        if df is None:
            print(" No hay datos disponibles para entrenar el modelo.")
            return

        tipos = self.tipo_model.listar_tipos()
        if not tipos:
            print(" No hay tipos de vivienda disponibles.")
            return

        self.modelo.entrenar_modelo(df)
        print(" Modelo de regresión entrenado exitosamente.")
        
