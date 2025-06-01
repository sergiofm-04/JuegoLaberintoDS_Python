from .Arma import Arma

class Vara(Arma):
    def __init__(self):
        """
        Inicializa la vara con un nombre y un poder adicional.
        """
        super().__init__("Vara", 10)

    def es_vara(self):
        """
        Verifica si el arma es una vara.
        """
        return True
