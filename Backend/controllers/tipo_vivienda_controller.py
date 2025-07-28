from Backend.models.tipo_vivienda_model import TipoViviendaModel
from bson import ObjectId
class TipoViviendaController:
    def __init__(self):
        self.model = TipoViviendaModel()

    def insertar_tipo(self, nombre):
        if not nombre:
            print(" El nombre del tipo de vivienda no puede estar vacío.")
            return
        self.model.insertar_tipo_unico(nombre)
        print(f"Tipo de vivienda '{nombre}' insertado.")

    def obtener_id_tipo(self, nombre):
        if not nombre:
            print("El nombre del tipo no puede estar vacío.")
            return None
        return self.model.obtener_id_web(nombre)
    
    def obtener_id_tipo_web(self, nombre_tipo):
        try:
            tipo = self.model.obtener_nombre_tipo(nombre_tipo)
            if tipo:
                return tipo["_id"]
            else:
                print(f"No se encontró el tipo de vivienda '{nombre_tipo}'.")
                return None
        except Exception as e:
            print(f"Error al obtener el tipo de vivienda por nombre: {e}")
            return None

    def listar_tipos(self):
        tipos = self.model.obtener_tipos()
        if not tipos:
            print("No hay tipos de vivienda registrados.")
        else:
            print("Tipos de vivienda disponibles:")
            for tipo in tipos:
                print(f"- {tipo['nombre']}")
        return tipos
    
    def limpiar_tipos(self):
        try:
            eliminados = self.model.eliminar_todo()
            print(f"Se eliminaron {eliminados} tipo de viviendas.")
            return eliminados
        except Exception as e:
            print(f"Error al eliminar viviendas: {e}")
            return 0
