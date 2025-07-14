from models.estadisticas_model import EstadisticasViviendaModel
from controllers.tipo_vivienda_controller import TipoViviendaController
from controllers.dataset_controller import DatasetController
from utils.data_util import DataUtil
from models.regresion_model import RegresionModel 

class EstadisticasController:
    def __init__(self):
        self.vivienda_model = EstadisticasViviendaModel()
        self.tipo_model = TipoViviendaController()
        self.model = DatasetController()
        self.regresion_model = RegresionModel()

    def mostrar_resumen(self):
        try:
            viviendas = self.vivienda_model.obtener_viviendas()
            if not viviendas:
                print("No hay datos de viviendas disponibles.")
                return

            tipos = self.tipo_model.listar_tipos()
            if not tipos:
                print("No hay tipos de vivienda disponibles.")
                return

            df = DataUtil.preparar_dataframe(viviendas, tipos)
            DataUtil.resumir_estadisticas(df, self.regresion_model)

        except Exception as e:
            print(f"Error al mostrar el resumen de estadísticas: {e}")
