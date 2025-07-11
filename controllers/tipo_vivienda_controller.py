from models.tipo_vivienda_model import TipoViviendaModel

class ViviendaController:
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

    def insertar_tipo_vivienda(self, vivienda):
        try:
            if isinstance(vivienda, dict):
                self.model.insertar_viviendas(vivienda)
                print("Vivienda insertada correctamente.")
            else:
                print("La vivienda debe ser un diccionario válido.")
        except Exception as e:
            print(f" Error al insertar vivienda: {e}")
