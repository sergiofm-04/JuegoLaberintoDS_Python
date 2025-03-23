from ..Laberinto.Bicho import Bicho
from ..Laberinto.Agresivo import Agresivo
from ..Laberinto.Perezoso import Perezoso
from ..Laberinto.Bomba import Bomba
from ..Laberinto.Habitacion import Habitacion
from ..Laberinto.Juego import Juego
from ..Laberinto.Laberinto import Laberinto
from ..Laberinto.Norte import Norte
from ..Laberinto.Sur import Sur
from ..Laberinto.Este import Este
from ..Laberinto.Oeste import Oeste
from ..Laberinto.Pared import Pared
from ..Laberinto.Puerta import Puerta

class Creator:
    """Clase Creator del patrón Factory Method."""

    def cambiar_a_modo_agresivo(self, unBicho):
        """Cambia el modo de un bicho a agresivo."""
        unBicho.modo = Agresivo()
        unBicho.poder = 10

    def fabricar_bicho_agresivo(self):
        """Fabrica un bicho agresivo."""
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricar_bicho_agresivo_en_habitacion(self, unaHab):
        """Fabrica un bicho agresivo en una habitación específica."""
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        bicho.posicion = unaHab
        return bicho

    def fabricar_bicho_perezoso(self):
        """Fabrica un bicho perezoso."""
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.poder = 5
        bicho.vidas = 1
        return bicho
    
    def fabricar_bicho_perezoso_en_habitacion(self, unaHab):
        """Fabrica un bicho perezoso en una habitación específica."""
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 1
        bicho.poder = 1
        bicho.posicion = unaHab
        return bicho

    def fabricar_bomba(self):
        """Crea una nueva instancia de Bomba."""
        return Bomba()

    """def fabricar_este(self):
        # Crea una nueva instancia de Este.
        return Este()"""
    
    def fabricar_este(self):
        """Crea una nueva instancia de Este."""
        return Este.default()

    def fabricar_habitacion(self, num):
        """Crea una habitación con paredes en todas las direcciones."""
        hab = Habitacion()
        hab.num = num
        hab.agregar_orientacion(self.fabricar_norte())
        hab.agregar_orientacion(self.fabricar_sur())
        hab.agregar_orientacion(self.fabricar_este())
        hab.agregar_orientacion(self.fabricar_oeste())
        for orientacion in hab.orientaciones:
            hab.poner_en_or(orientacion, self.fabricar_pared())
        return hab

    def fabricar_juego(self):
        """Crea una nueva instancia de Juego."""
        return Juego()

    def fabricar_laberinto(self):
        """Crea una nueva instancia de Laberinto."""
        return Laberinto()

    """def fabricar_norte(self):
        # Crea una nueva instancia de Norte.
        return Norte()"""

    """def fabricar_oeste(self):
        # Crea una nueva instancia de Oeste.
        return Oeste()"""
    
    def fabricar_norte(self):
        """Crea una nueva instancia de Norte."""
        return Norte.default()

    def fabricar_oeste(self):
        """Crea una nueva instancia de Oeste."""
        return Oeste.default()

    def fabricar_pared(self):
        """Crea una nueva instancia de Pared."""
        return Pared()

    def fabricar_puerta(self):
        """Crea una nueva instancia de Puerta."""
        return Puerta()

    """def fabricar_sur(self):
        # Crea una nueva instancia de Sur.
        return Sur()"""
    
    def fabricar_sur(self):
        """Crea una nueva instancia de Sur."""
        return Sur.default()
