from .Orientacion import Orientacion

class Suroeste(Orientacion):
    """
    Clase que representa la orientación Suroeste.
    """

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Suroeste.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.suroeste:
            posicion.suroeste.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Suroeste del contenedor.
        """
        return un_contenedor.suroeste

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Suroeste del contenedor.
        """
        en_un_contenedor.suroeste = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Suroeste.
        """
        if un_contenedor.suroeste:
            un_contenedor.suroeste.recorrer(un_bloque)
