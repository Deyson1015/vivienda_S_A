from Backend.models.regresion_model import RegresionModel
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from Backend.controllers.dataset_controller import DatasetController
from flask import render_template, request
import pandas as pd


class RegresionController:
    def __init__(self):
        self.modelo = RegresionModel()
        self.base_model = DatasetController()
        self.tipo_model = TipoViviendaController()

    def entrenar_modelo(self):
        df = self.base_model.obtener_dataframe()
        if df is None:
            print(" No hay datos disponibles para entrenar el modelo.")
            return

        tipos = self.tipo_model.listar_tipos()
        if not tipos:
            print(" No hay tipos de vivienda disponibles.")
            return

        self.modelo.entrenar_modelo(df)
        print(" Modelo de regresión entrenado exitosamente.")


    def procesar_prediccion(self):
        area = request.form.get("area")
        habitaciones = request.form.get("habitaciones")

        if not area or not habitaciones:
            return render_template("predicciones.html", error="Por favor complete todos los campos.")

        try:
            area = float(area)
            habitaciones = int(habitaciones)
        except ValueError:
            return render_template("predicciones.html", error="Datos inválidos. Área debe ser número y habitaciones un entero.")

        # Obtener DataFrame
        df = self.base_model.obtener_dataframe()
        if df is None:
            return render_template("predicciones.html", error="No hay datos para predecir.")

        # Limpiar datos necesarios
        df_filtrado = df.dropna(subset=['area', 'habitaciones', 'precio'])

        # Preparar X e y
        X = df_filtrado[['area', 'habitaciones']]
        y = df_filtrado['precio']

        # Entrenar el modelo temporal
        self.modelo.entrenar_modelo(X, y)

        # Crear entrada
        entrada = pd.DataFrame([{'area': area, 'habitaciones': habitaciones}])

        # Predecir
        prediccion = self.modelo.predecir(entrada)[0]
        precio_formateado = "${:,.0f}".format(prediccion).replace(",", ".")


        return render_template(
            "predicciones.html",
            area=area,
            habitaciones=habitaciones,
            prediccion=precio_formateado
        )
