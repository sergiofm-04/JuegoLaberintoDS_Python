from .Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False
    
    def entrar(self):
        if self.activa:
            print("Te has chocado con una bomba")
        else:
            self.get_em().entrar()

    def set_activa(self, activa):
        self.activa = activa

    def get_activa(self):
        return self.activa
