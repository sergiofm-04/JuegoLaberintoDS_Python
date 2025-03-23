from .Modo import Modo
import time

class Agresivo(Modo):
    """
    Agresivo: es un bicho que se mueve rápido y tiene más poder.
    """

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
