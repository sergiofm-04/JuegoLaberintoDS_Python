from .Comando import Comando

class Entrar(Comando):
    """
    Entrar representa la petición de entrar de los elementos del mapa.
    """

    def ejecutar(self, alguien):
        """
        Ejecuta el comando de entrar en el receptor.
        """
        if self.receptor:
            self.receptor.entrar(alguien)
