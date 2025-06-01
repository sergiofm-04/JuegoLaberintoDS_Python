import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
from JuegoLaberinto.Elementos.Builder.Director import Director

from JuegoLaberinto.Elementos.Laberinto.EspadaAltair import EspadaAltair
from JuegoLaberinto.Elementos.Laberinto.Hashashin import Hashashin
from JuegoLaberinto.Elementos.Laberinto.Daga import Daga
from JuegoLaberinto.Elementos.Laberinto.Katana import Katana
from JuegoLaberinto.Elementos.Laberinto.Vara import Vara
from JuegoLaberinto.Elementos.Laberinto.FlechaYaka import FlechaYaka

class ModificacionesTest(unittest.TestCase):
    """
    Clase de pruebas para las modificaciones efectuadas.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        super().setUp()
        self.director = Director()
        ruta = "C:\\Users\\sergi\\Desktop\\Proyectos DS\\Laberintos\\"
        self.director.procesar(ruta + "lab2Hab.json")
        self.dict = self.director.dict
        self.juego = self.director.obtener_juego()
        self.juego.agregar_personaje('CR7')

    # Métodos get y set para `juego`
    def get_juego(self):
        """
        Devuelve el juego utilizado en las pruebas.
        """
        return self.juego

    def set_juego(self, juego):
        """
        Establece el juego utilizado en las pruebas.
        """
        self.juego = juego

    # Métodos get y set para `director`
    def get_director(self):
        """
        Devuelve el director utilizado en las pruebas.
        """
        return self.director

    def set_director(self, director):
        """
        Establece el director utilizado en las pruebas.
        """
        self.director = director

    # Métodos get y set para `dict`
    def get_dict(self):
        """
        Devuelve el diccionario utilizado en las pruebas.
        """
        return self.dict

    def set_dict(self, dict_obj):
        """
        Establece el diccionario utilizado en las pruebas.
        """
        self.dict = dict_obj

    def test_espada(self):
        """
        Prueba para verificar la espada en el juego.
        """
        self.juego.person.recoger_arma(EspadaAltair())
        self.assertIsNotNone(self.juego.person.arma_eq)
        self.assertIsInstance(self.juego.person.arma_eq, EspadaAltair)
        # El poder debe ser el base + el de la espada
        self.assertEqual(self.juego.person.poder, 3 + self.juego.person.arma_eq.poder_extra)

        bicho1 = self.juego.bichos[0]
        vidas_antes = bicho1.vidas
        self.juego.person.atacar()
        self.assertEqual(bicho1.vidas, vidas_antes - self.juego.person.poder)
    
    def test_modo_hashashin(self):
        """
        Prueba para verificar el modo Hashashin en el juego.
        """
        self.juego.person.recoger_arma(EspadaAltair())

        bicho1 = self.juego.bichos[0]
        self.juego.person.atacar()

        self.assertIsInstance(bicho1.modo, Hashashin)
    
    def test_daga(self):
        """
        Prueba para verificar la daga en el juego.
        """
        self.juego.person.recoger_arma(Daga())
        self.assertIsNotNone(self.juego.person.arma_eq)
        self.assertIsInstance(self.juego.person.arma_eq, Daga)
        self.assertEqual(self.juego.person.poder, 3 + self.juego.person.arma_eq.poder_extra)

        bicho1 = self.juego.bichos[0]
        vidas_antes = bicho1.vidas
        self.juego.person.atacar()
        self.assertEqual(bicho1.vidas, vidas_antes - self.juego.person.poder)
    
    def test_katana(self):
        """
        Prueba para verificar la katana en el juego.
        """
        self.juego.person.recoger_arma(Katana())
        self.assertIsNotNone(self.juego.person.arma_eq)
        self.assertIsInstance(self.juego.person.arma_eq, Katana)
        self.assertEqual(self.juego.person.poder, 3 + self.juego.person.arma_eq.poder_extra)

        bicho1 = self.juego.bichos[0]
        vidas_antes = bicho1.vidas
        self.juego.person.atacar()
        self.assertEqual(bicho1.vidas, vidas_antes - self.juego.person.poder)
    
    def test_vara(self):
        """
        Prueba para verificar la vara en el juego.
        """
        self.juego.person.recoger_arma(Vara())
        self.assertIsNotNone(self.juego.person.arma_eq)
        self.assertIsInstance(self.juego.person.arma_eq, Vara)
        self.assertEqual(self.juego.person.poder, 3 + self.juego.person.arma_eq.poder_extra)

        bicho1 = self.juego.bichos[0]
        vidas_antes = bicho1.vidas
        self.juego.person.atacar()
        self.assertEqual(bicho1.vidas, vidas_antes - self.juego.person.poder)

    def test_flecha_yaka(self):
        """
        Prueba para verificar el funcionamiento de la Flecha Yaka en el juego.
        - Si las puertas están cerradas, no ataca.
        - Si las puertas están abiertas, ataca a todos los bichos vivos.

        En este test además se verifica internamente el funcionamiento del visitor implementado.
        """
        # Equipa la flecha al personaje
        self.juego.person.recoger_arma(FlechaYaka())
        bichos = self.juego.bichos
        # Guarda las vidas iniciales
        vidas_iniciales = [bicho.vidas for bicho in bichos]

        # 1. Puertas cerradas: no debe atacar
        self.juego.cerrar_puertas()
        self.juego.person.atacar()
        # Las vidas deben permanecer igual
        for bicho, vida in zip(bichos, vidas_iniciales):
            self.assertEqual(bicho.vidas, vida, "La flecha no debe atacar con puertas cerradas")

        # 2. Puertas abiertas: debe atacar a todos los bichos vivos
        self.juego.abrir_puertas()
        self.juego.person.atacar()
        # Todos los bichos vivos deben haber recibido daño (poder del personaje + poder de la flecha)
        poder_ataque = self.juego.person.poder
        for bicho, vida in zip(bichos, vidas_iniciales):
            if bicho.esta_vivo():
                self.assertEqual(bicho.vidas, vida - poder_ataque, "La flecha debe atacar a todos los bichos vivos")

    def test_cofre(self):
        """
        Prueba para verificar que el cofre entrega un arma al personaje al entrar en la segunda habitación.

        En este test se verifica también de manera implícita el funcionamiento del comando implementado.
        """
        self.juego.abrir_puertas()
        personaje = self.juego.person
        # El personaje se mueve al sur (a la segunda habitación, que contiene el cofre)
        personaje.ir_al_sur()
        # El personaje debe tener un arma equipada tras abrir el cofre
        self.assertIsNotNone(personaje.arma_eq, "El personaje no recogió ningún arma del cofre.")

if __name__ == '__main__':
    unittest.main()
