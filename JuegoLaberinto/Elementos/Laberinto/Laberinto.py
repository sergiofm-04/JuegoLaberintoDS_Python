from .Contenedor import Contenedor

class Laberinto(Contenedor):
    """
    Clase Laberinto.
    """

    # Gestión de habitaciones
    def agregar_habitacion(self, una_habitacion):
        """Agrega una habitación al laberinto."""
        self.hijos.append(una_habitacion)

    def eliminar_habitacion(self, una_habitacion):
        """Elimina una habitación del laberinto."""
        try:
            self.hijos.remove(una_habitacion)
        except ValueError:
            print("No existe ese objeto habitación")

    def obtener_habitacion(self, un_num):
        """Obtiene una habitación por su número."""
        for each in self.hijos:
            if each.get_num() == un_num:
                return each
        return None

    # Puertas
    def abrir_puertas(self):
        """Abre todas las puertas del laberinto."""
        self.recorrer(lambda each: each.abrir() if each.es_puerta() else None)

    def cerrar_puertas(self):
        """Cierra todas las puertas del laberinto."""
        self.recorrer(lambda each: each.cerrar() if each.es_puerta() else None)

    # Movimiento
    def entrar(self, alguien):
        """Define la acción de entrar en el laberinto."""
        hab1 = self.obtener_habitacion(1)
        if hab1:
            hab1.entrar(alguien)

    # Impresión
    def __str__(self):
        """Devuelve una representación en texto del laberinto."""
        return "Laberinto"
