from .Orientacion import Orientacion

class Sureste(Orientacion):
    """
    Clase que representa la orientación Sureste.
    """

    def caminar(self, un_bicho):
        """
        Define cómo un bicho camina hacia el Sureste.
        """
        posicion = un_bicho.get_posicion()
        if posicion and posicion.sureste:
            posicion.sureste.entrar(un_bicho)

    def obtener_elemento_or_en(self, un_contenedor):
        """
        Obtiene el elemento en la orientación Sureste del contenedor.
        """
        return un_contenedor.sureste

    def poner_elemento(self, un_em, en_un_contenedor):
        """
        Coloca un elemento en la orientación Sureste del contenedor.
        """
        en_un_contenedor.sureste = un_em

    def recorrer(self, un_bloque, un_contenedor):
        """
        Aplica un bloque de código (función) al elemento en la orientación Sureste.
        """
        if un_contenedor.sureste:
            un_contenedor.sureste.recorrer(un_bloque)
