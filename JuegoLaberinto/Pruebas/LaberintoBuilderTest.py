import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
from JuegoLaberinto.Elementos.Builder.Director import Director

class LaberintoBuilderTest(unittest.TestCase):
    """
    Clase de pruebas para el Laberinto Builder.
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

    # Métodos de comprobación
    def comprobar_armario(self, num, un_cont):
        """
        Comprueba que un contenedor tiene un armario.
        """
        arm = next((each for each in un_cont.hijos if each.es_armario()), None)
        self.assertIsNotNone(arm)
        self.assertTrue(arm.es_armario())
        return arm

    def comprobar_bomba_en(self, un_contenedor):
        """
        Comprueba que un contenedor tiene una bomba.
        """
        bomba = next((each for each in un_contenedor.hijos if each.es_bomba()), None)
        self.assertIsNotNone(bomba)
        self.assertTrue(bomba.es_bomba())

    def comprobar_habitacion(self, num):
        """
        Comprueba que existe una habitación con el número dado.
        """
        hab = self.juego.obtener_habitacion(num)
        self.assertEqual(hab.num, num)
        return hab

    def comprobar_laberinto_recursivo(self, un_dic, padre):
        """
        Comprueba recursivamente los elementos del laberinto.
        """
        nada = True
        con = None

        if un_dic.get('tipo') == 'habitacion':
            nada = False
            con = self.comprobar_habitacion(un_dic.get('num'))
        elif un_dic.get('tipo') == 'armario':
            nada = False
            con = self.comprobar_armario(un_dic.get('num'), padre)
        elif un_dic.get('tipo') == 'bomba':
            nada = False
            self.comprobar_bomba_en(padre)
        elif un_dic.get('tipo') == 'tunel':
            nada = False
            self.comprobar_tunel_en(padre)

        lista = un_dic.get('hijos', None)
        if lista:
            for each in lista:
                self.comprobar_laberinto_recursivo(each, con)

        if nada:
            self.fail("Elemento no reconocido en el laberinto.")

    def comprobar_puerta_de(self, un_num, orientacion, otro_num, otra_orientacion):
        """
        Comprueba que existe una puerta entre dos habitaciones con las orientaciones dadas.
        """
        una_hab = self.juego.obtener_habitacion(un_num)
        otra_hab = self.juego.obtener_habitacion(otro_num)

        self.assertEqual(una_hab.num, un_num)
        self.assertEqual(otra_hab.num, otro_num)

        or1 = getattr(self.director.builder, f'fabricar_{orientacion.lower()}')()
        or2 = getattr(self.director.builder, f'fabricar_{otra_orientacion.lower()}')()

        pt1 = una_hab.obtener_elemento_or(or1)
        pt2 = otra_hab.obtener_elemento_or(or2)
        
        self.assertTrue(pt1.es_puerta())
        self.assertTrue(pt2.es_puerta())
        self.assertEqual(pt1, pt2)
        self.assertFalse(pt1.esta_abierta())

    def comprobar_tunel_en(self, un_contenedor):
        """
        Comprueba que un contenedor tiene un túnel.
        """
        tunel = next((each for each in un_contenedor.hijos if each.es_tunel()), None)
        self.assertIsNotNone(tunel)
        self.assertTrue(tunel.es_tunel())

    def test_iniciales(self):
        """
        Prueba iniciales del juego y laberinto.
        """
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)

    def test_laberinto(self):
        """
        Prueba el laberinto recursivamente.
        """
        for each in self.dict.get('laberinto', []):
            self.comprobar_laberinto_recursivo(each, 'root')

        for cada in self.dict.get('puertas', []):
            self.comprobar_puerta_de(cada[0], cada[1], cada[2], cada[3])

    def test_personaje(self):
        """
        Prueba que el personaje se encuentra en la habitación inicial.
        """
        self.assertIsNotNone(self.juego.person)
        hab = self.juego.obtener_habitacion(1)
        self.assertEqual(self.juego.person.posicion, hab)

    def test_bicho(self):
        """
        Prueba que un bicho está en la habitación inicial con las vidas correctas.
        """
        bicho = self.juego.bichos[0]
        self.assertIsNotNone(bicho)
        hab = self.juego.obtener_habitacion(1)
        self.assertEqual(bicho.posicion, hab)
        self.assertEqual(bicho.vidas, 5)

    def test_bicho_ataca(self):
        """
        Prueba que un bicho puede atacar al personaje.
        """
        hab1 = self.juego.obtener_habitacion(1)
        bicho = self.juego.bichos[0]
        person = self.juego.person

        self.assertIsNotNone(bicho)
        self.assertIsNotNone(person)

        hab1.entrar(bicho)
        hab1.entrar(person)
        bicho.atacar()

        self.assertEqual(person.vidas, 0)

    def test_personaje_ataca(self):
        """
        Prueba que el personaje puede atacar a un bicho.
        """
        hab1 = self.juego.obtener_habitacion(1)
        bicho = self.juego.bichos[0]
        person = self.juego.person

        self.assertIsNotNone(bicho)
        self.assertIsNotNone(person)

        hab1.entrar(bicho)
        hab1.entrar(person)
        person.atacar()

        self.assertEqual(bicho.vidas, 4)

if __name__ == '__main__':
    unittest.main()
