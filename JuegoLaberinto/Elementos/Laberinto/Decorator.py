from .Hoja import Hoja

class Decorator(Hoja):
    """
    Decorator es la interfaz común de los decoradores.
    """

    def __init__(self, em=None):
        self.em = em

    def get_em(self):
        return self.em

    def set_em(self, anObject):
        self.em = anObject
