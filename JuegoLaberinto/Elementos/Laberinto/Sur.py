from .Orientacion import Orientacion

class Sur(Orientacion):
    """
    Clase que representa la orientación Sur.
    Implementa el patrón Singleton para garantizar una única instancia.
    """

    _unica_instancia = None

    @classmethod
    def default(cls):
        """
        Devuelve la única instancia de Sur.
        Si no existe, la crea.
        """
        if cls._unica_instancia is None:
            cls._unica_instancia = cls.__new__(cls)
        return cls._unica_instancia

    def __new__(cls, *args, **kwargs):
        if cls._unica_instancia is None:
            cls._unica_instancia = super(Sur, cls).__new__(cls, *args, **kwargs)
        return cls._unica_instancia

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Sur.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.sur:
            posicion.sur.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Sur del contenedor.
        """
        return un_contenedor.sur

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Sur del contenedor.
        """
        en_un_contenedor.sur = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Sur.
        """
        if un_contenedor.sur:
            un_contenedor.sur.recorrer(un_bloque)
