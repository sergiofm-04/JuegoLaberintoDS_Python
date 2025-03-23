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
✅ Soporte para distintos tipos de elementos del mapa, como paredes, puertas y habitaciones.  
✅ Posibilidad de expandir el juego con nuevos elementos fácilmente.

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
   python main.py
   ```

---

## 🚀 Cómo Jugar

(Más adelante...)

---

## 📂 Estructura del Proyecto

```
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
│   ├── Laberinto/
│   │   │   ├── Creator.py
│   └── ...
│
├── Pruebas/
│   ├── test_laberinto.py
│   ├── test_bichos.py
│   └── ...
│
├── main.py
├── README.md
└── Diagrama.png
```

---

## 🧑‍💻 Contribuciones

No se aceptan contribuciones al menos hasta la finalización del proyecto para la asignatura (mes de mayo).

---

## 📜 Licencia

No hay licencia establecida para este proyecto.