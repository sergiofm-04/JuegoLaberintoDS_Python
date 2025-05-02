from abc import ABC, abstractmethod

class EstadoPuerta(ABC):
    """
    Interfaz de los estados de la puerta.
    """

    @abstractmethod
    def abrir(self, una_puerta):
        """
        Define la acción de abrir la puerta.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def cerrar(self, una_puerta):
        """
        Define la acción de cerrar la puerta.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def entrar(self, alguien, una_puerta):
        """
        Define la acción de entrar a través de la puerta.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def esta_abierta(self):
        """
        Devuelve False por defecto, indicando que la puerta no está abierta.
        Las subclases pueden sobrescribir este método.
        """
        return False
