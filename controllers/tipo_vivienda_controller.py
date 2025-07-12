from models.tipo_vivienda_model import TipoViviendaModel

class TipoViviendaController:
    def __init__(self):
        self.model = TipoViviendaModel()

    def obtener_tipo_vivienda(self):
        try:
            viviendas = self.model.obtener_viviendas()
            print(f" Se obtuvieron {len(viviendas)} viviendas.")
            return viviendas
        except Exception as e:
            print(f" Error al obtener viviendas: {e}")
            return []

    def eliminar_tipos(self):
        try:
            eliminados = self.model.eliminar_todo()
            print(f"Se eliminaron {eliminados} tipo viviendas.")
            return eliminados
        except Exception as e:
            print(f"Error al eliminar viviendas: {e}")
            return 0
