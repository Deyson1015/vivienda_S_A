from bson.objectid import ObjectId
from Backend.models.vivienda_model import ViviendaModel
from config.config import COLLECTION_NAME_2

class TipoViviendaModel(ViviendaModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME_2)

    def insertar_tipo_unico(self, nombre):
        if self.collection.find_one({"nombre": nombre.upper()}) is None:
            self.collection.insert_one({"nombre": nombre.upper()})
    
    def obtener_id_web(self, tipo_id):
        try:
            return self.collection.find_one({"_id": ObjectId(tipo_id)})
        except Exception as e:
            print(f"Error al obtener tipo de vivienda por ID: {e}")
            return None
    
    def obtener_nombre_tipo(self, nombre):
        return self.collection.find_one({"nombre": nombre.upper()})
       
    def obtener_tipos(self):
        return list(self.collection.find())       