from ..Laberinto.Juego import Juego
from ..Laberinto.Laberinto import Laberinto
from ..Laberinto.Habitacion import Habitacion
from ..Laberinto.Armario import Armario
from ..Laberinto.Bicho import Bicho
from ..Laberinto.Agresivo import Agresivo
from ..Laberinto.Perezoso import Perezoso
from ..Laberinto.Bomba import Bomba
from ..Laberinto.Norte import Norte
from ..Laberinto.Sur import Sur
from ..Laberinto.Este import Este
from ..Laberinto.Oeste import Oeste
from ..Laberinto.Pared import Pared
from ..Laberinto.Puerta import Puerta
from ..Laberinto.Tunel import Tunel
from ..Laberinto.Cuadrado import Cuadrado

class LaberintoBuilder:
    """
    LaberintoBuilder construye un tipo de laberinto por encargo del Director.
    """

    def __init__(self):
        self.juego = None
        self.laberinto = None

    # Métodos de fabricación
    def fabricar_armario(self, un_num, un_contenedor):
        arm = Armario()
        arm.num = un_num
        arm.forma = self.fabricar_forma()
        for orientacion in arm.obtener_orientaciones():
            arm.poner_en_or(orientacion, self.fabricar_pared())
        un_contenedor.agregar_hijo(arm)
        return arm

    def fabricar_bicho_agresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        return bicho

    def fabricar_bicho_agresivo_en_habitacion(self, una_hab):
        bicho = self.fabricar_bicho_agresivo()
        bicho.posicion = una_hab
        return bicho

    def fabricar_bicho_modo(self, str_modo, posicion):
        hab = self.laberinto.obtener_habitacion(posicion)
        bicho = getattr(self, f"fabricar_bicho_{str_modo.lower()}")()
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)

    def fabricar_bicho_perezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 1
        bicho.poder = 1
        return bicho

    def fabricar_bicho_perezoso_en_habitacion(self, una_hab):
        bicho = self.fabricar_bicho_perezoso()
        bicho.posicion = una_hab
        return bicho

    def fabricar_bomba_en(self, un_contenedor):
        bmb = Bomba()
        un_contenedor.agregar_hijo(bmb)

    def fabricar_este(self):
        return Este.default()

    def fabricar_forma(self):
        forma = Cuadrado()
        forma.agregar_orientacion(self.fabricar_norte())
        forma.agregar_orientacion(self.fabricar_sur())
        forma.agregar_orientacion(self.fabricar_este())
        forma.agregar_orientacion(self.fabricar_oeste())
        return forma

    def fabricar_habitacion(self, un_num):
        hab = Habitacion()
        hab.num = un_num
        hab.forma = self.fabricar_forma()
        for orientacion in hab.obtener_orientaciones():
            hab.poner_en_or(orientacion, self.fabricar_pared())
        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricar_juego(self):
        self.juego = Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = self.juego.clonar_laberinto()

    def fabricar_laberinto(self):
        self.laberinto = Laberinto()

    def fabricar_norte(self):
        return Norte.default()

    def fabricar_oeste(self):
        return Oeste.default()

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta_l1(self, num1, str_or1, num2, str_or2):
        hab1 = self.laberinto.obtener_habitacion(num1)
        hab2 = self.laberinto.obtener_habitacion(num2)
        obj_or1 = getattr(self, f"fabricar_{str_or1.lower()}")()
        obj_or2 = getattr(self, f"fabricar_{str_or2.lower()}")()
        pt = Puerta()
        pt.lado1 = hab1
        pt.lado2 = hab2
        hab1.poner_en_or(obj_or1, pt)
        hab2.poner_en_or(obj_or2, pt)

    def fabricar_sur(self):
        return Sur.default()

    def fabricar_tunel_en(self, un_contenedor):
        tunel = Tunel()
        un_contenedor.agregar_hijo(tunel)

    # Métodos de acceso
    def get_juego(self):
        return self.juego

    def set_juego(self, juego):
        self.juego = juego

    def get_laberinto(self):
        return self.laberinto

    def set_laberinto(self, laberinto):
        self.laberinto = laberinto

    def obtener_juego(self):
        return self.juego
