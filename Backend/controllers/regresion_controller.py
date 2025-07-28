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

    def mostrar_formulario_prediccion(self):
        # Carga la lista de tipos desde MongoDB
        tipos = self.tipo_model.listar_tipos()
        return render_template("predicciones.html", tipos_vivienda=tipos)

    def procesar_prediccion(self):
        area = request.form.get("area")
        tipo = request.form.get("tipo_vivienda")

        if not area or not tipo:
            return render_template("predicciones.html", error="Por favor complete todos los campos.")

        try:
            area = float(area)
        except ValueError:
            return render_template("predicciones.html", error="Área inválida. Debe ser un número.")

        df = self.base_model.obtener_dataframe()
        if df is None:
            return render_template("predicciones.html", error="No hay datos para predecir.")

        # Filtrar por tipo
        df_filtrado = df[df['tipo'] == tipo]

        if df_filtrado.empty:
            return render_template("predicciones.html", error=f"No hay datos para '{tipo}'.")

        # Dividir en X e y
        X = df_filtrado[['area']]
        y = df_filtrado['precio']

        # Entrenar y predecir
        modelo_temp = RegresionModel()
        modelo_temp.entrenar_modelo(X, y)
        
        input_df = pd.DataFrame([[area]], columns=["area"])

        # Realizar la predicción
        precio_estimado = modelo_temp.predecir(input_df)  
        
        precio_formateado = "${:,.0f}".format(precio_estimado).replace(",", ".")
        
        return render_template(
            "predicciones.html",
            tipos_vivienda=self.tipo_model.listar_tipos(),
            area=area,
            tipo_vivienda=tipo,
            prediccion=precio_formateado
        )
