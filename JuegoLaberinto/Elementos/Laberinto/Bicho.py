from .Ente import Ente
from .Agresivo import Agresivo
from .Perezoso import Perezoso

class Bicho(Ente):
    """
    Bicho es el enemigo en el juego. Puede ser agresivo o perezoso.
    """

    def __init__(self):
        super().__init__()
        self.modo = None

    # Comportamiento
    def actua(self):
        """El bicho actúa según su modo."""
        if self.modo:
            self.modo.actua(self)

    # Ataques
    def atacar(self):
        """El bicho ataca buscando un personaje en el juego."""
        if self.juego:
            self.juego.buscar_personaje(self)

    # Consulta
    def es_agresivo(self):
        """Devuelve True si el bicho es agresivo."""
        return self.modo.es_agresivo() if self.modo else False

    def es_perezoso(self):
        """Devuelve True si el bicho es perezoso."""
        return self.modo.es_perezoso() if self.modo else False

    # Muerte
    def he_muerto(self):
        """Acción a realizar cuando el bicho muere."""
        if self.juego:
            self.juego.terminar_bicho(self)

    # Inicialización
    def ini_agresivo(self):
        """Inicializa el bicho en modo agresivo."""
        self.modo = Agresivo()
        self.poder = 10

    def ini_perezoso(self):
        """Inicializa el bicho en modo perezoso."""
        self.modo = Perezoso()
        self.poder = 1

    # Acceso
    def get_modo(self):
        """Devuelve el modo del bicho."""
        return self.modo

    def set_modo(self, un_modo):
        """Establece el modo del bicho."""
        self.modo = un_modo

    # Orientación
    def obtener_orientacion(self):
        """Obtiene una orientación desde la posición actual."""
        if self.posicion:
            return self.posicion.obtener_orientacion()
        return None

    # Impresión
    def __str__(self):
        """Devuelve una representación en texto del bicho."""
        modo_str = str(self.modo) if self.modo else "Sin modo"
        return f"Bicho-{modo_str}"
