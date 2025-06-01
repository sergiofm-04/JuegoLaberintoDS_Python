import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from JuegoLaberinto.Elementos.Builder.Director import Director

class LaberintoApp(tk.Tk):
    def __init__(self, ruta_json):
        super().__init__()
        import sys
        class PrintRedirector:
            def __init__(self, mostrar_func):
                self.mostrar_func = mostrar_func
            def write(self, texto):
                if texto.strip():
                    self.mostrar_func(texto.strip())
            def flush(self):
                pass
        
        self.iconos = {
            "personaje": ImageTk.PhotoImage(Image.open("imagenes/heroe.png").resize((100, 100))),
            "bicho_per": ImageTk.PhotoImage(Image.open("imagenes/bicho_per.png").resize((60, 60))),
            "bicho_agr": ImageTk.PhotoImage(Image.open("imagenes/bicho_agr.png").resize((80, 80))),
            "bicho_has": ImageTk.PhotoImage(Image.open("imagenes/bicho_has.png").resize((80, 80))),
            "cofre": ImageTk.PhotoImage(Image.open("imagenes/cofre.png").resize((40, 40))),
            "espada": ImageTk.PhotoImage(Image.open("imagenes/espada.png").resize((40, 40))),
            "flecha": ImageTk.PhotoImage(Image.open("imagenes/flecha.png").resize((40, 40))),
            "daga": ImageTk.PhotoImage(Image.open("imagenes/daga.png").resize((40, 40))),
            "katana": ImageTk.PhotoImage(Image.open("imagenes/katana.png").resize((40, 40))),
            "vara": ImageTk.PhotoImage(Image.open("imagenes/vara.png").resize((40, 40))),
        }

        sys.stdout = PrintRedirector(self.mostrar_mensaje)
        self.title("Juego del Laberinto")
        self.geometry("900x700")
        self.juego = None
        self.personaje = None
        self.habitaciones_posiciones = {}

        self.panel_mensajes = ScrolledText(self, width=40, height=25, state='disabled')
        self.panel_mensajes.pack(side=tk.RIGHT, padx=10, pady=20, fill=tk.Y)

        # Inicializar el juego
        self.inicializar_juego(ruta_json)

        # Canvas para el laberinto
        self.canvas = tk.Canvas(self, width=700, height=600, bg="white")
        self.canvas.pack(pady=20)

        # Dibujar el laberinto y el personaje
        self.dibujar_laberinto()
        self.dibujar_bichos()
        self.dibujar_personaje()

        # Crear botones
        self.crear_botones()

        # Refrescar periódicamente la interfaz
        self.refresco_periodico()

        # Controles de movimiento
        self.bind("<w>", self.mover_personaje)
        self.bind("<s>", self.mover_personaje)
        self.bind("<a>", self.mover_personaje)
        self.bind("<d>", self.mover_personaje)
        self.bind("<space>", self.atacar_personaje)

    def inicializar_juego(self, ruta_json):
        director = Director()
        director.procesar(ruta_json)
        self.juego = director.obtener_juego()
        self.juego.director = director  # <-- Añade esta línea
        self.forma = director.dict.get('forma', None)
        self.juego.agregar_personaje("Héroe")
        self.personaje = self.juego.person
        self.juego.lanzar_bichos()

    def calcular_posiciones(self):
        desplazamientos = {
            "Norte": (0, -1),
            "Sur": (0, 1),
            "Este": (1, 0),
            "Oeste": (-1, 0),
        }
        ROOM_SIZE = 140  # Aumenta el tamaño de la habitación
        conexiones = {}
        for puerta in self.juego.director.dict["puertas"]:
            h1, or1, h2, or2 = puerta
            conexiones.setdefault(h1, []).append((or1, h2))
            conexiones.setdefault(h2, []).append((or2, h1))

        posiciones = {}
        visitados = set()
        from collections import deque
        queue = deque()
        habitaciones = [hab.num for hab in self.juego.laberinto.hijos]
        if not habitaciones:
            return
        posiciones[habitaciones[0]] = (0, 0)
        queue.append(habitaciones[0])
        visitados.add(habitaciones[0])

        while queue:
            actual = queue.popleft()
            x, y = posiciones[actual]
            for orientacion, vecino in conexiones.get(actual, []):
                dx, dy = desplazamientos.get(orientacion, (0, 0))
                nueva_pos = (x + dx, y + dy)
                if vecino not in posiciones:
                    posiciones[vecino] = nueva_pos
                    queue.append(vecino)
                    visitados.add(vecino)
        min_x = min(x for x, y in posiciones.values())
        min_y = min(y for x, y in posiciones.values())
        self.habitaciones_posiciones = {}
        for num, (x, y) in posiciones.items():
            self.habitaciones_posiciones[num] = (
                100 + (x - min_x) * (ROOM_SIZE + 60),
                100 + (y - min_y) * (ROOM_SIZE + 60)
            )

    def dibujar_laberinto(self):
        self.calcular_posiciones()
        ROOM_SIZE = 140  # Tamaño grande para habitaciones

        # Importa las clases de orientación
        from JuegoLaberinto.Elementos.Laberinto.Norte import Norte
        from JuegoLaberinto.Elementos.Laberinto.Sur import Sur
        from JuegoLaberinto.Elementos.Laberinto.Este import Este
        from JuegoLaberinto.Elementos.Laberinto.Oeste import Oeste
        from JuegoLaberinto.Elementos.Laberinto.Cofre import Cofre

        orientaciones_obj = {
            "Norte": Norte.default(),
            "Sur": Sur.default(),
            "Este": Este.default(),
            "Oeste": Oeste.default(),
        }

        for habitacion in self.juego.laberinto.hijos:
            x, y = self.habitaciones_posiciones[habitacion.num]
            self.canvas.create_rectangle(
                x, y, x + ROOM_SIZE, y + ROOM_SIZE, fill="lightblue", outline="black", width=4
            )
            self.canvas.create_text(
                x + ROOM_SIZE // 2, y + ROOM_SIZE // 2, text=f"H{habitacion.num}", fill="black", font=("Arial", 24, "bold")
            )

            # Dibuja cofres (solo el cofre, nunca las armas dentro)
            for hijo in getattr(habitacion, "hijos", []):
                if hasattr(hijo, "es_cofre") and hijo.es_cofre():
                    self.canvas.create_image(x + ROOM_SIZE // 2 + 50, y + ROOM_SIZE - 30, image=self.iconos["cofre"])

            # Dibuja armas sueltas en la habitación SOLO si no han sido recogidas y NO están en cofres
            offset_y = 30
            for hijo in getattr(habitacion, "hijos", []):
                # Solo dibuja armas cuyo padre NO es un cofre
                padre = getattr(hijo, "get_padre", lambda: None)()
                if padre and hasattr(padre, "es_cofre") and padre.es_cofre():
                    continue  # No dibujar armas que están dentro de cofres
                if hasattr(hijo, "es_espada_altair") and hijo.es_espada_altair() and not getattr(hijo, "recogida", False):
                    self.canvas.create_image(x + ROOM_SIZE - 40, y + offset_y, image=self.iconos["espada"])
                    offset_y += 40
                elif hasattr(hijo, "es_flecha_yaka") and hijo.es_flecha_yaka() and not getattr(hijo, "recogida", False):
                    self.canvas.create_image(x + ROOM_SIZE - 40, y + offset_y, image=self.iconos["flecha"])
                    offset_y += 40
                elif hasattr(hijo, "es_daga") and hijo.es_daga() and not getattr(hijo, "recogida", False):
                    self.canvas.create_image(x + ROOM_SIZE - 40, y + offset_y, image=self.iconos["daga"])
                    offset_y += 40
                elif hasattr(hijo, "es_katana") and hijo.es_katana() and not getattr(hijo, "recogida", False):
                    self.canvas.create_image(x + ROOM_SIZE - 40, y + offset_y, image=self.iconos["katana"])
                    offset_y += 40
                elif hasattr(hijo, "es_vara") and hijo.es_vara() and not getattr(hijo, "recogida", False):
                    self.canvas.create_image(x + ROOM_SIZE - 40, y + offset_y, image=self.iconos["vara"])
                    offset_y += 40

            # Dibuja puertas en los lados de la habitación según orientación y estado
            orientaciones_canvas = {
                "Norte": ((x + 30, y), (x + ROOM_SIZE - 30, y)),
                "Sur": ((x + 30, y + ROOM_SIZE), (x + ROOM_SIZE - 30, y + ROOM_SIZE)),
                "Este": ((x + ROOM_SIZE, y + 30), (x + ROOM_SIZE, y + ROOM_SIZE - 30)),
                "Oeste": ((x, y + 30), (x, y + ROOM_SIZE - 30)),
            }

            for orientacion, (p1, p2) in orientaciones_canvas.items():
                or_obj = orientaciones_obj[orientacion]
                puerta = None
                if hasattr(habitacion, "obtener_elemento_or"):
                    puerta = habitacion.obtener_elemento_or(or_obj)
                elif hasattr(habitacion, "obtenerElementoOr"):
                    puerta = habitacion.obtenerElementoOr(or_obj)
                if puerta and hasattr(puerta, "es_puerta") and puerta.es_puerta():
                    # Usa el método de la puerta para saber si está abierta
                    color = "green" if puerta.esta_abierta() else "red"
                    self.canvas.create_line(
                        p1[0], p1[1], p2[0], p2[1], fill=color, width=10
                    )

    def dibujar_personaje(self):
        ROOM_SIZE = 140
        if hasattr(self, 'personaje_icono'):
            self.canvas.delete(self.personaje_icono)
        if self.personaje and self.personaje.esta_vivo():
            habitacion_actual = self.personaje.posicion.num
            x, y = self.habitaciones_posiciones[habitacion_actual]
            self.personaje_icono = self.canvas.create_image(
                x + ROOM_SIZE // 2 - 50, y + ROOM_SIZE // 2 - 50, image=self.iconos["personaje"]
            )

    def dibujar_bichos(self):
        ROOM_SIZE = 140
        if hasattr(self, 'bichos_iconos'):
            for icono in self.bichos_iconos.values():
                self.canvas.delete(icono)
        self.bichos_iconos = {}
        for bicho in self.juego.bichos:
            if hasattr(bicho, "posicion") and bicho.esta_vivo():
                x, y = self.habitaciones_posiciones[bicho.posicion.num]
                # Selecciona el icono según el modo del bicho
                modo = getattr(bicho.modo, "__class__", type(bicho.modo)).__name__.lower()
                if "agresivo" in modo:
                    icono_img = self.iconos["bicho_agr"]
                elif "perezoso" in modo:
                    icono_img = self.iconos["bicho_per"]
                elif "hashashin" in modo:
                    icono_img = self.iconos["bicho_has"]
                icono = self.canvas.create_image(
                    x + ROOM_SIZE // 2, y + ROOM_SIZE // 2 + 30, image=icono_img
                )
                self.bichos_iconos[bicho] = icono

    def mover_personaje(self, event):
        key = event.keysym.lower()
        if key == "w":
            self.personaje.ir_al_norte()
        elif key == "s":
            self.personaje.ir_al_sur()
        elif key == "a":
            self.personaje.ir_al_oeste()
        elif key == "d":
            self.personaje.ir_al_este()
        self.refrescar_todo()

    def crear_botones(self):
        botones_frame = tk.Frame(self)
        botones_frame.pack(pady=10)
        abrir_puertas_btn = tk.Button(botones_frame, text="Abrir Puertas", command=self.abrir_puertas)
        abrir_puertas_btn.pack(side=tk.LEFT, padx=5)
        cerrar_puertas_btn = tk.Button(botones_frame, text="Cerrar Puertas", command=self.cerrar_puertas)
        cerrar_puertas_btn.pack(side=tk.LEFT, padx=5)
        atacar_btn = tk.Button(botones_frame, text="Atacar (Espacio)", command=self.atacar_personaje)
        atacar_btn.pack(side=tk.LEFT, padx=5)

    def abrir_puertas(self):
        print("Abriendo puertas...")
        self.juego.abrir_puertas()
        self.refrescar_todo()

    def cerrar_puertas(self):
        print("Cerrando puertas...")
        self.juego.cerrar_puertas()
        self.refrescar_todo()

    def atacar_personaje(self, event=None):
        if self.personaje:
            self.personaje.puede_atacar()
        self.refrescar_todo()

    def mostrar_mensaje(self, mensaje):
        def append():
            if self.winfo_exists():
                self.panel_mensajes.config(state='normal')
                self.panel_mensajes.insert(tk.END, mensaje + "\n")
                self.panel_mensajes.yview(tk.END)
                self.panel_mensajes.config(state='disabled')
        try:
            if self.winfo_exists():
                self.after(0, append)
        except RuntimeError:
            pass  # La ventana ya no existe

    def refrescar_todo(self):
        self.canvas.delete("all")
        self.dibujar_laberinto()
        self.dibujar_bichos()
        self.dibujar_personaje()
    
    def refresco_periodico(self):
        self.refrescar_todo()
        self.after(200, self.refresco_periodico)

if __name__ == "__main__":
    ruta_json = "C:\\Users\\sergi\\Desktop\\Proyectos DS\\Laberintos\\lab6HabInterfaz.json"
    app = LaberintoApp(ruta_json)
    app.mainloop()
