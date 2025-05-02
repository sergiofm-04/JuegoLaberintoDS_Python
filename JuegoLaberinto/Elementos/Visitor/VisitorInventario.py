from .Visitor import Visitor

class VisitorInventario(Visitor):
    """
    VisitorInventario sirve para mostrar información de los elementos visitados.
    """

    def visitar_armario(self, un_armario):
        """
        Muestra información del armario visitado.
        """
        print(f"{un_armario}")

    def visitar_bomba(self, una_bomba):
        """
        Muestra información de la bomba visitada.
        """
        print(f"{una_bomba}")

    def visitar_habitacion(self, una_habitacion):
        """
        Muestra información de la habitación visitada.
        """
        print(f"{una_habitacion}")

    def visitar_pared(self, una_pared):
        """
        Muestra información de la pared visitada.
        """
        print(f"{una_pared}")

    def visitar_puerta(self, una_puerta):
        """
        Muestra información de la puerta visitada.
        """
        print(f"{una_puerta}")

    def visitar_tunel(self, un_tunel):
        """
        Muestra información del túnel visitado.
        """
        print(f"{un_tunel}")
