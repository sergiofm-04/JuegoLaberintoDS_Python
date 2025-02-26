import Habitacion, Pared, Puerta, Laberinto

class Juego:
    """Clase principal del juego del laberinto."""

    def __init__(self):
        """Inicializa el juego sin un laberinto asignado."""
        self.laberinto = None

    def crear_laberinto_2_habitaciones(self):
        """Crea un laberinto con dos habitaciones conectadas por una puerta."""
        hab1 = Habitacion()
        hab1.set_num(1)
        hab1.set_este(Pared())
        hab1.set_oeste(Pared())
        hab1.set_norte(Pared())

        hab2 = Habitacion()
        hab2.set_num(2)
        hab2.set_sur(Pared())
        hab2.set_este(Pared())
        hab2.set_oeste(Pared())

        puerta = Puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        self.laberinto = Laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        return self.laberinto

    def crear_laberinto_2_habitaciones_fm(self, un_fm):
        """
        Crea un laberinto con dos habitaciones usando una fábrica de laberintos.

        :param un_fm: Instancia de una fábrica que genera elementos del laberinto.
        """
        hab1 = un_fm.fabricar_habitacion(1)
        hab2 = un_fm.fabricar_habitacion(2)

        puerta = un_fm.fabricar_puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        self.laberinto = un_fm.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        return self.laberinto

    def get_laberinto(self):
        """Devuelve la referencia al laberinto."""
        return self.laberinto

    def set_laberinto(self, laberinto):
        """Asigna un laberinto al juego."""
        self.laberinto = laberinto

    def obtener_habitacion(self, num):
        """Devuelve la habitación con el número dado, delegando en el laberinto."""
        return self.laberinto.obtener_habitacion(num) if self.laberinto else None
