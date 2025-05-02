from .Forma import Forma

class Rombo(Forma):
    """
    Es una figura plana de cuatro lados. Es una implementación de los contenedores.
    """

    def __init__(self):
        """
        Inicializa un rombo con sus lados (noreste, noroeste, sureste, suroeste) como None.
        """
        super().__init__()
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None

    # Acceso
    def get_noreste(self):
        """
        Devuelve el lado noreste del rombo.
        """
        return self.noreste

    def set_noreste(self, an_object):
        """
        Establece el lado noreste del rombo.
        """
        self.noreste = an_object

    def get_noroeste(self):
        """
        Devuelve el lado noroeste del rombo.
        """
        return self.noroeste

    def set_noroeste(self, an_object):
        """
        Establece el lado noroeste del rombo.
        """
        self.noroeste = an_object

    def get_sureste(self):
        """
        Devuelve el lado sureste del rombo.
        """
        return self.sureste

    def set_sureste(self, an_object):
        """
        Establece el lado sureste del rombo.
        """
        self.sureste = an_object

    def get_suroeste(self):
        """
        Devuelve el lado suroeste del rombo.
        """
        return self.suroeste

    def set_suroeste(self, an_object):
        """
        Establece el lado suroeste del rombo.
        """
        self.suroeste = an_object
