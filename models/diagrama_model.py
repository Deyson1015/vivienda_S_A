from models.base_model import BaseModel
from config.config import COLLECTION_NAME

class DiagramaModel(BaseModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
