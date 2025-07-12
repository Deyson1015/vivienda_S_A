from pymongo import MongoClient, errors
from config.config import MONGO_URL, DB_NAME

class Conexion:
    def __init__(self):
        try:
            self.cliente = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
            self.db = self.cliente[DB_NAME]
            # Prueba de conexión
            self.cliente.server_info()
        except errors.ServerSelectionTimeoutError as e:
            print("Error de conexión a MongoDB.")
            print(f"Detalles: {e}")
            self.db = None

    def obtener_conexion(self):
        return self.db