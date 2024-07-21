import os
import funciones.corefile as cf
import json
pelicula ={}

cf.RUTA = 'data/blockbuster.json'
def add_movie():
    id_p = input('Ingrese la ID de la película: ')
    nombre = input('Ingrese el nombre de la película: ')
    duracion = input('Ingrese la duración de la película: ')
    sipnosis = input('Ingrese la sinopsis de la película: ')
    os.system('pause & cls')

    genre_id = input('Ingrese la ID del género: ')
    genre_nombre = input('Ingrese el nombre del género: ')
    genre = {
        'id': genre_id,
        'nombre_G': genre_nombre,
    }
    os.system('pause & cls')

    print('Ingreso del actor')
    id_a = input('Ingrese la ID del actor: ')
    actor_nombre = input('Ingrese el nombre del actor: ')
    rol = input('Ingrese el rol del actor en la película: ')
    os.system('pause & cls')

    print('Ingreso del formato')
    id_f = input('Ingrese la ID del formato: ')
    formato_nombre = input('Ingrese el nombre del formato: ')
    nroCopias = input('Ingrese el número de copias que tiene la película: ')
    prestamo = input('Ingrese el valor del préstamo: ')
    
    # Cargar datos existentes
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
    else:
        bd = {'blockbuster': {'peliculas': {}, 'actores': {}, 'formato': {}}}

    # Agregar la nueva película
    bd['blockbuster']['peliculas'][id_p] = {
        'nombre': nombre,
        'duracion': duracion,
        'sipnosis': sipnosis,
        'generos': {genre_id: genre},
        'actores': {id_a: {'nombre': actor_nombre, 'rol': rol}},
        'formatos': {id_f: {'nombre': formato_nombre, 'nroCopias': nroCopias, 'valorPrestamo': prestamo}}
    }

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)

    print('Película añadida correctamente.')
    input('Presione Enter para continuar...')

def search():
    data = cf.open_file()
    name = input('Ingrese el nombre de la película a buscar: ')
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    for pelicula in peliculas.values():
        if pelicula.get('nombre') == name:
            print(json.dumps(pelicula, indent=4))
            return
    print('No se encontró esa película.')

    input('Presione Enter para continuar...')

def delete():
    data = cf.open_file()
    id_p = input('Ingrese la ID de la película a eliminar: ')
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    if id_p in peliculas:
        del peliculas[id_p]
        cf.save_file(data)
        print('Película eliminada correctamente.')
    else:
        print('No se encontró esa película.')

    input('Presione Enter para continuar...')


def modify():
    data = cf.open_file()
    id_p = input('Ingrese la ID de la película a modificar: ')
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    found_movie = peliculas.get(id_p)

    if not found_movie:
        print('No existe esa película.')
        return

    print('Película encontrada. Puede editar los siguientes campos:')
    for key, value in found_movie.items():
        if isinstance(value, dict):
            print(f'{key}:')
            for sub_key, sub_value in value.items():
                user_input = input(f'Desea editar el campo {sub_key}? (Ingrese "si" para editar, "no" para omitir): ')
                if user_input.lower() == 'si':
                    new_value = input(f'Ingrese el nuevo valor para {sub_key.capitalize()}: ')
                    found_movie[key][sub_key] = new_value
        else:
            user_input = input(f'Desea editar el campo {key}? (Ingrese "si" para editar, "no" para omitir): ')
            if user_input.lower() == 'si':
                new_value = input(f'Ingrese el nuevo valor para {key.capitalize()}: ')
                found_movie[key] = new_value

    # Guardar los datos actualizados en el archivo
    cf.save_file(data)
    print('Película actualizada correctamente.')
    input('Presione Enter para continuar...')


def list_all_movies():
    data = cf.open_file()
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    if not peliculas:
        print('No hay películas registradas.')
    else:
        print('Listado de películas:')
        for id_p, pelicula in peliculas.items():
            print(f"ID: {id_p}")
            for key, value in pelicula.items():
                if isinstance(value, dict):
                    print(f'{key}:')
                    for sub_key, sub_value in value.items():
                        print(f'  {sub_key}: {sub_value}')
                else:
                    print(f'{key}: {value}')
            print('-' * 30)

    input('Presione Enter para continuar...')


def buscar_pelicula_y_mostrar():
    data = cf.open_file()
    nombre = input('Ingrese el nombre de la película a buscar: ')
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    for pelicula in peliculas.values():
        if pelicula.get('nombre') == nombre:
            print(f"Sinopsis: {pelicula.get('sipnosis')}")
            print("Actores:")
            actores = pelicula.get('actores', {})
            for actor in actores.values():
                print(f"Nombre: {actor.get('nombre')}, Rol: {actor.get('rol')}")
            return
    print('No se encontró esa película.')
