import os
import funciones.corefile as cf
import json
cf.RUTA = 'data/blockbuster.json'
pelicula = {
}
def add_movie():
    id_p = input('ingrese la id de la pelicula: ')
    nombre = input('ingrese el nombre de la pelicula: ')
    duracion = input('ingrese la duracion la pelicula: ')
    sipnosis = input('Ingrese la sipnosis de la pelicula: ')
    os.system('pause & cls')
    genre = {
    'id' : '',
    'nombre_G': '',
    }
    id = input('ingrese la id de la pelicula: ')
    nombre_G = input('ingrese el genero de la pelicula: ')
    genre['id'] = id
    genre['nombre_G'] = nombre_G
    os.system('pause & cls')

    print('Ingreso del actor')
    id_a = (input('ingrese la id de la pelicula: '))
    n = input('ingrese el nombre de la pelicula: ')
    rol = input('ingres el rol del actor en la pelicula')
    os.system('pause & cls')

    print('Ingreso del formato')
    id_f = input('ingrese la id de la pelicula: ')
    name = input('ingrese el formato de la pelicula: ')
    nroCopias = input('ingrese nro de copias que tiene la pelicula: ')
    prestamo = input('Ingrese valor del prestamo: ')
    

    bd = {
        'blockbuster': {
            'peliculas':{
                'id_p': id_p,
                'nombre': nombre,
                'duracion': duracion,
                'sipnosis': sipnosis,
                'generos': {}
            },
            'actores':{
                'id_p': id_a,
                'nombre' : n,
                'rol': rol
            },
            'formato':{
                'id_p': id_f,
                'nombre': name,
                'nroCopias': nroCopias,
                'valorPrestamo': prestamo
            }
        }
    }
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd,rut,indent=4)


def search():
    data = cf.open_file()
    name = input('ingrese nombre la pelicula a buscar: ')
    if pelicula.get('nombre') == name:
        print(pelicula['blockbuster']['peliculas'])
    else:
        print('No se encontro ese id')

def delete():
    data = cf.open_file()
    name = input('ingrese nombre la pelicula a eliminar: ')
    for i,c in enumerate(data):
        if pelicula.get('nombre') == name:
            index_to_remove = i
            cf.eliminar(data,index_to_remove = index_to_remove)
            cf.save_file(data)

def modify():
    found_movie = None
    data = cf.open_file()
    name = input('ingrese nombre la pelicula a modificar: ')
    for c in data:
        if pelicula.get('nombre') == name:
            found_movie = c
        else:
            print('no existe')

    if found_movie is not None:
        for key, value in found_movie.items():
            user_input = input(f'Desea editar el campo {key} enter Si otra cosa no')

            if user_input != '':
                new_value =  input(f'Desea editar el campo {key.capitalize()} enter Si otra cosa no')
                found_movie[key] = new_value
        print('actualizado') 

    for i, camper in enumerate(data):
         if pelicula.get('id') == id:
            data[i] = found_movie
            break
    cf.save_file(pelicula)

    
