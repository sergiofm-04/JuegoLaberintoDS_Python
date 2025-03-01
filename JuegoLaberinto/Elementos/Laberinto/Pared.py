from .ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    """Clase que representa una pared en el laberinto."""

    def entrar(self):
        """Mensaje de colisión con la pared."""
        print("Te has chocado con una pared.")

    def entrar_alguien(self, alguien):
        return super().entrar_alguien(alguien)

    def es_pared(self):
        return True
