from .EstadoEnte import EstadoEnte

class Vivo(EstadoEnte):
    """
    Define el estado del Ente con vidas > 0.
    """

    def actua(self, un_bicho):
        """
        Permite que el bicho actúe si está vivo.
        """
        un_bicho.puede_actuar()

    def atacar(self, alguien):
        """
        Permite que el ente ataque si está vivo.
        """
        alguien.puede_atacar()
