import random
from .Contenedor import Contenedor

class Cofre(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def abrir(self, personaje):
        """
        Abre el cofre si la llave es válida y proporciona un arma aleatoria.
        """

        arma = random.choice(self.hijos)
        personaje.recoger_arma(arma)
        print(f"El cofre {self.num} ha sido abierto. {personaje.nombre} ha obtenido {arma}.")
    
    def visitar_contenedor(self, un_visitor):
        pass

    def es_cofre(self):
        """
        Indica que este objeto es un cofre.
        """
        return True
