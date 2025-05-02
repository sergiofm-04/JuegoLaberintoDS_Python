from tkinter import Tk, Label, Button, Entry, StringVar, Canvas, messagebox
from JuegoLaberinto.Elementos.Laberinto.Juego import Juego
from JuegoLaberinto.Elementos.FactoryMethod.Creator import Creator

class LaberintoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏰 Juego del Laberinto 🏰")

        # Crear el juego y el laberinto
        self.juego = Juego()
        self.creator = Creator()
        self.laberinto = self.juego.crear_laberinto_2_habitaciones_fm(self.creator)

        # Variables
        self.nombre_personaje = StringVar()

        # Interfaz inicial
        self.label_bienvenida = Label(root, text="Bienvenido al Juego del Laberinto", font=("Arial", 16))
        self.label_bienvenida.pack(pady=10)

        self.label_nombre = Label(root, text="Introduce el nombre de tu personaje:")
        self.label_nombre.pack()

        self.entry_nombre = Entry(root, textvariable=self.nombre_personaje)
        self.entry_nombre.pack()

        self.boton_iniciar = Button(root, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=10)

        # Canvas para el laberinto
        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Controles del juego
        self.label_accion = Label(root, text="", font=("Arial", 14))
        self.boton_norte = Button(root, text="Ir al Norte", command=self.ir_al_norte, state="disabled")
        self.boton_sur = Button(root, text="Ir al Sur", command=self.ir_al_sur, state="disabled")
        self.boton_este = Button(root, text="Ir al Este", command=self.ir_al_este, state="disabled")
        self.boton_oeste = Button(root, text="Ir al Oeste", command=self.ir_al_oeste, state="disabled")
        self.boton_salir = Button(root, text="Salir del Juego", command=self.salir)

    def iniciar_juego(self):
        nombre = self.nombre_personaje.get()
        if not nombre:
            messagebox.showerror("Error", "Por favor, introduce un nombre para tu personaje.")
            return

        self.juego.agregar_personaje(nombre)
        self.label_accion.config(text=f"¡Bienvenido, {nombre}! ¿A dónde quieres ir?")
        self.label_accion.pack(pady=10)

        # Mostrar botones de movimiento
        self.boton_norte.pack(pady=5)
        self.boton_sur.pack(pady=5)
        self.boton_este.pack(pady=5)
        self.boton_oeste.pack(pady=5)
        self.boton_salir.pack(pady=10)

        # Habilitar botones
        self.boton_norte.config(state="normal")
        self.boton_sur.config(state="normal")
        self.boton_este.config(state="normal")
        self.boton_oeste.config(state="normal")

        # Dibujar el laberinto inicial
        self.dibujar_laberinto()

    def dibujar_laberinto(self):
        """
        Dibuja el laberinto en el canvas.
        """
        self.canvas.delete("all")  # Limpiar el canvas
        # Dibujar habitaciones y conexiones (puertas, paredes)
        self.canvas.create_rectangle(50, 50, 150, 150, fill="lightblue", outline="black", tags="hab1")
        self.canvas.create_rectangle(200, 50, 300, 150, fill="lightblue", outline="black", tags="hab2")
        self.canvas.create_rectangle(150, 90, 200, 110, fill="brown", outline="black", tags="puerta")

        # Dibujar al personaje en la primera habitación
        self.personaje = self.canvas.create_oval(80, 80, 120, 120, fill="red", tags="personaje")

    def mover_personaje(self, dx, dy):
        """
        Mueve al personaje en el canvas.
        """
        self.canvas.move("personaje", dx, dy)

    def ir_al_norte(self):
        if self.juego.person.posicion.norte is None:
            self.notificar("Has chocado con una pared al Norte.")
        else:
            self.juego.person.ir_al_norte()
            self.actualizar_estado("Norte")
            self.mover_personaje(0, -50)

    def ir_al_sur(self):
        if self.juego.person.posicion.sur is None:
            self.notificar("Has chocado con una pared al Sur.")
        else:
            self.juego.person.ir_al_sur()
            self.actualizar_estado("Sur")
            self.mover_personaje(0, 50)

    def ir_al_este(self):
        if self.juego.person.posicion.este is None:
            self.notificar("Has chocado con una pared al Este.")
        else:
            self.juego.person.ir_al_este()
            self.actualizar_estado("Este")
            self.mover_personaje(150, 0)

    def ir_al_oeste(self):
        if self.juego.person.posicion.oeste is None:
            self.notificar("Has chocado con una pared al Oeste.")
        else:
            self.juego.person.ir_al_oeste()
            self.actualizar_estado("Oeste")
            self.mover_personaje(-150, 0)

    def notificar(self, mensaje):
        """
        Muestra una notificación en la interfaz.
        """
        messagebox.showinfo("Movimiento", mensaje)

    def actualizar_estado(self, direccion):
        self.label_accion.config(text=f"Te has movido hacia el {direccion}.")

    def salir(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = LaberintoGUI(root)
    root.mainloop()
