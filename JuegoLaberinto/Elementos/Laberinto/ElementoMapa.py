from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    """
    Interfaz común para los elementos del mapa.
    """

    def __init__(self):
        self.padre = None

    @abstractmethod
    def entrar(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    @abstractmethod
    def entrar_alguien(self, alguien):
        """
        Método abstracto que debe ser implementado por las subclases para indicar quién entra.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def es_habitacion(self):
        return False

    def es_pared(self):
        return False

    def es_puerta(self):
        return False

    def get_padre(self):
        return self.padre

    def set_padre(self, unObjeto):
        self.padre = unObjeto
