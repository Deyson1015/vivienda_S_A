from bson.objectid import ObjectId
from models.base_model import BaseModel
from config.config import COLLECTION_NAME_2

class TipoViviendaModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME_2)

    def insertar_tipo_unico(self, tipo_nombre):
        if self.collection.find_one({"nombre": tipo_nombre}) is None:
            self.collection.insert_one({"nombre": tipo_nombre})

    def obtener_id(self, tipo_nombre):
        tipo = self.collection.find_one({"nombre": tipo_nombre})
        return tipo["_id"] if tipo else None
