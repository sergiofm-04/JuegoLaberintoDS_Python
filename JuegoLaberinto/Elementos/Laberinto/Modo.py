class Modo:
    """
    Modo es la interfaz de la estrategia de los bichos.
    """

    def actua(self, un_bicho):
        """
        Template Method: Define el flujo de acciones del bicho.
        """
        self.dormir(un_bicho)
        self.caminar(un_bicho)
        self.atacar(un_bicho)

    def atacar(self, un_bicho):
        """
        Realiza un ataque utilizando el método atacar del bicho.
        """
        un_bicho.atacar()

    def caminar(self, un_bicho):
        """
        El bicho elige una orientación aleatoria y camina hacia ella.
        """
        orientacion = un_bicho.obtener_orientacion()
        if orientacion:
            orientacion.caminar(un_bicho)

    def dormir(self, un_bicho):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        raise NotImplementedError("Subclasses should implement this!")

    def es_agresivo(self):
        """
        Devuelve False por defecto. Las subclases pueden sobrescribir este método.
        """
        return False

    def es_perezoso(self):
        """
        Devuelve False por defecto. Las subclases pueden sobrescribir este método.
        """
        return False
