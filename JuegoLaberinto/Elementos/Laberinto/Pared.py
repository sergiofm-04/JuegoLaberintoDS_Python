from .ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    """
    Clase que representa una pared en el laberinto.
    """

    def entrar(self, alguien):
        """
        Define la acción de entrar en una pared.
        """
        print(f"{alguien} ha chocado con una pared.")

    def es_pared(self):
        """
        Indica que este objeto es una pared.
        """
        return True

    def __str__(self):
        """
        Devuelve una representación en texto de la pared.
        """
        return "Pared"
