from Backend.models.estadisticas_model import EstadisticasViviendaModel
from Backend.controllers.tipo_vivienda_controller import TipoViviendaController
from Backend.controllers.dataset_controller import DatasetController
from Backend.models.regresion_model import RegresionModel
from Backend.utils.data_util import DataUtil
from flask import render_template

class EstadisticasController:
    def __init__(self):
        self.vivienda_model = EstadisticasViviendaModel()
        self.tipo_model = TipoViviendaController()
        self.model = DatasetController()
        self.regresion_model = RegresionModel()
        
    def _cargar_dataframe(self):
        viviendas = self.vivienda_model.obtener_viviendas()
        tipos = self.tipo_model.listar_tipos()

        if not viviendas or not tipos:
            return None, None

        df = DataUtil.preparar_dataframe(viviendas, tipos)
        return df, tipos
    
    def mostrar_resumen_web(self):
        try:
            df, tipos = self._cargar_dataframe()
            if df is None:
                return render_template("estadisticas.html")
            resumen = DataUtil.generar_estadisticas(df, modo='resumen')

            return render_template("estadisticas.html", df=df, tipos=tipos, resumen=resumen)

        except Exception as e:
            print(f"Error al mostrar el resumen: {e}")
            return render_template("estadisticas.html")


    def mostrar_dashboard(self):
        try:
            df, _ = self._cargar_dataframe()
            if df is None:
                return render_template("dashboard.html")

            dashboard = DataUtil.generar_estadisticas(df, modo='dashboard')

            return render_template("dashboard.html", dashboard=dashboard, df=df)

        except Exception as e:
            print(f"Error al mostrar el dashboard: {e}")
            return render_template("dashboard.html")
