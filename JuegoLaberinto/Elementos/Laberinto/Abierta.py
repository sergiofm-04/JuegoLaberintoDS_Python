from .EstadoPuerta import EstadoPuerta

class Abierta(EstadoPuerta):
    """
    Define el estado de la puerta que permite el paso.
    """

    def abrir(self, una_puerta):
        """
        La puerta ya está abierta.
        """
        print("La puerta ya está abierta.")

    def cerrar(self, una_puerta):
        """
        Cierra la puerta y cambia su estado a Cerrada.
        """
        from .Cerrada import Cerrada
        print(f"{una_puerta} cerrada.")
        una_puerta.set_estado(Cerrada())

    def entrar(self, alguien, una_puerta):
        """
        Permite que alguien entre a través de la puerta.
        """
        una_puerta.puede_entrar(alguien)

    def esta_abierta(self):
        """
        Indica que la puerta está abierta.
        """
        return True
