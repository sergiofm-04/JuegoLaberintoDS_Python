# 🏰 Juego del Laberinto

Este juego ha sido desarrollado para la asignatura Diseño de Software del Grado en Ingeniería Informática de Albacete, en el curso 2024/25.

Este proyecto se ha llevado a cabo con ayuda de ChatGPT y GitHub Copilot a partir del repositorio https://github.com/sergiofm-04/JuegoLaberintoDS_Smalltalk.git realizado en Pharo Smalltalk.

El **Juego del Laberinto** consiste en que un jugador recorra habitaciones conectadas entre sí, siguiendo una estructura de laberinto. Las habitaciones pueden contener elementos como puertas, paredes, bombas o bichos.  
Los bichos actúan de acuerdo con su estrategia (agresiva o perezosa), y las habitaciones pueden tener decoraciones que afectan el comportamiento del juego.  
El jugador debe moverse entre las habitaciones, evitando obstáculos y enemigos, con el objetivo de encontrar la salida o superar desafíos definidos.  

---

## 📌 Características

✅ Estructura modular basada en orientación a objetos.  
✅ Implementación de múltiples patrones de diseño para garantizar flexibilidad, escalabilidad y reutilización del código.  
✅ Soporte para distintos tipos de elementos del mapa, como paredes, puertas, cofres, armas y habitaciones.  
✅ Interfaz gráfica con iconos para personajes, bichos, cofres y armas.  
✅ Refresco automático de la interfaz para mostrar el movimiento de los bichos en tiempo real.  
✅ Las puertas se dibujan en el lado correcto de cada habitación y su color indica si están abiertas (verde) o cerradas (rojo).  
✅ Los bichos muestran un icono distinto según su modo (agresivo, perezoso o hashashin).

---

## 🛠️ Patrones de Diseño Implementados

### 1. **Factory Method**
- **Uso**: Se utiliza en la clase `Creator` para fabricar elementos del laberinto como habitaciones, paredes, puertas y orientaciones (`Norte`, `Sur`, `Este`, `Oeste`). Esto permite crear instancias específicas sin acoplar el código a clases concretas.

### 2. **Decorator**
- **Uso**: La clase `Bomba` actúa como un decorador para los elementos del mapa, añadiendo funcionalidad adicional (como explotar) sin modificar la estructura original de las clases decoradas.

### 3. **Strategy**
- **Uso**: Los bichos (`Bicho`) utilizan el patrón Strategy para definir su comportamiento. Los modos `Agresivo` y `Perezoso` implementan estrategias diferentes para actuar, caminar y atacar.

### 4. **Composite**
- **Uso**: La clase `Contenedor` implementa el patrón Composite para representar la estructura jerárquica del laberinto. Esto permite tratar de manera uniforme a elementos simples (como paredes) y compuestos (como habitaciones con varios elementos).

### 5. **Iterator**
- **Uso**: Se utiliza en la clase `Contenedor` para recorrer los hijos y orientaciones de un contenedor, aplicando operaciones a cada uno de ellos de manera uniforme.

### 6. **Template Method**
- **Uso**: La clase `Modo` define un método plantilla (`actua`) que establece el flujo de acciones de los bichos (dormir, caminar, atacar). Las subclases (`Agresivo`, `Perezoso`) personalizan el comportamiento de cada paso.

### 7. **Abstract Factory**
- **Uso**: La clase `Creator` actúa como una fábrica abstracta para crear diferentes tipos de elementos del laberinto, permitiendo la creación de configuraciones específicas del juego.

### 8. **Singleton**
- **Uso**: Las clases de orientaciones (`Norte`, `Sur`, `Este`, `Oeste`) implementan el patrón Singleton para garantizar que solo exista una instancia de cada orientación en el juego.

### 9. **Builder**
- **Uso**: La clase `LaberintoBuilder` implementa el patrón Builder para construir laberintos complejos paso a paso, delegando la creación de habitaciones, puertas y otros elementos al `Director`.

### 10. **Proxy**
- **Uso**: Se utiliza para controlar el acceso a elementos del laberinto, como túneles o habitaciones protegidas, permitiendo realizar verificaciones antes de acceder al objeto real.

