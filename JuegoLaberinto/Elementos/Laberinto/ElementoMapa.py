from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    """
    Es la interfaz común de los elementos del mapa.
    """

    def __init__(self):
        self.padre = None
        self.comandos = []

    # Métodos abstractos
    @abstractmethod
    def entrar(self, alguien):
        """
        Método abstracto que debe ser implementado por las subclases para indicar quién entra.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def aceptar(self, un_visitor):
        """
        Método abstracto para aceptar un visitante (Visitor Pattern).
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    # Métodos de consulta
    def es_armario(self):
        return False

    def es_bomba(self):
        return False

    def es_habitacion(self):
        return False

    def es_pared(self):
        return False

    def es_puerta(self):
        return False

    def es_tunel(self):
        return False

    # Métodos de acceso
    def get_padre(self):
        return self.padre

    def set_padre(self, un_objeto):
        self.padre = un_objeto

    def get_comandos(self):
        return self.comandos

    def set_comandos(self, comandos):
        self.comandos = comandos

    # Métodos de comandos
    def agregar_comando(self, un_comando):
        """
        Agrega un comando a la lista de comandos.
        """
        self.comandos.append(un_comando)

    def eliminar_comando(self, un_comando):
        """
        Elimina un comando de la lista de comandos.
        """
        try:
            self.comandos.remove(un_comando)
        except ValueError:
            print("No existe ese comando.")

    def obtener_comandos(self):
        """
        Devuelve la lista de comandos.
        """
        return self.comandos

    # Recorrido
    def recorrer(self, un_bloque):
        """
        Aplica un bloque de código (función) al elemento actual.
        """
        un_bloque(self)
