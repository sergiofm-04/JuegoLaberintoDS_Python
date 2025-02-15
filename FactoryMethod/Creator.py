from Laberinto import Habitacion, Juego, Laberinto, Pared, Puerta

class Creator:
    """Clase Creator del patrón Factory Method."""

    def fabricar_habitacion(self, num):
        """
        Crea una habitación con paredes en todas las direcciones.
        
        :param num: Número identificador de la habitación.
        :return: Nueva instancia de Habitacion con paredes.
        """
        hab = Habitacion()
        hab.set_num(num)
        hab.set_este(self.fabricar_pared())
        hab.set_oeste(self.fabricar_pared())
        hab.set_norte(self.fabricar_pared())
        hab.set_sur(self.fabricar_pared())
        return hab

    def fabricar_juego(self):
        """Crea una nueva instancia de Juego."""
        return Juego()

    def fabricar_laberinto(self):
        """Crea una nueva instancia de Laberinto."""
        return Laberinto()

    def fabricar_pared(self):
        """Crea una nueva instancia de Pared."""
        return Pared()

    def fabricar_puerta(self):
        """Crea una nueva instancia de Puerta."""
        return Puerta()
