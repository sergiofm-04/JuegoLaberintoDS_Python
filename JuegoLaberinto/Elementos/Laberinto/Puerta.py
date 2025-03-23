from .ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    """
    Clase que representa una puerta en el laberinto.
    """

    def __init__(self):
        """Inicializa la puerta cerrada y sin lados asignados."""
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    # Métodos de acceso
    def get_abierta(self):
        """Devuelve si la puerta está abierta."""
        return self.abierta

    def set_abierta(self, estado):
        """Establece si la puerta está abierta."""
        self.abierta = estado

    def get_lado1(self):
        """Devuelve el primer lado de la puerta."""
        return self.lado1

    def set_lado1(self, habitacion):
        """Asigna el primer lado de la puerta a una habitación."""
        self.lado1 = habitacion

    def get_lado2(self):
        """Devuelve el segundo lado de la puerta."""
        return self.lado2

    def set_lado2(self, habitacion):
        """Asigna el segundo lado de la puerta a una habitación."""
        self.lado2 = habitacion

    # Métodos de estado
    def abrir(self):
        """Abre la puerta."""
        self.set_abierta(True)
        print("La puerta está abierta.")

    def cerrar(self):
        """Cierra la puerta."""
        self.set_abierta(False)
        print("La puerta está cerrada.")

    # Movimiento
    def entrar(self, alguien):
        """
        Define la acción de entrar en la puerta.
        Si está abierta, mueve a alguien al lado opuesto.
        """
        if self.abierta:
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
            print("La puerta está cerrada.")

    # Consulta
    def es_puerta(self):
        """Indica que este objeto es una puerta."""
        return True

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto de la puerta.
        Incluye los números de las habitaciones conectadas y su estado.
        """
        lado1_num = self.lado1.num if self.lado1 else "None"
        lado2_num = self.lado2.num if self.lado2 else "None"
        estado = "abierta" if self.abierta else "cerrada"
        return f"Puerta {lado1_num}-{lado2_num} ({estado})"
