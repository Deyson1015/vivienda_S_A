import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuraciones de conexión a la base de datos
MONGO_URL = os.getenv('MONGO_URL')  
DB_NAME = os.getenv('DB_NAME')  
COLLECTION_NAME = os.getenv('COLLECTION_NAME')  
COLLECTION_NAME_2 = os.getenv('COLLECTION_NAME_2')  
DATASET_PATH = os.getenv('DATASET_PATH')