### 11. **Adapter**
- **Uso**: Permite integrar clases externas o incompatibles con la estructura del juego, adaptando su interfaz para que funcione con el sistema existente.

### 12. **Bridge**
- **Uso**: Separa la abstracción de la implementación en elementos como las puertas, permitiendo que diferentes tipos de puertas (por ejemplo, puertas mágicas o cerraduras) compartan la misma interfaz.

### 13. **Mediator**
- **Uso**: Coordina la interacción entre diferentes elementos del juego, como bichos y personajes, sin que estos se comuniquen directamente entre sí.

### 14. **State**
- **Uso**: Las puertas utilizan el patrón State para cambiar entre estados como `Abierta` y `Cerrada`, delegando el comportamiento al estado actual.

### 15. **Prototype**
- **Uso**: El laberinto utiliza el patrón Prototype para clonar configuraciones completas del laberinto, permitiendo crear copias profundas de estructuras complejas.

### 16. **Observer**
- **Uso**: Se utiliza para notificar a los elementos del juego (como bichos o personajes) cuando ocurren eventos importantes, como la activación de una bomba.

### 17. **Command**
- **Uso**: Permite encapsular acciones del jugador (como moverse o atacar) en objetos de comando, facilitando la implementación de funcionalidades como deshacer o repetir acciones.

### 18. **Visitor**
- **Uso**: Implementado en la clase `Visitor` para realizar operaciones sobre los elementos del laberinto sin modificar sus clases. Por ejemplo, `VisitorActivarBombas` activa todas las bombas en el laberinto.

---

## 📷 Diagrama UML

![alt text](<Diagrama Proyecto.png>)



*(Este diagrama muestra las clases y relaciones dentro del juego del laberinto, incluyendo todos los patrones implementados).*  

---

## ⚙️ Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/sergiofm-04/JuegoLaberintoDS_Python.git
   cd juego-laberinto

2. **Instala las dependencias necesarias (si las hubiera):**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ejecuta el juego:**
   ```sh
   python interfaz.py
   ```

---

## 🚀 Cómo Jugar

🖱️ Usa las teclas WASD para mover al personaje por el laberinto.
🖱️ Pulsa la tecla de ataque (espacio) para atacar a los bichos si tienes un arma equipada.
🖱️ Las armas solo aparecen en la habitación si están disponibles para recoger (no se muestran las armas dentro de cofres).
🖱️ Los cofres se muestran como iconos y pueden contener armas; para obtenerlas, entra a la habitación que contiene el cofre.
🖱️ El color de las puertas indica su estado: verde (abierta), rojo (cerrada).
🖱️ Los bichos se mueven automáticamente y su icono indica su modo de comportamiento (ver carpeta imágenes para el significado de cada imagen).

---

## 📂 Estructura del Proyecto

```
imagenes/
├── bicho_agr.png
└── ...
JuegoLaberinto/
│
├── Elementos/
|   ├── Builder/
│   │   ├── Director.py
|   |   └── LaberintoBuilder.py
|   ├── FactoryMethod/
│   │   ├── Creator.py
|   |   └── CreatorB.py
│   ├── Laberinto/
│   │   ├── Creator.py
│   │   ├── LaberintoBuilder.py
│   │   ├── Contenedor.py
│   │   ├── Habitacion.py
│   │   ├── Puerta.py
│   │   ├── Pared.py
│   │   ├── Bomba.py
│   │   ├── Orientacion.py
│   │   ├── Norte.py
│   │   ├── Sur.py
│   │   ├── Este.py
│   │   ├── Oeste.py
│   │   ├── Bicho.py
│   │   ├── Personaje.py
│   │   ├── Juego.py
│   │   └── ...
│   ├── Visitor/
│   │   │   ├── Visitor.py
|   |   |   └── ...
│   └── ...
│
├── Pruebas/
│   ├── LaberintoBuilderTest.py
│   ├── PruebasLaberinto.py
│   └── ...
│
interfaz.py
README.md
Diagrama Proyecto.png
...
```

---

## 🧑‍💻 Contribuciones

PROYECTO FINALIZADO A DÍA 1 DE JUNIO DE 2025.

---

## 📜 Licencia

No hay licencia establecida para este proyecto.