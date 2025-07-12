import unicodedata

class TextoUtil:
    @staticmethod
    def limpiar_descripcion(texto):
        """
        Limpia la descripción: convierte a minúsculas, elimina tildes
        y retorna la primera palabra. Si no es texto válido, retorna cadena vacía.
        """
        if not isinstance(texto, str):
            return ""
        texto_normalizado = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("utf-8")
        palabras = texto_normalizado.strip().split()
        return palabras[0].lower() if palabras else ""
