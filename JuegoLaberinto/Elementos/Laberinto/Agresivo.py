from .Modo import Modo
import time

class Agresivo(Modo):
    """
    Agresivo: es un bicho que se mueve rápido y tiene más poder.
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

    def es_agresivo(self):
        """
        Indica que este modo es agresivo.
        """
        return True

    def __str__(self):
        """
        Devuelve una representación en texto del modo agresivo.
        """
        return "Agresivo"
