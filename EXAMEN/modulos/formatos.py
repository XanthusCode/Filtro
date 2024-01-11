import os
import json
import funciones.corefile as cf

def formato():
    id_p = input('ingrese la id de la pelicula: ')
    nombre = input('ingrese el genero de la pelicula: ')
    nroCopias = input('ingrese nro de copias que tiene la pelicula: ')
    prestamo = input('Ingrese valor del prestamo: ')
    

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
                'id_p': id_p,
                'nombre': nombre,
                'nroCopias': nroCopias,
                'valorPrestamo': prestamo
            }
        }
    }
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd,rut,indent=4)