# views/app.py
from controllers.vivienda_controller import ViviendaController

def main():
    controller = ViviendaController()

    # 1. Guardar en MongoDB
    controller.guardar_datos_en_mongo()

    # 2. Mostrar resumen estadístico
    controller.mostrar_resumen()

if __name__ == "__main__":
    main()



