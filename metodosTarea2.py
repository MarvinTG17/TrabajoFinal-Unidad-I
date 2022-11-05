import requests
import time

def menu_principal():
    print("\n--------MENU DE BIENVENIDA--------")
    print("\nEscoga un numero del menu:")
    print("Opcion 1 : Listar pokemons por generacion")
    print("Opcion 2 : Listar pokemons por forma")
    print("Opcion 3 : Listar pokemons por habilidad")
    print("Opcion 4 : Listar pokemons por habitad")
    print("Opcion 5 : Listar pokemons por tipo")
    print("Opcion 0 : Salir")

    opcion = input("\nIngresar la opcion de su preferencia: ")

    return opcion

# Imprimir listas
def imprimirListas(listasPokemones):
    print(listasPokemones)
    for posicion,pokemon in enumerate(listasPokemones, start=1):
        print(f'{posicion}.- Nombre pokemon: {pokemon[0]}') 
        print('     Habilidades:   ',' :: '.join(pokemon[1]))
        print(f'     URL Imagen:     {pokemon[2]}')
        time.sleep(1)

# Obtener Id del Pokemon
def obtenerIdPokemon(url):
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    pokemonId=detailPokemon['id']
    return pokemonId

# Obtener habilidades de un pokemon
def obtenerHabilidadesXPokemon(id):
    listaHabilidadesPokemon = []
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
    detailPokemon = result.json()
    listaHabilidadesPokemon=[pokemon['ability']['name'] for pokemon in detailPokemon['abilities']]
    return listaHabilidadesPokemon

# Obtener imagen frontal de un pokemon
def obtenerImagenXPokemon(id):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
    detailPokemon = result.json()
    imagenPokemon=detailPokemon['sprites']['front_default']
    return imagenPokemon


# Opcion 1:
def obtenerPokemonesXGeneracion(generacion):
    result = requests.get(f'https://pokeapi.co/api/v2/generation/{int(generacion)}/')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    listaPokemonesURL=[pokemon['url'] for pokemon in detailPokemon['pokemon_species']]
    listaIdPokemones=[obtenerIdPokemon(pokemonURL) for pokemonURL in listaPokemonesURL]
    listaHabilidades=[obtenerHabilidadesXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaImagenes=[obtenerImagenXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaNombreHabilidadImagen = [[listaPokemones[posicion],listaHabilidades[posicion],listaImagenes[posicion]] for posicion in range(len(listaPokemones))]
    imprimirListas(listaNombreHabilidadImagen)

# Opcion 2:

def obtenerFormas(forma):
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    detailPokemon = result.json()
    listaFormas=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    i=0
    posicion=0
    seEncontroForma = False
    for formas in listaFormas:
        if forma==formas:
            posicion=i
            seEncontroForma = True
            break
        i+=1

    if(seEncontroForma):
        listaPokemonesXForma=obtenerPokemonesXForma(listaURL[posicion])
        imprimirListas(listaPokemonesXForma)
    else:
        print(f'No se encontro la forma: {forma}, solicitada')

def obtenerPokemonesXForma(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    listaPokemonesURL=[pokemon['url'] for pokemon in detailPokemon['pokemon_species']]
    listaIdPokemones=[obtenerIdPokemon(pokemonURL) for pokemonURL in listaPokemonesURL]
    listaHabilidades=[obtenerHabilidadesXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaImagenes=[obtenerImagenXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaNombreHabilidadImagen = [[listaPokemones[posicion],listaHabilidades[posicion],listaImagenes[posicion]] for posicion in range(len(listaPokemones))]
    return listaNombreHabilidadImagen



# Opcion 3
def obtenerHabilidades(habilidad):
    result = requests.get(f'https://pokeapi.co/api/v2/ability/')
    detailPokemon = result.json()
    listaHabilidades=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    i=0
    posicion=0
    seEncontroHabilidad = False
    for habil in listaHabilidades:
        if habilidad==habil:
            posicion=i
            seEncontroHabilidad = True
            break
        i+=1
    
    if(seEncontroHabilidad):
        listaPokemonesXHabilidad=obtenerPokemonesXHabilidad(listaURL[posicion])
        imprimirListas(listaPokemonesXHabilidad)
    else:
        print(f'No se encontro la habilidad: {habilidad}, solicitada')


def obtenerPokemonesXHabilidad(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['pokemon']['name'] for pokemon in detailPokemon['pokemon']]
    listaPokemonesURL=[pokemon['pokemon']['url'] for pokemon in detailPokemon['pokemon']]
    listaIdPokemones=[obtenerIdPokemon(pokemonURL) for pokemonURL in listaPokemonesURL]
    listaHabilidades=[obtenerHabilidadesXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaImagenes=[obtenerImagenXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaNombreHabilidadImagen = [[listaPokemones[posicion],listaHabilidades[posicion],listaImagenes[posicion]] for posicion in range(len(listaPokemones))]
    return listaNombreHabilidadImagen
