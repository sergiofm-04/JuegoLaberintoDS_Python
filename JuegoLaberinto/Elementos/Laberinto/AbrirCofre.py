from .Comando import Comando
from .Cofre import Cofre

class AbrirCofre(Comando):
    """
    AbrirCofre representa la petición de abrir un cofre en el laberinto.
    """

    def ejecutar(self, personaje):
        """
        Ejecuta el comando de abrir el cofre con la llave proporcionada.
        """
        if isinstance(self.receptor, Cofre):
            self.receptor.abrir(personaje)
        else:
            print("El receptor no es un cofre.")
