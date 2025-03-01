from .Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self):
        super().__init__()
        self.num = None
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self):
        print("Estás en la habitación")

    def es_habitacion(self):
        return True

    def get_num(self):
        return self.num

    def set_num(self, valor):
        self.num = valor

    def get_norte(self):
        return self.norte

    def set_norte(self, valor):
        self.norte = valor

    def get_sur(self):
        return self.sur

    def set_sur(self, valor):
        self.sur = valor

    def get_este(self):
        return self.este

    def set_este(self, valor):
        self.este = valor

    def get_oeste(self):
        return self.oeste

    def set_oeste(self, valor):
        self.oeste = valor
