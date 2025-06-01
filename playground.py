from JuegoLaberinto.Elementos.Builder.Director import Director


dir = Director()
ruta = 'C:\\Users\\sergi\\Desktop\\Proyectos DS\\Laberintos\\'
dir.procesar(ruta + 'lab6Hab.json')

juego = dir.obtener_juego()
juego.agregar_personaje('Paco')
# juego.lanzar_bichos()

hab1 = juego.obtener_habitacion(1)
bicho1 = juego.bichos[0]
person = juego.person
person.vidas = 100
# hab1.entrar(person)
# hab1.entrar(bicho)

while True:
    comando = input("Ingrese un comando (0 para ayuda): ")
    if comando == '0':
        print("Comandos disponibles:")
        print("1: Ir al norte")
        print("2: Ir al sur")
        print("3: Ir al oeste")
        print("4: Ir al este")
        print("5: Atacar")
        print("6: Abrir puertas")
        print("7: Cerrar puertas")
        print("8: Salir del juego")
        print("9: Bicho ataca")
    elif comando == '1':
        person.ir_al_norte()
    elif comando == '2':
        person.ir_al_sur()
    elif comando == '3':
        person.ir_al_oeste()
    elif comando == '4':
        person.ir_al_este()
    elif comando == '5':
        person.atacar()
    elif comando == '6':
        juego.abrir_puertas()
    elif comando == '7':
        juego.cerrar_puertas()
    elif comando == '8':
        print("Saliendo del juego.")
        juego.terminar_bichos()
        break
    elif comando == '9':
        bicho1.atacar()
    else:
        print("Comando no reconocido. Intente de nuevo.")
