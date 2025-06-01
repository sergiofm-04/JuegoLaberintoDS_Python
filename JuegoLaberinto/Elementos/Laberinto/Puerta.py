from .ElementoMapa import ElementoMapa
from .Cerrada import Cerrada

class Puerta(ElementoMapa):
    """
    Clase que representa una puerta en el laberinto.
    """

    def __init__(self):
        """
        Inicializa la puerta con un estado cerrado y sin lados asignados.
        """
        super().__init__()
        self.lado1 = None
        self.lado2 = None
        self.estado = Cerrada()  # Estado inicial

    # Métodos de estado
    def abrir(self):
        """
        Abre la puerta.
        """
        self.estado.abrir(self)

    def cerrar(self):
        """
        Cierra la puerta.
        """
        self.estado.cerrar(self)

    # Movimiento
    def entrar(self, alguien):
        """
        Define la acción de entrar en la puerta.
        """
        self.estado.entrar(alguien, self)

    def puede_entrar(self, alguien):
        """
        Permite que alguien entre por la puerta si está abierta.
        """
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    # Consulta
    def es_puerta(self):
        """
        Indica que este objeto es una puerta.
        """
        return True

    def esta_abierta(self):
        """
        Devuelve si la puerta está abierta.
        """
        return self.estado.esta_abierta()

    # Métodos de acceso
    def get_estado(self):
        """
        Devuelve el estado actual de la puerta.
        """
        return self.estado

    def set_estado(self, estado):
        """
        Establece el estado de la puerta.
        """
        self.estado = estado

    def get_lado1(self):
        """
        Devuelve el primer lado de la puerta.
        """
        return self.lado1

    def set_lado1(self, habitacion):
        """
        Asigna el primer lado de la puerta a una habitación.
        """
        self.lado1 = habitacion

    def get_lado2(self):
        """
        Devuelve el segundo lado de la puerta.
        """
        return self.lado2

    def set_lado2(self, habitacion):
        """
        Asigna el segundo lado de la puerta a una habitación.
        """
        self.lado2 = habitacion

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto de la puerta.
        Incluye los números de las habitaciones conectadas y su estado.
        """
        lado1_num = self.lado1.num if self.lado1 else "None"
        lado2_num = self.lado2.num if self.lado2 else "None"
        return f"Puerta {lado1_num}-{lado2_num} ({self.estado})"

    def aceptar(self, un_visitor):
        un_visitor.visitar_puerta(self)
