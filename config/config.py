import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuraciones de conexión a la base de datos
MONGO_URL = os.getenv('MONGO_URL')  # URI de conexión por defecto si no se encuentra en .env
DB_NAME = os.getenv('DB_NAME')  # Nombre de la base de datos
COLLECTION_NAME = os.getenv('COLLECTION_NAME')  # Nombre de la colección
COLLECTION_NAME_2 = os.getenv('COLLECTION_NAME_2')  # Nombre de la segunda colección