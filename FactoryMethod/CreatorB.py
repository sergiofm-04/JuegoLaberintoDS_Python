import Creator
from Laberinto import ParedBomba

class CreatorB(Creator):
    """CreatorB crea laberintos con ParedBomba en lugar de Pared."""

    def fabricar_pared(self):
        """Crea una instancia de ParedBomba en lugar de Pared."""
        return ParedBomba()
