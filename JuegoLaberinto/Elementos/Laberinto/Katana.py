from .Arma import Arma

class Katana(Arma):
    def __init__(self):
        """
        Inicializa la katana con un nombre y un poder adicional.
        """
        super().__init__("Katana", 3)

    def es_katana(self):
        """
        Verifica si el arma es una katana.
        """
        return True
