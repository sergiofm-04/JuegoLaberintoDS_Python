from .Muerto import Muerto
from .Vivo import Vivo

class Ente:
    """
    Interfaz común de los entes del juego.
    """

    def __init__(self):
        """
        Inicializa un ente con valores predeterminados.
        """
        self.poder = 1
        self.posicion = None
        self.vidas = 5
        self.juego = None
        self.estado_ente = Vivo()  # Estado inicial

    # Métodos de ataques
    def atacar(self):
        """
        Realiza un ataque según el estado actual del ente.
        """
        self.estado_ente.atacar(self)

    def es_atacado_por(self, alguien):
        """
        Define la acción de ser atacado por otro ente.
        """
        print(f"{self} es atacado por {alguien}")
        self.vidas -= alguien.get_poder()
        print(f"Vidas restantes: {self.vidas}")

        if self.vidas <= 0:
            self.he_muerto()

    def puede_atacar(self):
        """
        Método abstracto para verificar si el ente puede atacar.
        """
        raise NotImplementedError("Subclasses should implement this!")

    # Métodos de consulta
    def esta_vivo(self):
        """
        Verifica si el ente está vivo.
        """
        return self.vidas > 0

    # Métodos de acceso
    def get_estado_ente(self):
        """
        Devuelve el estado actual del ente.
        """
        return self.estado_ente

    def set_estado_ente(self, estado):
        """
        Establece el estado del ente.
        """
        self.estado_ente = estado

    def get_juego(self):
        """
        Devuelve el juego asociado al ente.
        """
        return self.juego

    def set_juego(self, un_juego):
        """
        Establece el juego asociado al ente.
        """
        self.juego = un_juego

    def get_poder(self):
        """
        Devuelve el poder del ente.
        """
        return self.poder

    def set_poder(self, un_poder):
        """
        Establece el poder del ente.
        """
        self.poder = un_poder

    def get_posicion(self):
        """
        Devuelve la posición actual del ente.
        """
        return self.posicion

    def set_posicion(self, una_posicion):
        """
        Establece la posición del ente.
        """
        self.posicion = una_posicion

    def get_vidas(self):
        """
        Devuelve las vidas restantes del ente.
        """
        return self.vidas

    def set_vidas(self, unas_vidas):
        """
        Establece las vidas del ente.
        """
        self.vidas = unas_vidas

    # Métodos de estado
    def he_muerto(self):
        """
        Define la acción de morir.
        """
        self.estado_ente = Muerto()
        self.avisar()

    def avisar(self):
        """
        Método abstracto para notificar la muerte del ente.
        """
        raise NotImplementedError("Subclasses should implement this!")

    # Métodos relacionados con túneles
    def buscar_tunel(self):
        """
        Acción predeterminada para buscar un túnel.
        """
        pass

    def crear_nuevo_laberinto(self, un_tunel):
        """
        Acción predeterminada para crear un nuevo laberinto.
        """
        pass

    def juego_clona_laberinto(self):
        """
        Clona el laberinto del juego asociado.
        """
        return self.juego.clonar_laberinto()
