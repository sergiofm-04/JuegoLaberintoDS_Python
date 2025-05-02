from .Visitor import Visitor

class VisitorActivarBombas(Visitor):
    """
    VisitorActivarBombas es un visitor que activa bombas.
    """

    def visitar_bomba(self, una_bomba):
        """
        Activa una bomba.
        """
        una_bomba.activar()
