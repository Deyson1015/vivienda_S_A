import os

class FileUtil:
    @staticmethod

    def crear_carpetas():
        carpetas = [
            "static",                  
            "models/modelo",  
        ]

        for carpeta in carpetas:
            try:
                os.makedirs(carpeta, exist_ok=True)
                print(f"✅ Carpeta creada o ya existente: {carpeta}")
            except Exception as e:
                print(f"❌ Error al crear carpeta '{carpeta}': {e}")
