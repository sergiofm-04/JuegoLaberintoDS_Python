from .Contenedor import Contenedor

class Armario(Contenedor):
    """
    Es un contenedor que representa un armario en el laberinto.
    """

    def es_armario(self):
        """
        Indica que este contenedor es un armario.
        """
        return True

    def visitar_contenedor(self, un_visitor):
        """
        Permite que un visitante interactúe con el armario.
        """
        un_visitor.visitar_armario(self)
