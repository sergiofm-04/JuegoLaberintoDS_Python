from .Arma import Arma

class Daga(Arma):
    def __init__(self):
        """
        Inicializa la daga con un nombre y un poder adicional.
        """
        super().__init__("Daga", 1)

    def es_daga(self):
        """
        Verifica si el arma es una daga.
        """
        return True
