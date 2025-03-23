from .Ente import Ente

class Personaje(Ente):
    """
    Representa al usuario en el juego.
    """

    def __init__(self):
        super().__init__()
        self.nombre = ""

    # Ataques
    def atacar(self):
        """El personaje ataca buscando un bicho en el juego."""
        if self.juego:
            self.juego.buscar_bicho()

    # Muerte
    def he_muerto(self):
        """Acción a realizar cuando el personaje muere."""
        if self.juego:
            self.juego.muere_personaje()

    # Movimiento
    def ir_al_este(self):
        """Mueve al personaje al este."""
        if self.posicion:
            self.posicion.ir_al_este(self)

    def ir_al_norte(self):
        """Mueve al personaje al norte."""
        if self.posicion:
            self.posicion.ir_al_norte(self)

    def ir_al_oeste(self):
        """Mueve al personaje al oeste."""
        if self.posicion:
            self.posicion.ir_al_oeste(self)

    def ir_al_sur(self):
        """Mueve al personaje al sur."""
        if self.posicion:
            self.posicion.ir_al_sur(self)

    # Acceso
    def get_nombre(self):
        """Devuelve el nombre del personaje."""
        return self.nombre

    def set_nombre(self, nombre):
        """Establece el nombre del personaje."""
        self.nombre = nombre

    # Impresión
    def __str__(self):
        """Devuelve una representación en texto del personaje."""
        return f"Personaje: {self.nombre}"
