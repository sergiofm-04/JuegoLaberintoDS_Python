from .LaberintoBuilder import LaberintoBuilder
from ..Laberinto.Rombo import Rombo
from ..Laberinto.Noreste import Noreste
from ..Laberinto.Noroeste import Noroeste
from ..Laberinto.Sureste import Sureste
from ..Laberinto.Suroeste import Suroeste

class LaberintoBuilderRombo(LaberintoBuilder):
    """
    Builder para los laberintos con forma de rombo.
    """

    def fabricar_forma(self):
        """
        Fabrica la forma del rombo con sus orientaciones específicas.
        """
        forma = Rombo()
        forma.agregar_orientacion(self.fabricar_noreste())
        forma.agregar_orientacion(self.fabricar_sureste())
        forma.agregar_orientacion(self.fabricar_noroeste())
        forma.agregar_orientacion(self.fabricar_suroeste())
        return forma

    def fabricar_noreste(self):
        """
        Fabrica la orientación noreste.
        """
        return Noreste()

    def fabricar_noroeste(self):
        """
        Fabrica la orientación noroeste.
        """
        return Noroeste()

    def fabricar_sureste(self):
        """
        Fabrica la orientación sureste.
        """
        return Sureste()

    def fabricar_suroeste(self):
        """
        Fabrica la orientación suroeste.
        """
        return Suroeste()
