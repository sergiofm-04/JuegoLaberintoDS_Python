from .Orientacion import Orientacion

class Oeste(Orientacion):
    """
    Clase que representa la orientación Oeste.
    Implementa el patrón Singleton para garantizar una única instancia.
    """

    _unica_instancia = None

    @classmethod
    def default(cls):
        """
        Devuelve la única instancia de Oeste.
        Si no existe, la crea.
        """
        if cls._unica_instancia is None:
            cls._unica_instancia = cls.__new__(cls)
        return cls._unica_instancia

    def __new__(cls, *args, **kwargs):
        if cls._unica_instancia is None:
            cls._unica_instancia = super(Oeste, cls).__new__(cls, *args, **kwargs)
        return cls._unica_instancia

    def caminar(self, un_bicho):
        posicion = un_bicho.get_posicion()
        if posicion and hasattr(posicion, "forma"):
            elemento = posicion.forma.obtener_elemento_or(self)
            if elemento:
                elemento.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Oeste del contenedor.
        """
        return un_contenedor.oeste

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Oeste del contenedor.
        """
        en_un_contenedor.oeste = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Oeste.
        """
        if hasattr(un_contenedor, "forma"):
            elemento = un_contenedor.forma.get_oeste()
            if elemento:
                elemento.recorrer(un_bloque)
