from pymongo import MongoClient

class Conexion:
    def __init__(self, db_name, collection_name):
        self.cliente = MongoClient('mongodb://localhost:27017/')
        self.db = self.cliente[db_name] 
        self.collection = self.db[collection_name] 

    def insertar(self, document):
        self.collection.insert_one(document)

    def obtener_viviendas(self):
        return list(self.collection.find())
