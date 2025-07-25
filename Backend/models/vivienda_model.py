from Backend.models.base_model import BaseModel
from config.config import COLLECTION_NAME

class ViviendaModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
