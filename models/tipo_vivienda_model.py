from bson.objectid import ObjectId
from models.base_model import BaseModel
from config.config import COLLECTION_NAME_2

class TipoViviendaModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME_2)

    def insertar_tipo_unico(self, nombre):
        if self.collection.find_one({"nombre": nombre.upper()}) is None:
            self.collection.insert_one({"nombre": nombre.upper()})

    def obtener_id(self, nombre):
        tipo = self.collection.find_one({"nombre": nombre.upper()})
        if not tipo:
            print(f" Tipo de vivienda '{nombre}' no encontrado.")
        return tipo["_id"] if tipo else None
    
    def obtener_tipos(self):
        if self.collection is None:
            print(" No se pudo obtener la colección de tipos de vivienda.")
            return []
        return list(self.collection.find())
         