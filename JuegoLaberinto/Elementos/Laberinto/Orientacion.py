from abc import ABC, abstractmethod

class Orientacion(ABC):
    """
    Interfaz común para las orientaciones.
    """

    @abstractmethod
    def poner_elemento(self, unEM, en_unContenedor):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Subclasses should implement this!")
