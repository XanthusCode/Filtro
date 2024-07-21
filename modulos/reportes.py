import funciones.corefile as cf
import json


import json
import funciones.corefile as cf


def listar_informe_genero():
    """Listar el género de las películas según el ID del género especificado."""
    data = cf.open_file()
    genero_id = input('Ingrese el ID del género a buscar: ')
    
    # Aquí 'peliculas' está directamente en 'blockbuster'
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    genero_encontrado = False
    
    for pelicula_id, pelicula in peliculas.items():
        # Verifica si 'pelicula' es un diccionario
        if isinstance(pelicula, dict):
            generos = pelicula.get('generos', {})
            if genero_id in generos:
                print(f"Película ID: {pelicula_id} tiene el género ID: {genero_id}")
                genero_encontrado = True
    
    if not genero_encontrado:
        print('No se encontraron películas para el género especificado.')

def listar_peliculas_protagonista(protagonista):
    """Listar películas donde el protagonista es el indicado."""
    data = cf.open_file()
    peliculas = data.get('blockbuster', {}).get('peliculas', {})
    
    peliculas_protagonista = {
        'protagonista': protagonista,
        'peliculas': []
    }
    
    for pelicula_id, pelicula in peliculas.items():
        # Asegúrate de que 'pelicula' sea un diccionario
        if isinstance(pelicula, dict):
            if pelicula.get('protagonista') == protagonista:
                peliculas_protagonista['peliculas'].append(pelicula)
        else:
            print(f"Advertencia: 'pelicula' con ID '{pelicula_id}' no es un diccionario.")
    
    if peliculas_protagonista['peliculas']:
        print(json.dumps(peliculas_protagonista, indent=4))
    else:
        print('No se encontraron películas con el protagonista especificado.')

def buscar_pelicula_y_mostrar():
    """Buscar película por nombre y mostrar sinopsis y actores."""
    data = cf.open_file()
    
    # Accede directamente al diccionario de atributos
    pelicula = data.get('blockbuster', {}).get('peliculas', {})
    
    # Si 'pelicula' no es un diccionario, muestra advertencia
    if not isinstance(pelicula, dict):
        print("Advertencia: 'peliculas' no es un diccionario.")
        return

    # Datos individuales de la película
    nombre = pelicula.get('nombre')
    sinopsis = pelicula.get('sipnosis')
    actores = pelicula.get('actores', {})
    
    # Busca por nombre de película (suponiendo que solo hay una película)
    nombre_buscar = input('Ingrese el nombre de la película a buscar: ')
    
    if nombre == nombre_buscar:
        print(f"Sinopsis: {sinopsis}")
        print("Actores:")
        
        if not actores:
            print("No se encontraron actores para esta película.")
        else:
            for actor_id, actor in actores.items():
                print(f"Nombre: {actor.get('nombre')}, Rol: {actor.get('rol')}")
    else:
        print('No se encontró esa película.')