from .Habitacion import Habitacion
from .Pared import Pared
from .Puerta import Puerta
from .Laberinto import Laberinto

class Juego:
    """
    Clase principal del juego del laberinto.
    """

    def __init__(self):
        self.laberinto = None
        self.bichos = []

    def agregar_bicho(self, un_bicho):
        """
        Agrega un bicho al juego.
        """
        self.bichos.append(un_bicho)

    def eliminar_bicho(self, un_bicho):
        """
        Elimina un bicho si existe en la colección.
        """
        if un_bicho in self.bichos:
            self.bichos.remove(un_bicho)
        else:
            print("No existe ese bicho")

    def crear_laberinto_2_habitaciones(self):
        """
        Crea un laberinto con dos habitaciones conectadas por una puerta.
        """
        hab1 = Habitacion(1)
        hab1.set_este(Pared())
        hab1.set_oeste(Pared())
        hab1.set_norte(Pared())

        hab2 = Habitacion(2)
        hab2.set_sur(Pared())
        hab2.set_este(Pared())
        hab2.set_oeste(Pared())

        puerta = Puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        self.laberinto = Laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        return self.laberinto

    def crear_laberinto_2_habitaciones_fm(self, un_fm):
        """
        Crea un laberinto con dos habitaciones usando una fábrica de laberintos.
        """
        hab1 = un_fm.fabricar_habitacion(1)
        hab2 = un_fm.fabricar_habitacion(2)
        puerta = un_fm.fabricar_puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.poner_en_or(un_fm.fabricar_sur(), puerta)
        hab2.poner_en_or(un_fm.fabricar_norte(), puerta)

        self.laberinto = un_fm.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        return self.laberinto
    
    def crear_laberinto_2_habitaciones_fmd(self, unFM):
        """Crea un laberinto con dos habitaciones usando una fábrica (Creator)."""
        hab1 = unFM.fabricar_habitacion(1)
        hab2 = unFM.fabricar_habitacion(2)

        bomba1 = unFM.fabricar_bomba()
        bomba1.em(unFM.fabricar_pared())
        hab1.set_este(bomba1)

        bomba2 = unFM.fabricar_bomba()
        bomba2.em(unFM.fabricar_pared())
        hab2.set_este(bomba2)

        puerta = unFM.fabricar_puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        self.laberinto = unFM.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)

        return self.laberinto

    def crear_laberinto_4h4b_fmd(self, unFM):
        """Crea un laberinto con cuatro habitaciones y cuatro bichos usando una fábrica (Creator)."""
        norte = unFM.fabricar_norte()
        sur = unFM.fabricar_sur()
        este = unFM.fabricar_este()
        oeste = unFM.fabricar_oeste()

        hab1 = unFM.fabricar_habitacion(1)
        hab2 = unFM.fabricar_habitacion(2)
        hab3 = unFM.fabricar_habitacion(3)
        hab4 = unFM.fabricar_habitacion(4)

        puerta1 = unFM.fabricar_puerta()
        puerta2 = unFM.fabricar_puerta()
        puerta3 = unFM.fabricar_puerta()
        puerta4 = unFM.fabricar_puerta()

        puerta1.set_lado1(hab1)
        puerta1.set_lado2(hab2)
        puerta2.set_lado1(hab1)
        puerta2.set_lado2(hab3)
        puerta3.set_lado1(hab2)
        puerta3.set_lado2(hab4)
        puerta4.set_lado1(hab3)
        puerta4.set_lado2(hab4)

        hab1.poner_en_or(sur, puerta1)
        hab2.poner_en_or(norte, puerta1)
        hab1.poner_en_or(este, puerta2)
        hab3.poner_en_or(oeste, puerta2)
        hab2.poner_en_or(este, puerta3)
        hab4.poner_en_or(oeste, puerta3)
        hab3.poner_en_or(sur, puerta4)
        hab4.poner_en_or(norte, puerta4)

        bicho1 = unFM.fabricar_bicho_agresivo()
        bicho2 = unFM.fabricar_bicho_agresivo()
        bicho3 = unFM.fabricar_bicho_perezoso()
        bicho4 = unFM.fabricar_bicho_perezoso()

        self.laberinto = unFM.fabricar_laberinto()
        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        self.laberinto.agregar_habitacion(hab3)
        self.laberinto.agregar_habitacion(hab4)

        self.agregar_bicho(bicho1)
        self.agregar_bicho(bicho2)
        self.agregar_bicho(bicho3)
        self.agregar_bicho(bicho4)

        bicho1.set_posicion(hab1)
        bicho2.set_posicion(hab3)
        bicho3.set_posicion(hab2)
        bicho4.set_posicion(hab4)

        return self.laberinto

    def get_laberinto(self):
        return self.laberinto

    def set_laberinto(self, laberinto):
        self.laberinto = laberinto

    def obtener_habitacion(self, num):
        if self.laberinto:
            return self.laberinto.obtener_habitacion(num)
        return None

    def get_bichos(self):
        return self.bichos

    def set_bichos(self, bichos):
        self.bichos = bichos
