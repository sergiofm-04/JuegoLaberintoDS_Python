from .ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    """
    Contenedor es el Composite. Es un ElementoMapa que tiene hijos.
    """

    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
        self.este = None
        self.norte = None
        self.num = None
        self.oeste = None
        self.sur = None

    # Gestión de hijos
    def agregar_hijo(self, un_em):
        """Agrega un hijo al contenedor."""
        un_em.set_padre(self)
        self.hijos.append(un_em)

    def eliminar_hijo(self, un_em):
        """Elimina un hijo del contenedor."""
        try:
            self.hijos.remove(un_em)
        except ValueError:
            print("No existe ese objeto")

    def get_hijos(self):
        """Devuelve los hijos del contenedor."""
        return self.hijos

    def set_hijos(self, valor):
        """Establece los hijos del contenedor."""
        self.hijos = valor

    # Gestión de orientaciones
    def agregar_orientacion(self, una_or):
        """Agrega una orientación al contenedor."""
        self.orientaciones.append(una_or)

    def obtener_elemento_or(self, una_or):
        """Obtiene el elemento en una orientación específica."""
        return una_or.obtener_elemento_or_en(self)

    def get_orientaciones(self):
        """Devuelve las orientaciones del contenedor."""
        return self.orientaciones

    def set_orientaciones(self, valor):
        """Establece las orientaciones del contenedor."""
        self.orientaciones = valor

    def obtener_orientacion(self):
        """Obtiene una orientación aleatoria del contenedor."""
        import random
        if self.orientaciones:
            return random.choice(self.orientaciones)
        return None

    def poner_en_or(self, una_or, un_em):
        """Coloca un elemento en una orientación específica."""
        una_or.poner_elemento(un_em, self)

    # Métodos de acceso
    def get_este(self):
        return self.este

    def set_este(self, valor):
        self.este = valor

    def get_norte(self):
        return self.norte

    def set_norte(self, valor):
        self.norte = valor

    def get_num(self):
        return self.num

    def set_num(self, valor):
        self.num = valor

    def get_oeste(self):
        return self.oeste

    def set_oeste(self, valor):
        self.oeste = valor

    def get_sur(self):
        return self.sur

    def set_sur(self, valor):
        self.sur = valor

    # Recorrido
    def recorrer(self, un_bloque):
        """
        Aplica un bloque de código (función) al contenedor y a sus hijos.
        """
        un_bloque(self)
        for hijo in self.hijos:
            hijo.recorrer(un_bloque)
        for orientacion in self.orientaciones:
            orientacion.recorrer(un_bloque, contenedor=self)

    # Método de entrada
    def entrar(self, alguien):
        """
        Define la acción de entrar en el contenedor.
        """
        print(f"{alguien} está en {self}")
        alguien.posicion = self
