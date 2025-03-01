from .Orientacion import Orientacion

class Este(Orientacion):
    """
    Clase que representa la orientación Este.
    """

    def obtener_elemento_or_en(self, unContenedor):
        """Obtiene el elemento en la orientación Este del contenedor."""
        return unContenedor.este

    def poner_elemento(self, unEM, en_unContenedor):
        """Coloca un elemento en la orientación Este del contenedor."""
        en_unContenedor.este = unEM
