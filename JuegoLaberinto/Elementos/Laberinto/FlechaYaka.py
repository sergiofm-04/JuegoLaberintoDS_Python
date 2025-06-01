from .Arma import Arma

class FlechaYaka(Arma):
    def __init__(self):
        """
        Inicializa la flecha Yaka con un nombre y un poder adicional.
        """
        super().__init__("Flecha Yaka", 2)

    def es_flecha_yaka(self):
        """
        Verifica si el arma es una flecha Yaka.
        """
        return True
