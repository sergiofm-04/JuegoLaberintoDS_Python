from .Contenedor import Contenedor

class Laberinto(Contenedor):
    def agregar_habitacion(self, una_habitacion):
        self.hijos.append(una_habitacion)

    def eliminar_habitacion(self, una_habitacion):
        try:
            self.hijos.remove(una_habitacion)
        except ValueError:
            print("No existe ese objeto habitacion")

    def entrar(self):
        pass
        # "qué significa entrar en el laberinto?? entrar en la habitación 1"

    def obtener_habitacion(self, un_num):
        for each in self.hijos:
            if each.get_num() == un_num:
                return each
        return None
