from Backend.models.tipo_vivienda_model import TipoViviendaModel

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
        return self.model.obtener_id(nombre)
    
    def obtener_nombre_tipo(self, nombre):
        if not nombre:
            print("El nombre del tipo no puede estar vacío.")
            return None
        tipo = self.model.obtener_nombre_tipo(nombre)
        return tipo["nombre"] if tipo else nombre


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
