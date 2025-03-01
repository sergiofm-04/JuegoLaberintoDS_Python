from .Orientacion import Orientacion

class Norte(Orientacion):
    """
    Clase que representa la orientación Norte.
    """

    def obtener_elemento_or_en(self, unContenedor):
        """Obtiene el elemento en la orientación Norte del contenedor."""
        return unContenedor.norte

    def poner_elemento(self, unEM, en_unContenedor):
        """Coloca un elemento en la orientación Norte del contenedor."""
        en_unContenedor.norte = unEM
