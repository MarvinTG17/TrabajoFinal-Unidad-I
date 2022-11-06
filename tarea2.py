#TAREA 2 
import requests
from funciones_tarea2 import *

# Variables
reintentarMenu = True
generacion = 0

while reintentarMenu:
    op = menu_principal()

    if op == "1":
        generacion = input("\nIngrese que generacion de pokemons: \nPor jemplo: 1, 2, 3, ...  ")
        try:
            generacion = int(generacion)
            obtenerPokemonesXGeneracion(generacion)
        except ValueError:
            print("Ingrese un valor numerico por favor.")
        
    elif op == "2":
        lFormas = obtenerFormas()
        print(f'Ingrese la forma de los pokemones: \nPor jemplo: {lFormas[0][0]}, {lFormas[1][0]} o {lFormas[2][0]}')
        forma = input()
        listarPokemonesXFormas(forma, lFormas)
    elif op == "3":
        lHabilidades = obtenerHabilidades()
        print(f'Ingrese la habilidad de los pokemones: \nPor jemplo: {lHabilidades[0][0]}, {lHabilidades[1][0]} o {lHabilidades[2][0]}')
        habilidad = input()
        listarPokemonesXHabilidad(habilidad, lHabilidades)
    elif op == "4":
        lHabitad = obtenerHabitad()
        print(f'Ingrese el habitad de los pokemones: \nPor jemplo: {lHabitad[0][0]}, {lHabitad[1][0]} o {lHabitad[2][0]}')
        habitad = input()
        listarPokemonesXHabitad(habitad, lHabitad)
    elif op == "5":
        lTipos = obtenerTipos()
        print(f'Ingrese el tipo de los pokemones: \nPor jemplo: {lTipos[0][0]}, {lTipos[1][0]} o {lTipos[2][0]}')
        tipo = input()
        listarPokemonesXTipo(tipo, lTipos)
    elif op == "0":
        reintentarMenu = False
        continue
    else :
        reintentarMenu = True
    time.sleep(2)
    print("Retornando al menu")
    time.sleep(2)
print("Gracias por su participacion")