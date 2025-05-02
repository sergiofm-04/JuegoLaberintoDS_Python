from .Orientacion import Orientacion

class Noroeste(Orientacion):
    """
    Clase que representa la orientación Noroeste.
    """

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Noroeste.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.noroeste:
            posicion.noroeste.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Noroeste del contenedor.
        """
        return un_contenedor.noroeste

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Noroeste del contenedor.
        """
        en_un_contenedor.noroeste = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Noroeste.
        """
        if un_contenedor.noroeste:
            un_contenedor.noroeste.recorrer(un_bloque)
