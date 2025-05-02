from .Contenedor import Contenedor

class Habitacion(Contenedor):
    """
    Clase Habitacion.
    """

    def __init__(self):
        super().__init__()

    # Consulta
    def es_habitacion(self):
        """
        Indica que este objeto es una habitación.
        """
        return True

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto de la habitación.
        """
        return f"Hab{self.num}"

    # Visitor
    def visitar_contenedor(self, un_visitor):
        """
        Permite que un visitante interactúe con la habitación.
        """
        un_visitor.visitar_habitacion(self)

    def __eq__(self, other):
        if isinstance(other, Habitacion):
            return self.num == other.num
        return False
