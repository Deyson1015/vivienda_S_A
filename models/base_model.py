from data.conexion import Conexion

class BaseModel:
    def __init__(self, collection_name):
        db = Conexion().obtener_conexion()
        if db is not None:
            self.collection = db[collection_name]
        else:
            self.collection = None
            print("No se pudo obtener la colección.")

    def insertar_viviendas(self, datos):
        if self.collection is None:
            print("No se pudo obtener la colección de viviendas.")
            return []
        return self.collection.insert_many(datos).inserted_ids
        

    def obtener_viviendas(self):
        if self.collection is None:
            print("No se pudo obtener la colección de viviendas.")
            return []
        return list(self.collection.find())
    
    def eliminar_todo(self):
        if self.collection is None:
            print("No se pudo obtener la colección de viviendas.")
            return False
        resultado = self.collection.delete_many({})
        print(f"{resultado.deleted_count} documentos eliminados.")
        return resultado.deleted_count
