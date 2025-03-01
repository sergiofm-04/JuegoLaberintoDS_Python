import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
from JuegoLaberinto.Elementos.Laberinto.Juego import Juego
from JuegoLaberinto.Elementos.FactoryMethod.Creator import Creator

class PruebasLaberinto(unittest.TestCase):
    def get_fm(self):
        return self.fm
    
    def set_fm(self, fm):
        self.fm = fm
    
    def get_juego(self):
        return self.juego
    
    def set_juego(self, juego):
        self.juego = juego

    def setUp(self):
        """Configuración inicial para las pruebas."""
        super().setUp()
        self.juego = Juego()
        self.fm = Creator()
        self.juego.crear_laberinto_2_habitaciones_fm(self.fm)

    def test_iniciales(self):
        """Prueba iniciales del juego y laberinto."""
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        num_hab = len(self.juego.laberinto.hijos)
        self.assertEqual(num_hab, 2)

    def test_habitaciones(self):
        """Prueba las habitaciones del laberinto."""
        norte = self.fm.fabricar_norte()
        sur = self.fm.fabricar_sur()
        este = self.fm.fabricar_este()
        oeste = self.fm.fabricar_oeste()
        hab1 = self.juego.obtener_habitacion(1)
        hab2 = self.juego.obtener_habitacion(2)

        self.assertTrue(hab1.es_habitacion())
        self.assertTrue(hab2.es_habitacion())

        self.assertTrue(hab1.norte.es_pared())

        self.assertTrue(hab1.obtener_elemento_or(sur).es_puerta())
        self.assertTrue(hab1.obtener_elemento_or(este).es_pared())

        self.assertTrue(hab2.obtener_elemento_or(norte).es_puerta())
        self.assertTrue(hab2.obtener_elemento_or(oeste).es_pared())

        pt12 = hab1.sur
        self.assertTrue(pt12.es_puerta())
        self.assertTrue(hab2.norte.es_puerta())
        self.assertFalse(pt12.abierta)

if __name__ == '__main__':
    unittest.main()
