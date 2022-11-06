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
    #print(listasPokemones)
    for posicion,pokemon in enumerate(listasPokemones, start=1):
        print(f'{posicion}.- Nombre pokemon: {pokemon[0]}') 
        print('     Habilidades:   ',' :: '.join(pokemon[1]))
        print(f'     URL Imagen:     {pokemon[2]}')
        time.sleep(0.2)

# Con la URL obtengo su habilidad e imagen_url
def obtenerPokemonesXNombreHabilidadImagen(listaPokemones):
    print(".")
    listaIdPokemones=[obtenerIdPokemon(pokemon[1]) for pokemon in listaPokemones]
    print(".")
    listaHabilidades=[obtenerHabilidadesXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    print(".")
    listaImagenes=[obtenerImagenXPokemon(idPokemon) for idPokemon in listaIdPokemones]
    listaNombreHabilidadImagen = [[listaPokemones[posicion][0],listaHabilidades[posicion],listaImagenes[posicion]] for posicion in range(len(listaPokemones))]
    return listaNombreHabilidadImagen

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
    imagenPokemon=detailPokemon['sprites']['other']['official-artwork']['front_default']
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

def listarPokemonesXFormas(forma, listaFormas):
    #listaFormas = obtenerFormas()
    i=0
    posicion=0
    seEncontroForma = False
    for formas in listaFormas:
        if forma==formas[0]:
            posicion=i
            seEncontroForma = True
            break
        i+=1

    if(seEncontroForma):
        listPokemonesXForma=obtenerPokemonesXForma(listaFormas[posicion][1])
        listaNombreHabilidadImagen = obtenerPokemonesXNombreHabilidadImagen(listPokemonesXForma)
        imprimirListas(listaNombreHabilidadImagen)
    else:
        print(f'No se encontro la forma: {forma}, solicitada')

def obtenerFormas():
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    detailPokemon = result.json()
    listaFormas=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    listFormas = list(zip(listaFormas, listaURL))
    return listFormas

def obtenerPokemonesXForma(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    listaPokemonesURL=[pokemon['url'] for pokemon in detailPokemon['pokemon_species']]
    listPokemon = list(zip(listaPokemones, listaPokemonesURL))
    return listPokemon



# Opcion 3

def listarPokemonesXHabilidad(habilidad, listaHabilidades):
    #listaHabilidades = obtenerHabilidades()
    i=0
    posicion=0
    seEncontroHabilidad = False
    for habil in listaHabilidades:
        if habilidad==habil[0]:
            posicion=i
            seEncontroHabilidad = True
            break
        i+=1
    
    if(seEncontroHabilidad):
        listaPokemonesXHabilidad=obtenerPokemonesXHabilidad(listaHabilidades[posicion][1])
        listaNombreHabilidadImagen = obtenerPokemonesXNombreHabilidadImagen(listaPokemonesXHabilidad)
        imprimirListas(listaNombreHabilidadImagen)
    else:
        print(f'No se encontro la habilidad: {habilidad}, solicitada')

def obtenerHabilidades():
    result = requests.get(f'https://pokeapi.co/api/v2/ability/')
    detailPokemon = result.json()
    listaHabilidades=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    listHabilidades = list(zip(listaHabilidades, listaURL))
    return listHabilidades

def obtenerPokemonesXHabilidad(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['pokemon']['name'] for pokemon in detailPokemon['pokemon']]
    listaPokemonesURL=[pokemon['pokemon']['url'] for pokemon in detailPokemon['pokemon']]
    listPokemon = list(zip(listaPokemones, listaPokemonesURL))
    return listPokemon



# Opcion 4: listar por habitad

def listarPokemonesXHabitad(habitad, listaHabitads):
    #listaHabitads = obtenerHabitad()
    i=0
    posicion=0
    seEncontroHabitad = False
    for habit in listaHabitads:
        if habitad==habit[0]:
            posicion=i
            seEncontroHabitad = True
            break
        i+=1
    
    if(seEncontroHabitad):
        listaPokemonesXHabitad=obtenerPokemonesXHabitad(listaHabitads[posicion][1])
        listaNombreHabilidadImagen = obtenerPokemonesXNombreHabilidadImagen(listaPokemonesXHabitad)
        imprimirListas(listaNombreHabilidadImagen)
    else:
        print(f'No se encontro el habitad: {habitad}, solicitada')

def obtenerHabitad():
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat/')
    detailPokemon = result.json()
    listaHabitads=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    listHabilidades = list(zip(listaHabitads, listaURL))
    return listHabilidades

def obtenerPokemonesXHabitad(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['name'] for pokemon in detailPokemon['pokemon_species']]
    listaPokemonesURL=[pokemon['url'] for pokemon in detailPokemon['pokemon_species']]
    listPokemon = list(zip(listaPokemones, listaPokemonesURL))
    return listPokemon

# Opcion 5

def listarPokemonesXTipo(tipo, listaTipos):
    #listaTipos = obtenerTipos()
    i=0
    posicion=0
    seEncontroTipo = False
    for tipos in listaTipos:
        if tipo==tipos[0]:
            posicion=i
            seEncontroTipo = True
            break
        i+=1
    if(seEncontroTipo):
        listaPokemonesXTipo=obtenerPokemonesXTipo(listaTipos[posicion][1])
        listaNombreHabilidadImagen = obtenerPokemonesXNombreHabilidadImagen(listaPokemonesXTipo)
        imprimirListas(listaNombreHabilidadImagen)
    else:
        print(f'No se encontro el tipo: {tipo}, solicitada')

def obtenerTipos():
    result = requests.get(f'https://pokeapi.co/api/v2/type/')
    detailPokemon = result.json()
    listaTipos=[pokemon['name'] for pokemon in detailPokemon['results']]
    listaURL=[pokemon['url'] for pokemon in detailPokemon['results']]
    listTipos = list(zip(listaTipos, listaURL))
    return listTipos

def obtenerPokemonesXTipo(url):
    listaPokemones = []
    result = requests.get(f'{url}')
    detailPokemon = result.json()
    listaPokemones=[pokemon['pokemon']['name'] for pokemon in detailPokemon['pokemon']]
    listaPokemonesURL=[pokemon['pokemon']['url'] for pokemon in detailPokemon['pokemon']]
    listPokemon = list(zip(listaPokemones, listaPokemonesURL))
    return listPokemon
