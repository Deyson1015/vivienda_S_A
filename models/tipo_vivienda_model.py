from models.base_model import BaseModel
from config.config import COLLECTION_NAME_2

class TipoViviendaModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME_2)

