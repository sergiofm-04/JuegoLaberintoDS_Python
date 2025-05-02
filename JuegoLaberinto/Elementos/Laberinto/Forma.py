import random

class Forma:
    """
    Forma representa la implementación de un contenedor. Puede ser cuadrado...
    """

    def __init__(self):
        """
        Inicializa la forma con una lista vacía de orientaciones.
        """
        self.orientaciones = []

    # Gestión de orientaciones
    def agregar_orientacion(self, una_or):
        """
        Agrega una orientación a la lista de orientaciones.
        """
        self.orientaciones.append(una_or)

    def obtener_elemento_or(self, una_or):
        """
        Obtiene el elemento en una orientación específica.
        """
        return una_or.obtener_elemento_or_en(self)

    def obtener_orientacion(self):
        """
        Obtiene una orientación aleatoria de la lista de orientaciones.
        """
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None

    def obtener_orientaciones(self):
        """
        Devuelve la lista de orientaciones.
        """
        return self.orientaciones

    def poner_en_or(self, una_or, un_em):
        """
        Coloca un elemento en una orientación específica.
        """
        una_or.poner_elemento(un_em, self)

    # Movimiento
    def ir_al_este(self, alguien):
        """
        Mueve a alguien al este.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def ir_al_norte(self, alguien):
        """
        Mueve a alguien al norte.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def ir_al_oeste(self, alguien):
        """
        Mueve a alguien al oeste.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def ir_al_sur(self, alguien):
        """
        Mueve a alguien al sur.
        Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    # Acceso
    def get_orientaciones(self):
        """
        Devuelve la lista de orientaciones.
        """
        return self.orientaciones

    def set_orientaciones(self, orientaciones):
        """
        Establece la lista de orientaciones.
        """
        self.orientaciones = orientaciones
