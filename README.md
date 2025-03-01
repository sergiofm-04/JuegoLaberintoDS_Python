# 🏰 Juego del Laberinto

Este juego ha sido desarrollado para la asignatura Diseño de Software del Grado en Ingeniería Informática de Albacete, en el curso 2024/25.

Este proyecto se ha llevado a cabo con ayuda de ChatGPT y GitHub Copilot a partir del repositorio https://github.com/sergiofm-04/JuegoLaberintoDS_Smalltalk.git realizado en Pharo Smalltalk.

El **Juego del Laberinto** consiste en que un jugador recorra habitaciones conectadas entre sí, siguiendo una estructura de laberinto. Las habitaciones pueden contener elementos como puertas, paredes, bombas o bichos.  
Los bichos actúan de acuerdo con su estrategia (agresiva o perezosa), y las habitaciones pueden tener decoraciones que afectan el comportamiento del juego.  
El jugador debe moverse entre las habitaciones, evitando obstáculos y enemigos, con el objetivo de encontrar la salida o superar desafíos definidos.  

---

## 📌 Características

✅ Estructura modular basada en orientación a objetos.  
✅ Implementación del **Patrón Factory Method** para la generación de habitaciones y paredes.  
✅ Soporte para distintos tipos de elementos del mapa, como paredes, puertas y habitaciones.  
✅ Implementación del **Patrón Decorator** para añadir dinámicamente nuevas funcionalidades a los elementos del mapa, como bombas o efectos especiales, sin modificar su estructura original.  
✅ Implementación del **Patrón Strategy** para definir diferentes comportamientos de los bichos (agresivos o perezosos) y permitir que cambien dinámicamente su forma de actuar sin modificar su código interno.  
✅ Implementación del **Patrón Composite** para representar la estructura jerárquica del laberinto, permitiendo tratar de manera uniforme a elementos simples (como paredes) y compuestos (como habitaciones con varios elementos).  
✅ Posibilidad de expandir el juego con nuevos elementos fácilmente.  

---

## 📷 Diagrama UML

![alt text](<Diagrama DS.png>)



*(Este diagrama muestra las clases y relaciones dentro del juego del laberinto, incluyendo todos los patrones implementados).*  

---

## ⚙️ Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/sergiofm-04/JuegoLaberintoDS_Python.git
   cd juego-laberinto
