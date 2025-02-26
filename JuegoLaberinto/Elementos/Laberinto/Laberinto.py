import ElementoMapa

class Laberinto(ElementoMapa):
    """Clase que representa un laberinto compuesto por habitaciones."""

    def __init__(self):
        """Inicializa el laberinto con una lista vacía de habitaciones."""
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al laberinto."""
        self.habitaciones.append(habitacion)

    def eliminar_habitacion(self, habitacion):
        """Elimina una habitación del laberinto si existe."""
        if habitacion in self.habitaciones:
            self.habitaciones.remove(habitacion)
        else:
            print("No existe ese objeto habitación.")

    def entrar(self):
        """Define la lógica de entrada al laberinto (pendiente de implementación)."""
        print("Entrando en el laberinto...")  # Podría moverse a la habitación 1

    def obtener_habitacion(self, num):
        """Devuelve la habitación con el número dado, o None si no existe."""
        for habitacion in self.habitaciones:
            if habitacion.get_num() == num:
                return habitacion
        return None  # Equivalente a `nil` en Smalltalk

    def get_habitaciones(self):
        """Devuelve la lista de habitaciones."""
        return self.habitaciones

    def set_habitaciones(self, habitaciones):
        """Establece la lista de habitaciones."""
        self.habitaciones = habitaciones
