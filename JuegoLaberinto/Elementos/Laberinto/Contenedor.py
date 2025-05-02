from .ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    """
    Contenedor es el Composite. Es un ElementoMapa que tiene hijos.
    """

    def __init__(self):
        super().__init__()
        self.hijos = []
        self.forma = None
        self.num = None

    def aceptar(self, un_visitor):
        """
        Acepta un visitante (Visitor Pattern).
        """
        self.visitar_contenedor(un_visitor)
        for hijo in self.hijos:
            hijo.recorrer(un_visitor)

    # Gestión de hijos
    def agregar_hijo(self, un_em):
        """
        Agrega un hijo al contenedor.
        """
        un_em.set_padre(self)
        self.hijos.append(un_em)

    def eliminar_hijo(self, un_em):
        """
        Elimina un hijo del contenedor.
        """
        try:
            self.hijos.remove(un_em)
        except ValueError:
            print("No existe ese objeto.")

    def get_hijos(self):
        """
        Devuelve los hijos del contenedor.
        """
        return self.hijos

    def set_hijos(self, valor):
        """
        Establece los hijos del contenedor.
        """
        self.hijos = valor

    # Gestión de orientaciones
    def agregar_orientacion(self, una_or):
        """
        Agrega una orientación al contenedor.
        """
        if self.forma:
            self.forma.agregar_orientacion(una_or)

    def obtener_elemento_or(self, una_or):
        """
        Obtiene el elemento en una orientación específica.
        """
        #if self.forma:
        return self.forma.obtener_elemento_or(una_or)
        #return None

    def obtener_orientacion(self):
        """
        Obtiene una orientación aleatoria del contenedor.
        """
        if self.forma:
            return self.forma.obtener_orientacion()
        return None

    def obtener_orientaciones(self):
        """
        Devuelve las orientaciones del contenedor.
        """
        if self.forma:
            return self.forma.obtener_orientaciones()
        return []

    def poner_en_or(self, una_or, un_em):
        """
        Coloca un elemento en una orientación específica.
        """
        if self.forma:
            self.forma.poner_en_or(una_or, un_em)

    # Movimiento
    def ir_al_este(self, alguien):
        """
        Mueve a alguien al este.
        """
        if self.forma:
            self.forma.ir_al_este(alguien)

    def ir_al_norte(self, alguien):
        """
        Mueve a alguien al norte.
        """
        if self.forma:
            self.forma.ir_al_norte(alguien)

    def ir_al_oeste(self, alguien):
        """
        Mueve a alguien al oeste.
        """
        if self.forma:
            self.forma.ir_al_oeste(alguien)

    def ir_al_sur(self, alguien):
        """
        Mueve a alguien al sur.
        """
        if self.forma:
            self.forma.ir_al_sur(alguien)

    # Métodos de acceso
    def get_forma(self):
        return self.forma

    def set_forma(self, valor):
        self.forma = valor

    def get_num(self):
        return self.num

    def set_num(self, valor):
        self.num = valor

    # Recorrido
    def recorrer(self, un_bloque):
        """
        Aplica un bloque de código (función) al contenedor y a sus hijos.
        """
        un_bloque(self)
        for hijo in self.hijos:
            hijo.recorrer(un_bloque)
        for orientacion in self.obtener_orientaciones():
            orientacion.recorrer(un_bloque, contenedor=self)

    def visitar_contenedor(self, un_visitor):
        """
        Método abstracto para visitar el contenedor.
        """
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    # Método de entrada
    def entrar(self, alguien):
        """
        Define la acción de entrar en el contenedor.
        """
        print(f"{alguien} está en {self}")
        alguien.posicion = self
        alguien.buscar_tunel()
