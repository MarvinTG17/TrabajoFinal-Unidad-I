#TAREA 2 
import requests
from metodosTarea2 import *

# Variables
reintentarMenu = True
generacion = 0

while reintentarMenu:
    op = menu_principal()

    if op == "1":
        generacion = int(input("\nIngrese que generacion de pokemons: \nPor jemplo: 1, 2, 3, ...  "))
        obtenerPokemonesXGeneracion(generacion)
    elif op == "2":
        lFormas = obtenerFormas(forma)
        print(f'Ingrese la forma de los pokemones: \nPor jemplo: {lFormas[0][0]}, {lFormas[1][0]} o {lFormas[2][0]}')
        forma = input()
        listarPokemonesXFormas(forma, lFormas)
    elif op == "3":
        lHabilidades = obtenerHabilidades(habilidad)
        print(f'Ingrese la habilidad de los pokemones: \nPor jemplo: {lHabilidades[0][0]}, {lHabilidades[1][0]} o {lHabilidades[2][0]}')
        habilidad = input()
        listarPokemonesXHabilidad(habilidad, lHabilidades)
    elif op == "4":
        habitad = input("\nIngrese el habitad de los pokemones.")
        obtenerHabitad(habitad)
    elif op == "5":
        tipo = input("\nIngrese el tipo de los pokemones.")
        obtenerTipos(tipo)
    elif op == "0":
        reintentarMenu = False
        continue
    else :
        reintentarMenu = True
    time.sleep(2)
    print("Retornando al menu")
    time.sleep(2)
print("Gracias por su participacion")