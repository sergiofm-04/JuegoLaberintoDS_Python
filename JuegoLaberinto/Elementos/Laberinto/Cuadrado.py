from .Forma import Forma

class Cuadrado(Forma):
    """
    Es una figura plana de cuatro lados. Es una implementación de los contenedores.
    """

    def __init__(self):
        """
        Inicializa un cuadrado con sus lados (norte, sur, este, oeste) como None.
        """
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    # Movimiento
    def ir_al_este(self, alguien):
        """
        Mueve a alguien al este.
        """
        if self.este:
            self.este.entrar(alguien)

    def ir_al_norte(self, alguien):
        """
        Mueve a alguien al norte.
        """
        if self.norte:
            self.norte.entrar(alguien)

    def ir_al_oeste(self, alguien):
        """
        Mueve a alguien al oeste.
        """
        if self.oeste:
            self.oeste.entrar(alguien)

    def ir_al_sur(self, alguien):
        """
        Mueve a alguien al sur.
        """
        if self.sur:
            self.sur.entrar(alguien)

    # Acceso
    def get_norte(self):
        """
        Devuelve el lado norte del cuadrado.
        """
        return self.norte

    def set_norte(self, an_object):
        """
        Establece el lado norte del cuadrado.
        """
        self.norte = an_object

    def get_sur(self):
        """
        Devuelve el lado sur del cuadrado.
        """
        return self.sur

    def set_sur(self, an_object):
        """
        Establece el lado sur del cuadrado.
        """
        self.sur = an_object

    def get_este(self):
        """
        Devuelve el lado este del cuadrado.
        """
        return self.este

    def set_este(self, an_object):
        """
        Establece el lado este del cuadrado.
        """
        self.este = an_object

    def get_oeste(self):
        """
        Devuelve el lado oeste del cuadrado.
        """
        return self.oeste

    def set_oeste(self, an_object):
        """
        Establece el lado oeste del cuadrado.
        """
        self.oeste = an_object
