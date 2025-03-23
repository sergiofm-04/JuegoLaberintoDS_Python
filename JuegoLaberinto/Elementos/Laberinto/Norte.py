from .Orientacion import Orientacion

class Norte(Orientacion):
    """
    Clase que representa la orientación Norte.
    Implementa el patrón Singleton para garantizar una única instancia.
    """

    _unica_instancia = None

    @classmethod
    def default(cls):
        """
        Devuelve la única instancia de Norte.
        Si no existe, la crea.
        """
        if cls._unica_instancia is None:
            cls._unica_instancia = cls.__new__(cls)
        return cls._unica_instancia

    def __new__(cls, *args, **kwargs):
        if cls._unica_instancia is None:
            cls._unica_instancia = super(Norte, cls).__new__(cls, *args, **kwargs)
        return cls._unica_instancia

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Norte.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.norte:
            posicion.norte.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Norte del contenedor.
        """
        return un_contenedor.norte

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Norte del contenedor.
        """
        en_un_contenedor.norte = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Norte.
        """
        if un_contenedor.norte:
            un_contenedor.norte.recorrer(un_bloque)
