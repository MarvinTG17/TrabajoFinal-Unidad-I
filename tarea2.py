#TAREA 2 

import requests
#   PREGUNTA 12 

# generacion > 8 O vacio: que vuelva a poner una generacion
# Maquillar el resultado

def obtenerPokemonesXGeneracion(generacion):
    result = requests.get(f'https://pokeapi.co/api/v2/generation/{int(generacion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    print(listaPokemones)



generacion = int(input("Ingresa numero de geme: "))
print("Eligio la generacion : ", str(generacion))

obtenerPokemonesXGeneracion(generacion)



# PREGUNTA 2

# Sugerir formas
# forma vacio: que vuelva a poner una generacion
# Maquillar el resultado


def obtenerFormas(forma):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    detailPokemon = result.json()
    listaFormas=[pokemon['name'] for pokemon in detailPokemon['results']]
    i=0
    posicion=0
    for formas in listaFormas:
        i+=1
        if forma==formas:
            posicion=i
    print(posicion)
    listaPokemonesXForma=obtenerPokemonesXForma(posicion)

    print(listaPokemonesXForma)

def obtenerPokemonesXForma(posicion):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/{int(posicion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    print(listaPokemones)

habilidad = input("Ingresa una habilidad: ")
print("Eligio la generacion : ", habilidad)

obtenerFormas(habilidad)


# PREGUNTA 3
def obtenerFormas(habilidad):
    result = requests.get(f'https://pokeapi.co/api/v2/ability/')
    detailPokemon = result.json()
    listaFormas=[pokemon['name'] for pokemon in detailPokemon['results']]
    i=0
    posicion=0
    for formas in listaFormas:
        i+=1
        if habilidad==formas:
            posicion=i
    print(posicion)
    listaPokemonesXForma=obtenerPokemonesXForma(posicion)

    print(listaPokemonesXForma)

def obtenerPokemonesXForma(posicion):
    result = requests.get(f'https://pokeapi.co/api/v2/ability/{int(posicion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['pokemon']['name'] for pokemon in detailPokemon['pokemon']]
    print(listaPokemones)

habilidad = input("Ingresa una habilidad: ")
print("Eligio la habilidad : ", habilidad)

obtenerFormas(habilidad)

# PREGUNTA 4
def obtenerFormas(forma):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat/')
    detailPokemon = result.json()
    listaFormas=[pokemon['name'] for pokemon in detailPokemon['results']]
    i=0
    posicion=0
    for formas in listaFormas:
        i+=1
        if forma==formas:
            posicion=i
    print(posicion)
    listaPokemonesXForma=obtenerPokemonesXForma(posicion)

    print(listaPokemonesXForma)

def obtenerPokemonesXForma(posicion):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat/{int(posicion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    print(listaPokemones)

habilidad = input("Ingresa un habitat: ")
print("Eligio el habitat: ", habilidad)

obtenerFormas(habilidad)


# PREGUNTA 5


def obtenerTipos(tipo):
    result = requests.get(f'https://pokeapi.co/api/v2/type/')
    detailPokemon = result.json()
    forma=""
    listaTipos=[pokemon['name'] for pokemon in detailPokemon['results']]
    print(listaTipos)
    i=0
    posicion=0
    for tipos in listaTipos:
        i+=1
        if tipo==tipos:
            posicion=i
    print(posicion)
    listaPokemonesXTipo=obtenerPokemonesXTipo(posicion)

    print(listaPokemonesXTipo)

def obtenerPokemonesXTipo(posicion):
    result = requests.get(f'https://pokeapi.co/api/v2/type/{int(posicion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['pokemon'] for pokemon in detailPokemon['pokemon']]
    listaPokemonesTipo=[pokemon['name'] for pokemon in listaPokemones]
    print(listaPokemonesTipo)

tipo = input("Ingresa un tipo: ")
print("Eligio el tipo : ", tipo)

obtenerTipos(tipo)