import ElementoMapa

class Habitacion(ElementoMapa):
    """Clase que representa una habitación en el laberinto."""

    def __init__(self, num):
        """Inicializa la habitación con su número y las conexiones a otras habitaciones."""
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self):
        """Imprime un mensaje indicando que el jugador ha entrado a la habitación."""
        print("Estás en la habitación.")

    # Métodos de acceso (getters y setters)
    def get_norte(self):
        return self.norte

    def set_norte(self, habitacion):
        self.norte = habitacion

    def get_sur(self):
        return self.sur

    def set_sur(self, habitacion):
        self.sur = habitacion

    def get_este(self):
        return self.este

    def set_este(self, habitacion):
        self.este = habitacion

    def get_oeste(self):
        return self.oeste

    def set_oeste(self, habitacion):
        self.oeste = habitacion

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num
