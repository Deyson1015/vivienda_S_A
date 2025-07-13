from models.vivienda_model import ViviendaModel
class ViviendaController:
    def __init__(self):
        self.model = ViviendaModel()

    def obtener_viviendas(self):
        try:
            viviendas = self.model.obtener_viviendas()
            print(f" Se obtuvieron {len(viviendas)} viviendas.")
            return viviendas
        except Exception as e:
            print(f" Error al obtener viviendas: {e}")
            return []

    def limpiar_viviendas(self):
        try:
            eliminados = self.model.eliminar_todo()
            print(f"Se eliminaron {eliminados} viviendas.")
            return eliminados
        except Exception as e:
            print(f"Error al eliminar viviendas: {e}")
            return 0
