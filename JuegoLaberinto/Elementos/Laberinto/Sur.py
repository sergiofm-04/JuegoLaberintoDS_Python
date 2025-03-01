from .Orientacion import Orientacion

class Sur(Orientacion):
    """
    Clase que representa la orientación Sur.
    """

    def obtener_elemento_or_en(self, unContenedor):
        """Obtiene el elemento en la orientación Sur del contenedor."""
        return unContenedor.sur

    def poner_elemento(self, unEM, en_unContenedor):
        """Coloca un elemento en la orientación Sur del contenedor."""
        en_unContenedor.sur = unEM
