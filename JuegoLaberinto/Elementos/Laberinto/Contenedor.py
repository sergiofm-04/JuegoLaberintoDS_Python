from .ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []
        self.orientaciones = []

    def agregar_hijo(self, un_em):
        un_em.set_padre(self)
        self.hijos.append(un_em)

    def eliminar_hijo(self, un_em):
        try:
            self.hijos.remove(un_em)
        except ValueError:
            print("No existe ese objeto")

    def get_hijos(self):
        return self.hijos

    def set_hijos(self, valor):
        self.hijos = valor

    def agregar_orientacion(self, una_or):
        self.orientaciones.append(una_or)

    def obtener_elemento_or(self, una_or):
        return una_or.obtener_elemento_or_en(self)

    def get_orientaciones(self):
        return self.orientaciones

    def set_orientaciones(self, valor):
        self.orientaciones = valor

    def poner_en_or(self, una_or, un_em):
        una_or.poner_elemento(un_em, self)

    def entrar(self):
        return super().entrar()
    
    def entrar_alguien(self, alguien):
        return super().entrar_alguien(alguien)
