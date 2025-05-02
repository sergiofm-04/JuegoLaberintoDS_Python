from .Comando import Comando

class Abrir(Comando):
    """
    Abrir representa la petición de abrir de los elementos del mapa.
    """

    def ejecutar(self, alguien):
        """
        Ejecuta el comando de abrir en el receptor.
        """
        if self.receptor:
            self.receptor.abrir()
