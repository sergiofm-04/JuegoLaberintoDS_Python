import json
from .LaberintoBuilder import LaberintoBuilder
from .LaberintoBuilderRombo import LaberintoBuilderRombo

class Director:
    """
    Director procesa el archivo JSON que especifica el laberinto.
    También se encarga del proceso de creación.
    """

    def __init__(self):
        self.builder = None
        self.dict = None

    # Métodos de acceso
    def get_builder(self):
        return self.builder

    def set_builder(self, builder):
        self.builder = builder

    def get_dict(self):
        return self.dict

    def set_dict(self, data):
        self.dict = data

    # Métodos de fabricación
    def fabricar_bichos(self):
        """Recorre la colección de bichos y los fabrica."""
        bichos = self.dict.get('bichos', [])
        for each in bichos:
            modo = each.get('modo')
            posicion = each.get('posicion')
            self.builder.fabricar_bicho_modo(modo, posicion)

    def fabricar_juego(self):
        """Fabrica el juego."""
        self.builder.fabricar_juego()

    def fabricar_laberinto(self):
        """Fabrica el laberinto y sus componentes."""
        self.builder.fabricar_laberinto()

        # Procesar el laberinto recursivamente
        laberinto = self.dict.get('laberinto', [])
        for each in laberinto:
            self.fabricar_laberinto_recursivo(each, 'root')

        # Procesar las puertas
        puertas = self.dict.get('puertas', [])
        for each in puertas:
            self.builder.fabricar_puerta_l1(each[0], each[1], each[2], each[3])

    def fabricar_laberinto_recursivo(self, un_dic, padre):
        """Procesa el laberinto de forma recursiva."""
        con = None

        # Contenedores
        if un_dic.get('tipo') == 'habitacion':
            con = self.builder.fabricar_habitacion(un_dic.get('num'))
        elif un_dic.get('tipo') == 'armario':
            con = self.builder.fabricar_armario(un_dic.get('num'), padre)
        elif un_dic.get('tipo') == 'cofre':
            con = self.builder.fabricar_cofre(un_dic.get('num'), padre)

        # Hojas
        if un_dic.get('tipo') == 'bomba':
            self.builder.fabricar_bomba_en(padre)
        elif un_dic.get('tipo') == 'tunel':
            self.builder.fabricar_tunel_en(padre)
        elif un_dic.get('tipo') == 'espada':
            self.builder.fabricar_espada_en(padre)
        elif un_dic.get('tipo') == 'daga':
            self.builder.fabricar_daga_en(padre)
        elif un_dic.get('tipo') == 'katana':
            self.builder.fabricar_katana_en(padre)
        elif un_dic.get('tipo') == 'flecha':
            self.builder.fabricar_flecha_en(padre)
        elif un_dic.get('tipo') == 'vara':
            self.builder.fabricar_vara_en(padre)

        # Procesar hijos recursivamente
        hijos = un_dic.get('hijos', [])
        for each in hijos:
            self.fabricar_laberinto_recursivo(each, con)

    def ini_builder(self):
        """Inicializa el builder para crear laberintos diferentes."""
        forma = self.dict.get('forma')
        if forma == 'cuadrado':
            self.builder = LaberintoBuilder()
        elif forma == 'rombo':
            self.builder = LaberintoBuilderRombo()

    def leer_archivo(self, archivo):
        """Lee el archivo JSON y lo convierte en un diccionario."""
        with open(archivo, 'r') as file:
            self.dict = json.load(file)

    def obtener_juego(self):
        """Obtiene el juego creado por el builder."""
        return self.builder.obtener_juego()

    def procesar(self, archivo):
        """Procesa el archivo JSON y crea el laberinto."""
        self.leer_archivo(archivo)
        self.ini_builder()
        self.fabricar_laberinto()
        self.fabricar_juego()
        self.fabricar_bichos()
