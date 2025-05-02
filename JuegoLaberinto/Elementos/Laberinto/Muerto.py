from .EstadoEnte import EstadoEnte

class Muerto(EstadoEnte):
    """
    Define el estado del Ente con vidas=0.
    """

    def actua(self, un_bicho):
        """
        Los muertos no actúan.
        """
        pass

    def atacar(self, alguien):
        """
        Los muertos no atacan.
        """
        pass
