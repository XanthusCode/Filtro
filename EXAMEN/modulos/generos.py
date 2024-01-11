import os
import json
import funciones.corefile as cf

def crearGenero():
    genre = {
    'id' : '',
    'nombre_G': '',
    }
    id = input('ingrese la id de la pelicula: ')
    nombre_G = input('ingrese el genero de la pelicula: ')
    genre['id'] = id
    genre['nombre_G'] = nombre_G

    bd = {
        'blockbuster': {
            'peliculas':{
                'id_p': '',
                'nombre': '',
                'duracion': '',
                'sipnosis': '',
                'generos': {}
            },
            'actores':{
                'id_p': '',
                'nombre' : '',
                'rol':''
            },
            'formato':{
                'id_p': '',
                'nombre': '',
                'nroCopias': '',
                'valorPrestamo': ''
            }
        }
    }
    genre.append(bd.get['generos'])
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd,rut,indent=4)