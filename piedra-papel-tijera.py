import random
import getpass

# Variables globales
historial = []
victorias_jugador1 = 0
victorias_jugador2 = 0
victorias_computadora = 0
empates = 0
partidas_totales = 0

# Función para mostrar el menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar contra la computadora")
        print("2. Jugar multijugador (2 jugadores)")
        print("3. Ver estadísticas")
        print("4. Reglas del juego")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar_vs_computadora()
        elif opcion == "2":
            jugar_multijugador()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            mostrar_reglas()
        elif opcion == "5":
            print("Saliendo del juego... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función para jugar contra la computadora
def jugar_vs_computadora():
    global victorias_jugador1, victorias_computadora, empates, partidas_totales

    # Solicitar el nombre del jugador
    jugador_nombre = input("¡Hola! ¿Cuál es tu nombre? ")

    # Solicitar el número de partidas
    while True:
        try:
            num_partidas = int(input(f"¿Cuántas partidas desea jugar, {jugador_nombre}? "))
            if num_partidas <= 0:
                print("Por favor, ingresa un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    opciones = ["piedra", "papel", "tijera"]

    # Jugar el número de partidas especificado
    for _ in range(num_partidas):
        print(f"\nPartida {_ + 1} de {num_partidas}")

        # Recoger las elecciones de ambos jugadores sin mostrar aún
        jugador = getpass.getpass(f"{jugador_nombre}, elige piedra, papel o tijera: ").lower()
        while jugador not in opciones:
            print("Opción no válida.")
            jugador = getpass.getpass(f"{jugador_nombre}, elige piedra, papel o tijera: ").lower()

        computadora = random.choice(opciones)

        # Mostrar las elecciones después de que ambos jugadores elijan
        print(f"\n{jugador_nombre} eligió: {jugador}")
        print(f"La computadora eligió: {computadora}")

        if jugador == computadora:
            print("¡Empate!")
            empates += 1
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
            victorias_jugador1 += 1
        else:
            print("Perdiste.")
            victorias_computadora += 1

        partidas_totales += 1

    # Mostrar estadísticas y el historial después de todas las partidas
    print("\n--- Estadísticas ---")
    print(f"Jugador: {jugador_nombre} - Ganó {victorias_jugador1} partidas, Perdió {victorias_computadora} partidas, Empató {empates} partidas")
    print(f"Computadora: Ganó {victorias_computadora} partidas, Perdió {victorias_jugador1} partidas, Empató {empates} partidas")

    print("\n--- Historial ---")
    historial.append(f"{jugador_nombre}: Ganó {victorias_jugador1}, Perdió {victorias_computadora}, Empató {empates}")
    for entry in historial:
        print(entry)

# Función para jugar multijugador
def jugar_multijugador():
    global victorias_jugador1, victorias_jugador2, empates, partidas_totales

    print("\n--- Modo Multijugador ---")

    # Solicitar nombres de los jugadores
    jugador1_nombre = input("Jugador 1, ¿cuál es tu nombre? ")
    jugador2_nombre = input("Jugador 2, ¿cuál es tu nombre? ")

    # Solicitar el número de partidas
    while True:
        try:
            num_partidas = int(input(f"¿Cuántas partidas desea jugar, {jugador1_nombre} y {jugador2_nombre}? "))
            if num_partidas <= 0:
                print("Por favor, ingresa un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    opciones = ["piedra", "papel", "tijera"]

    # Jugar el número de partidas especificado
    for _ in range(num_partidas):
        print(f"\nPartida {_ + 1} de {num_partidas}")

        # Recoger las elecciones de ambos jugadores sin mostrar aún
        jugador1 = getpass.getpass(f"{jugador1_nombre}, elige piedra, papel o tijera: ").lower()
        while jugador1 not in opciones:
            print("Opción no válida.")
            jugador1 = getpass.getpass(f"{jugador1_nombre}, elige piedra, papel o tijera: ").lower()

        jugador2 = getpass.getpass(f"{jugador2_nombre}, elige piedra, papel o tijera: ").lower()
        while jugador2 not in opciones:
            print("Opción no válida.")
            jugador2 = getpass.getpass(f"{jugador2_nombre}, elige piedra, papel o tijera: ").lower()

        # Mostrar las elecciones después de que ambos jugadores elijan
        print(f"\n{jugador1_nombre} eligió: {jugador1}")
        print(f"{jugador2_nombre} eligió: {jugador2}")

        if jugador1 == jugador2:
            print("¡Es un empate!")
            empates += 1
        elif (jugador1 == "piedra" and jugador2 == "tijera") or \
             (jugador1 == "papel" and jugador2 == "piedra") or \
             (jugador1 == "tijera" and jugador2 == "papel"):
            print(f"¡{jugador1_nombre} gana!")
            victorias_jugador1 += 1
        else:
            print(f"¡{jugador2_nombre} gana!")
            victorias_jugador2 += 1

        partidas_totales += 1

    # Mostrar estadísticas y el historial después de todas las partidas
    print("\n--- Estadísticas ---")
    print(f"{jugador1_nombre}: Ganó {victorias_jugador1} partidas, Perdió {victorias_jugador2} partidas, Empató {empates} partidas")
    print(f"{jugador2_nombre}: Ganó {victorias_jugador2} partidas, Perdió {victorias_jugador1} partidas, Empató {empates} partidas")

    print("\n--- Historial ---")
    historial.append(f"{jugador1_nombre}: Ganó {victorias_jugador1}, Perdió {victorias_jugador2}, Empató {empates}")
    historial.append(f"{jugador2_nombre}: Ganó {victorias_jugador2}, Perdió {victorias_jugador1}, Empató {empates}")
    for entry in historial:
        print(entry)

# Función para mostrar las estadísticas
def mostrar_estadisticas():
    print("\n--- Estadísticas ---")
    print(f"Jugador 1: ganó {victorias_jugador1} partidas, perdió {victorias_computadora + victorias_jugador2} partidas, empató {empates} partidas")
    print(f"Jugador 2: ganó {victorias_jugador2} partidas, perdió {victorias_jugador1} partidas, empató {empates} partidas")
    print(f"Computadora: ganó {victorias_computadora} partidas, perdió {victorias_jugador1} partidas, empató {empates} partidas")

# Función para mostrar las reglas del juego
def mostrar_reglas():
    print("\n--- Reglas del Juego ---")
    print("1. Piedra gana contra tijera.")
    print("2. Tijera gana contra papel.")
    print("3. Papel gana contra piedra.")
    print("4. En caso de elegir la misma opción, es un empate.")
    print("5. ¡Disfruta el juego y diviértete!")

# Iniciar el menú
menu()



    



    





