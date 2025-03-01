class Modo:
    """
    Modo es la interfaz de la estrategia de los bichos.
    """

    def actua(self, unBicho):
        """Template Method"""
        # self.duerme()
        self.camina(unBicho)
        # self.ataca()

    def camina(self, unBicho):
        """Definir un caminar predeterminado para todos"""
        raise NotImplementedError("Subclasses should implement this!")

    def es_agresivo(self):
        return False

    def es_perezoso(self):
        return False
