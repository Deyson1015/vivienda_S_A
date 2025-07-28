import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from config.config import MODEL_PATH

class RegresionModel:
    def __init__(self):
        self.model_path = MODEL_PATH
        self.model = None

    def entrenar_modelo(self, X, y):
        modelo = LinearRegression()
        modelo.fit(X, y)
        self.model = modelo

        with open(self.model_path, "wb") as f:
            pickle.dump(modelo, f)

        return modelo

    def cargar_modelo(self):
        if self.model is None:
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        return self.model

    def predecir(self, entrada):
        modelo = self.cargar_modelo()
        return modelo.predict(entrada)

