import random

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
    opciones = ["piedra", "papel", "tijera"]

    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower()

        if jugador not in opciones:
            print("Opción no válida.")
            continue

        computadora = random.choice(opciones)
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
        if input("¿Jugar de nuevo? (sí/no): ").lower() != "sí":
            break

import random
import getpass
import time

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

def jugar_multijugador():
    print("\n--- Modo Multijugador ---")
    
    # Jugador 1 elige en secreto
    jugador1 = getpass.getpass("Jugador 1, elige piedra, papel o tijera (no se mostrará en pantalla): ").lower()
    
    while jugador1 not in opciones:
        print("Opción inválida. Intenta nuevamente.")
        jugador1 = getpass.getpass("Jugador 1, elige piedra, papel o tijera: ").lower()

    print("\n" * 50)  # Limpia la pantalla simulando que el Jugador 2 no ve la elección
    
    # Jugador 2 elige
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

    while jugador2 not in opciones:
        print("Opción inválida. Intenta nuevamente.")
        jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

    # Mostrar las elecciones y el resultado
    print(f"\nJugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")

    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")


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



    



    





