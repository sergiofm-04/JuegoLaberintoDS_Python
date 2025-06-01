from .Contenedor import Contenedor

class Laberinto(Contenedor):
    """
    Clase Laberinto.
    """

    # Gestión de habitaciones
    def agregar_habitacion(self, una_habitacion):
        """
        Agrega una habitación al laberinto.
        """
        self.hijos.append(una_habitacion)

    def eliminar_habitacion(self, una_habitacion):
        """
        Elimina una habitación del laberinto.
        """
        try:
            self.hijos.remove(una_habitacion)
        except ValueError:
            print("No existe ese objeto habitación")

    def obtener_habitacion(self, un_num):
        """
        Obtiene una habitación por su número.
        """
        for each in self.hijos:
            if each.num == un_num:
                return each
        return None

    # Puertas
    def abrir_puertas(self):
        """
        Abre todas las puertas del laberinto.
        """
        self.recorrer(lambda each: each.abrir() if each.es_puerta() else None)

    def cerrar_puertas(self):
        """
        Cierra todas las puertas del laberinto.
        """
        self.recorrer(lambda each: each.cerrar() if each.es_puerta() else None)

    # Movimiento
    def entrar(self, alguien):
        """
        Define la acción de entrar en el laberinto.
        """
        hab1 = self.obtener_habitacion(1)
        if hab1:
            hab1.entrar(alguien)

    # Recorrido
    """def aceptar(self, un_visitor):
        
        Acepta un visitante (Visitor Pattern).
        
        for hijo in self.hijos:
            hijo.recorrer(un_visitor)"""
    
    def aceptar(self, un_visitor):
        self.visitar_contenedor(un_visitor)
        for hijo in self.hijos:
            hijo.aceptar(un_visitor)
        for orientacion in self.obtener_orientaciones():
            orientacion_elemento = self.forma.obtener_elemento_or(orientacion)
            if orientacion_elemento:
                orientacion_elemento.aceptar(un_visitor)

    def recorrer(self, un_bloque):
        """
        Aplica un bloque de código (función) al laberinto y a sus hijos.
        """
        un_bloque(self)
        for hijo in self.hijos:
            hijo.recorrer(un_bloque)

    # Impresión
    def __str__(self):
        """
        Devuelve una representación en texto del laberinto.
        """
        return "Laberinto"

    def visitar_contenedor(self, un_visitor):
        un_visitor.visitar_laberinto(self)
