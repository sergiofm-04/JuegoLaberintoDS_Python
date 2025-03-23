from .Modo import Modo
import time

class Perezoso(Modo):
    """
    Perezoso: es un bicho lento y con poco poder.
    """

    def dormir(self, un_bicho):
        """
        El bicho agresivo duerme por un segundo antes de actuar.
        """
        print(f"{un_bicho} duerme")
        time.sleep(3)

    def es_perezoso(self):
        """
        Indica que este modo es agresivo.
        """
        return True

    def __str__(self):
        """
        Devuelve una representación en texto del modo agresivo.
        """
        return "Perezoso"
