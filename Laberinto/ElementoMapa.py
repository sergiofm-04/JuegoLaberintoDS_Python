from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    """Interfaz común de los elementos del mapa."""

    @abstractmethod
    def entrar(self):
        """Debe ser implementado por las subclases."""
        pass
