class Bicho:
    def __init__(self):
        self.vidas = 5
        self.poder = 1
        self.modo = None
        self.posicion = None

    def actua(self):
        self.modo.actua(self)

    def es_agresivo(self):
        return self.modo.es_agresivo()

    def es_perezoso(self):
        return self.modo.es_perezoso()

    def ini_agresivo(self):
        import Agresivo  # Importación para evitar dependencias circulares
        self.set_modo(Agresivo())
        self.set_poder(10)

    def ini_perezoso(self):
        import Perezoso  # Importación para evitar dependencias circulares
        self.set_modo(Perezoso())
        self.set_poder(1)

    def get_modo(self):
        return self.modo

    def set_modo(self, an_object):
        self.modo = an_object

    def get_poder(self):
        return self.poder

    def set_poder(self, an_object):
        self.poder = an_object

    def get_posicion(self):
        return self.posicion

    def set_posicion(self, an_object):
        self.posicion = an_object

    def get_vidas(self):
        return self.vidas

    def set_vidas(self, an_object):
        self.vidas = an_object
