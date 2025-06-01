from .Arma import Arma

class EspadaAltair(Arma):
    def __init__(self):
        """
        Inicializa la espada Altair con un nombre y un poder adicional.
        """
        super().__init__("Espada Altair", 2)

    def es_espada_altair(self):
        """
        Verifica si el arma es una espada Altair.
        """
        return True
