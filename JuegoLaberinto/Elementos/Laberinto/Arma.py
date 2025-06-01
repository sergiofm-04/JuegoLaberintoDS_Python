from .Decorator import Decorator

class Arma(Decorator):
    def __init__(self, nombre, poder_extra):
        """
        Inicializa un arma con un nombre, poder adicional y un efecto opcional.
        """
        self.nombre = nombre
        self.poder_extra = poder_extra
        self.recogida = False
    
    def entrar(self, alguien):
        """
        Define la acción de entrar en un arma.
        """
        alguien.recoger_arma(self)

    def __str__(self):
        return f"Arma {self.nombre} (+{self.poder_extra} poder)"

    def aceptar(self, un_visitor):
        if hasattr(un_visitor, "visitar_tunel"):
            un_visitor.visitar_tunel(self)
        else:
            None

    def es_arma(self):
        """
        Indica que este objeto es un arma.
        """
        return True
