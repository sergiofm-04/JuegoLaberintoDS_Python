from .ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    """Clase que representa una puerta en el laberinto."""

    def __init__(self):
        """Inicializa la puerta cerrada y sin lados asignados."""
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def entrar(self):
        """Indica si la puerta está abierta o cerrada."""
        if self.abierta:
            print("La puerta está abierta.")
        else:
            print("La puerta está cerrada.")

    def entrar_alguien(self, alguien):
        pass

    def get_abierta(self):
        """Devuelve el estado de la puerta (abierta o cerrada)."""
        return self.abierta

    def set_abierta(self, estado):
        """Cambia el estado de la puerta."""
        self.abierta = estado

    def es_puerta(self):
        return True

    def get_lado1(self):
        """Devuelve el primer lado de la puerta."""
        return self.lado1

    def set_lado1(self, habitacion):
        """Asigna el primer lado de la puerta a una habitación."""
        self.lado1 = habitacion

    def get_lado2(self):
        """Devuelve el segundo lado de la puerta."""
        return self.lado2

    def set_lado2(self, habitacion):
        """Asigna el segundo lado de la puerta a una habitación."""
        self.lado2 = habitacion
