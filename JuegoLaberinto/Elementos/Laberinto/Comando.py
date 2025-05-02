class Comando:
    """
    Comando es la interfaz de los comandos del laberinto.
    """

    def __init__(self):
        self.receptor = None

    # Métodos de acceso
    def get_receptor(self):
        """
        Devuelve el receptor del comando.
        """
        return self.receptor

    def set_receptor(self, receptor):
        """
        Establece el receptor del comando.
        """
        self.receptor = receptor
