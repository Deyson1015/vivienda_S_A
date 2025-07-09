# controllers/vivienda_controller.py
from models.vivienda_model import ViviendaModel
from data.conexion import Conexion

class ViviendaController:
    def __init__(self):
        self.model = ViviendaModel()
        self.conexion = Conexion()

    def guardar_datos_en_mongo(self):
        self.model.insertar_viviendas_en_mongo(self.conexion)

    def mostrar_resumen(self):
        resumen, total = self.model.obtener_resumen_estadistico()
        print(f"\nTotal de viviendas: {total}\n")
        print(resumen)
