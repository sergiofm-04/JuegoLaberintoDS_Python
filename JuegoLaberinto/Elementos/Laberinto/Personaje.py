from .Ente import Ente

class Personaje(Ente):
    """
    Representa al usuario en el juego.
    """

    def __init__(self):
        super().__init__()
        self.nombre = ""

    # Aviso
    def avisar(self):
        """
        Notifica al juego que el personaje ha muerto.
        """
        if self.juego:
            self.juego.muere_personaje()

    # Movimiento
    def crear_nuevo_laberinto(self, un_tunel):
        """
        Crea un nuevo laberinto a través de un túnel.
        """
        un_tunel.crear_nuevo_laberinto(self)

    def ir_al_este(self):
        """
        Mueve al personaje al este.
        """
        if self.posicion:
            self.posicion.ir_al_este(self)

    def ir_al_norte(self):
        """
        Mueve al personaje al norte.
        """
        if self.posicion:
            self.posicion.ir_al_norte(self)

    def ir_al_oeste(self):
        """
        Mueve al personaje al oeste.
        """
        if self.posicion:
            self.posicion.ir_al_oeste(self)

    def ir_al_sur(self):
        """
        Mueve al personaje al sur.
        """
        if self.posicion:
            self.posicion.ir_al_sur(self)

    # Acceso
    def get_nombre(self):
        """
        Devuelve el nombre del personaje.
        """
        return self.nombre

    def set_nombre(self, nombre):
        """
        Establece el nombre del personaje.
        """
        self.nombre = nombre

    def obtener_comandos(self):
        """
        Obtiene la lista de comandos disponibles en la posición actual.
        """
        lista = []
        if self.posicion:
            self.posicion.recorrer(lambda each: lista.extend(each.obtener_comandos()))
        return lista

    # Ataques
    def puede_atacar(self):
        """
        Permite que el personaje ataque buscando un bicho en el juego.
        """
        if self.juego:
            self.juego.buscar_bicho()

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto del personaje.
        """
        return f"Player-{self.nombre}"
