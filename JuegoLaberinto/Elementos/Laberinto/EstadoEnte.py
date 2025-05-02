from abc import ABC, abstractmethod

class EstadoEnte(ABC):
    """
    Interfaz de los estados de un Ente (Vivo o Muerto).
    """

    @abstractmethod
    def actua(self, un_bicho):
        """
        Define la acción que realiza un bicho en este estado.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def atacar(self, alguien):
        """
        Define la acción de atacar en este estado.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")
