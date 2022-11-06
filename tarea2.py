#TAREA 2 

import requests
import os
from metodosTarea2 import *

# Variables
reintentarMenu = True
generacion = 0

while reintentarMenu:
    op = menu_principal()

    if op == "1":
        generacion = int(input("\nIngrese que generacion de pokemons "))
        obtenerPokemonesXGeneracion(generacion)
    elif op == "2":
        forma = input("\nIngrese la forma de los pokemones.")
        obtenerFormas(forma)
    elif op == "3":
        habilidad = input("\nIngrese la habilidad de los pokemones.")
        obtenerHabilidades(habilidad)
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
    os.system ("cls") 
    print("Retornando al menu")
    time.sleep(2)
print("Gracias por su participacion")