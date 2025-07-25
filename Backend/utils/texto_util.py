import unicodedata

class TextoUtil:
    @staticmethod
    def limpiar_descripcion(texto):
        if not isinstance(texto, str):
            return ""
        texto_normalizado = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("utf-8")
        palabras = texto_normalizado.strip().split()
        return palabras[0].lower() if palabras else ""
