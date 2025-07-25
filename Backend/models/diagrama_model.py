from Backend.models.vivienda_model import ViviendaModel
from config.config import COLLECTION_NAME

class DiagramaModel(ViviendaModel):
    def __init__(self):
        super().__init__(COLLECTION_NAME)
