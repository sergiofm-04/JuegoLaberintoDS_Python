from .Contenedor import Contenedor

class Habitacion(Contenedor):
    """
    Clase Habitacion.
    """

    def __init__(self):
        super().__init__()

    # Consulta
    def es_habitacion(self):
        """Indica que este objeto es una habitación."""
        return True

    # Movimiento
    def ir_al_este(self, alguien):
        """Mueve a alguien al este."""
        if self.este:
            self.este.entrar(alguien)

    def ir_al_norte(self, alguien):
        """Mueve a alguien al norte."""
        if self.norte:
            self.norte.entrar(alguien)

    def ir_al_oeste(self, alguien):
        """Mueve a alguien al oeste."""
        if self.oeste:
            self.oeste.entrar(alguien)

    def ir_al_sur(self, alguien):
        """Mueve a alguien al sur."""
        if self.sur:
            self.sur.entrar(alguien)

    # Impresión
    def __str__(self):
        """Devuelve una representación en texto de la habitación."""
        return f"Hab{self.num}"
