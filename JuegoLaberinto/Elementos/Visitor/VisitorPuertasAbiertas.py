from .Visitor import Visitor

class VisitorPuertasAbiertas(Visitor):
    """
    Visitor que comprueba si todas las puertas del laberinto están abiertas.
    """

    def __init__(self):
        self.todas_abiertas = True

    def visitar_puerta(self, una_puerta):
        if not una_puerta.esta_abierta():
            self.todas_abiertas = False

    def resultado(self):
        return self.todas_abiertas
