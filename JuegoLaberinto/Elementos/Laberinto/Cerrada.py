from .EstadoPuerta import EstadoPuerta

class Cerrada(EstadoPuerta):
    """
    Define el estado de la puerta que no permite el paso.
    """

    def abrir(self, una_puerta):
        """
        Abre la puerta y cambia su estado a Abierta.
        """
        from .Abierta import Abierta
        print(f"{una_puerta} abierta.")
        una_puerta.set_estado(Abierta())

    def cerrar(self, una_puerta):
        """
        La puerta ya está cerrada.
        """
        print("La puerta ya está cerrada.")

    def entrar(self, alguien, una_puerta):
        """
        Indica que alguien choca con la puerta cerrada.
        """
        print(f"{alguien} choca con puerta cerrada.")

    def __str__(self):
        return "Cerrada"
