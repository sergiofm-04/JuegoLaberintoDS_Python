from .Ente import Ente

class Personaje(Ente):
    """
    Representa al usuario en el juego.
    """

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.llaves = []
        self.arma_eq = None
        self.poder = 3
        self.vidas = 300

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
    
    def get_arma(self):
        """
        Devuelve el arma equipada del personaje.
        """
        return self.arma_eq
    
    def set_arma(self, arma):
        """
        Establece el arma equipada del personaje.
        """
        self.arma_eq = arma

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
            self.juego.buscar_bicho(self)

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto del personaje.
        """
        return f"Player-{self.nombre}"

    def recoger_arma(self, arma):
        """
        Añade un arma al inventario del personaje y aumenta su poder.
        """
        if self.arma_eq:
            print(f"{self.nombre} ya tiene un arma equipada: {self.arma_eq.nombre}. Reemplazando por {arma.nombre}.")
            self.poder -= self.arma_eq.poder_extra
        self.set_arma(arma)
        self.poder += arma.poder_extra
        print(f"{self.nombre} ha recogido {arma} de poder {arma.poder_extra}. Antes tenía {self.poder - arma.poder_extra} de poder, y ahora tiene {self.poder} de poder.")
        arma.recogida = True
