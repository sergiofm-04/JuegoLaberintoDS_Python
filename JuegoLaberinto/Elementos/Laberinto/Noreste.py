from .Orientacion import Orientacion

class Noreste(Orientacion):
    """
    Clase que representa la orientación Noreste.
    """

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Noreste.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.noreste:
            posicion.noreste.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Noreste del contenedor.
        """
        return un_contenedor.noreste

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Noreste del contenedor.
        """
        en_un_contenedor.noreste = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Noreste.
        """
        if un_contenedor.noreste:
            un_contenedor.noreste.recorrer(un_bloque)
