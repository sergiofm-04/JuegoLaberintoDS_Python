from .Ente import Ente
from .Agresivo import Agresivo
from .Perezoso import Perezoso
from .Hashashin import Hashashin

class Bicho(Ente):
    """
    Bicho es el enemigo en el juego. Puede ser agresivo o perezoso.
    """

    def __init__(self):
        super().__init__()
        self.modo = None

    # Comportamiento
    def actua(self):
        """
        El bicho actúa según su estado y modo.
        """
        if self.estado_ente:
            self.estado_ente.actua(self)

    def puede_actuar(self):
        """
        Verifica si el bicho puede actuar según su modo.
        """
        if self.modo:
            self.modo.actua(self)

    # Aviso
    def avisar(self):
        """
        Notifica al juego que el bicho ha muerto.
        """
        if self.juego:
            self.juego.terminar_bicho(self)

    # Búsqueda de túneles
    def buscar_tunel(self):
        """
        El bicho busca un túnel según su modo.
        """
        if self.modo:
            self.modo.buscar_tunel_bicho(self)

    # Consulta
    def es_agresivo(self):
        """
        Devuelve True si el bicho es agresivo.
        """
        return self.modo.es_agresivo() if self.modo else False

    def es_perezoso(self):
        """
        Devuelve True si el bicho es perezoso.
        """
        return self.modo.es_perezoso() if self.modo else False

    # Inicialización
    def ini_agresivo(self):
        """
        Inicializa el bicho en modo agresivo.
        """
        self.modo = Agresivo()
        self.poder = 10

    def ini_perezoso(self):
        """
        Inicializa el bicho en modo perezoso.
        """
        self.modo = Perezoso()
        self.poder = 1
    
    def ini_hashashin(self):
        """
        Inicializa el bicho en modo hashashin.
        """
        self.modo = Hashashin()
        self.poder = 5

    # Acceso
    def get_modo(self):
        """
        Devuelve el modo del bicho.
        """
        return self.modo

    def set_modo(self, un_modo):
        """
        Establece el modo del bicho.
        """
        self.modo = un_modo

    # Orientación
    def obtener_orientacion(self):
        """
        Obtiene una orientación desde la posición actual.
        """
        if self.posicion:
            return self.posicion.obtener_orientacion()
        return None

    # Ataques
    def puede_atacar(self):
        """
        El bicho busca un personaje en el juego para atacar. Si es hashashin, busca otros bichos.
        """
        if isinstance(self.modo, Hashashin):
            self.juego.buscar_bicho(self)
        elif isinstance(self.modo, Agresivo):
            self.juego.buscar_personaje(self)

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto del bicho.
        """
        modo_str = str(self.modo) if self.modo else "Sin modo"
        return f"Bicho-{modo_str} en {self.posicion}"
    
    def cambiar_modo(self):
        """
        Cambia el modo del bicho entre agresivo y perezoso.
        """
        self.ini_hashashin()
        print("El bicho ha cambiado a modo Hashashin (fue atacado con la Espada de Altair).")
