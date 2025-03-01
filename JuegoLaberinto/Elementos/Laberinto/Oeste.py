from .Orientacion import Orientacion

class Oeste(Orientacion):
    """
    Clase que representa la orientación Oeste.
    """

    def obtener_elemento_or_en(self, unContenedor):
        """Obtiene el elemento en la orientación Oeste del contenedor."""
        return unContenedor.oeste

    def poner_elemento(self, unEM, en_unContenedor):
        """Coloca un elemento en la orientación Oeste del contenedor."""
        en_unContenedor.oeste = unEM
