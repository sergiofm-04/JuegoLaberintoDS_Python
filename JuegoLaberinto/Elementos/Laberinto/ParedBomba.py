from .Pared import Pared

class ParedBomba(Pared):
    """Clase que representa una pared bomba en el laberinto."""

    def __init__(self):
        """Inicializa la pared bomba como inactiva."""
        # super().__init__()
        self.activa = False

    def entrar(self):
        """Mensaje de colisión con la pared bomba."""
        print("Te has chocado con una pared bomba.")

    def get_activa(self):
        """Devuelve el estado de la pared bomba."""
        return self.activa

    def set_activa(self, estado):
        """Cambia el estado de la pared bomba."""
        self.activa = estado
