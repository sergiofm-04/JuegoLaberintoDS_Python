from .Hoja import Hoja

class Tunel(Hoja):
    """
    Tunel es un Proxy virtual. Cuando el personaje entre en el túnel, se creará un nuevo laberinto.
    """

    def __init__(self):
        super().__init__()
        self.laberinto = None

    # Visitor
    def aceptar(self, un_visitor):
        """
        Permite que un visitante interactúe con el túnel.
        """
        un_visitor.visitar_tunel(self)

    # Caminar
    def crear_nuevo_laberinto(self, alguien):
        """
        Crea un nuevo laberinto cuando alguien entra en el túnel.
        """
        print(f"{alguien} crea un nuevo laberinto.")
        self.laberinto = alguien.juego_clona_laberinto()  # Prototipo o deep copy

    def entrar(self, alguien):
        """
        Define la acción de entrar en el túnel.
        Si no hay un laberinto, se crea uno nuevo.
        """
        if self.laberinto is None:
            self.crear_nuevo_laberinto(alguien)
        else:
            print(f"{alguien} entra en un nuevo laberinto.")
            self.laberinto.entrar(alguien)

    # Consulta
    def es_tunel(self):
        """
        Indica que este objeto es un túnel.
        """
        return True

    # Acceso
    def get_laberinto(self):
        """
        Devuelve el laberinto asociado al túnel.
        """
        return self.laberinto

    def set_laberinto(self, laberinto):
        """
        Establece el laberinto asociado al túnel.
        """
        self.laberinto = laberinto
