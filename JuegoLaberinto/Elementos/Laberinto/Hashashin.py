from .Modo import Modo
import time

class Hashashin(Modo):
    """
    Hashashin: es un bicho agresivo hacia otros bichos en lugar de hacia el personaje.
    """

    def buscar_tunel_bicho(self, un_bicho):
        """
        Busca un túnel en la posición actual del bicho y entra en él si lo encuentra.
        """
        un_cont = un_bicho.get_posicion()
        tunel = next(
            (each for each in un_cont.get_hijos() if each.es_tunel()),
            None
        )
        if tunel:
            tunel.entrar(un_bicho)

    def dormir(self, un_bicho):
        """
        El bicho agresivo duerme por un segundo antes de actuar.
        """
        print(f"{un_bicho} duerme")
        time.sleep(1)

    def es_hashashin(self):
        return True
    
    def __str__(self):
        """
        Devuelve una representación en texto del modo agresivo.
        """
        return "Hashashin"
