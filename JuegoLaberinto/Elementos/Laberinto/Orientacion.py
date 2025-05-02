from abc import ABC, abstractmethod

class Orientacion(ABC):
    """
    Interfaz común para las orientaciones.
    """

    @abstractmethod
    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina en esta orientación.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en esta orientación dentro de un contenedor.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en esta orientación dentro de un contenedor.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) a esta orientación dentro de un contenedor.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")
