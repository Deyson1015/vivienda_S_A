from models.base_model import BaseModel
from config.config import COLLECTION_NAME  

class DatasetModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)

    def insertar_viviendas(self, viviendas):
        if self.collection:
            resultado = self.collection.insert_many(viviendas)
            return resultado.inserted_ids
        else:
            print(" No se pudo insertar el dataset.")
            return []

    def contar_viviendas(self):
        if self.collection:
            return self.collection.count_documents({})
        else:
            print("No se pudo contar documentos.")
            return 0

