class Ente:
    def __init__(self):
        self.poder = 1
        self.posicion = None
        self.vidas = 5
        self.juego = None
    
    def get_juego(self):
        return self.juego
    
    def set_juego(self, unJuego):
        self.juego = unJuego

    def get_poder(self):
        return self.poder
    
    def set_poder(self, unPoder):
        self.poder = unPoder

    def get_posicion(self):
        return self.posicion
    
    def set_posicion(self, unaPosicion):
        self.posicion = unaPosicion
    
    def get_vidas(self):
        return self.vidas
    
    def set_vidas(self, unasVidas):
        self.vidas = unasVidas
    
    def esta_vivo(self):
        return self.vidas > 0
    
    def he_muerto():
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses should implement this!")

    def es_atacado_por(self, alguien):
        print(f"{self} es atacado por {alguien}")

        self.vidas = self.vidas - alguien.get_poder()
        print(f"{self} pierde {alguien.get_poder()} vidas y le quedan {self.vidas}")

        if self.vidas <= 0:
            self.he_muerto()
