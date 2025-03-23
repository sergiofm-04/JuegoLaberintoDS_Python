from .Decorator import Decorator

class Bomba(Decorator):
    """
    Bomba es un EM que explota cuando está activa. Puede actuar como decorador.
    """

    def __init__(self):
        super().__init__()
        self.activa = False

    def get_activa(self):
        """Devuelve si la bomba está activa."""
        return self.activa

    def set_activa(self, activa):
        """Establece si la bomba está activa."""
        self.activa = activa

    def entrar(self, alguien):
        """
        Define la acción de entrar en la bomba.
        Si está activa, realiza una acción (como explotar).
        Si no está activa, delega la acción al elemento decorado.
        """
        if self.activa:
            print(f"{alguien} ha chocado con una bomba")
            # Aquí puedes implementar lógica adicional, como restar vidas, etc.
        else:
            if self.get_em():
                self.get_em().entrar(alguien)
