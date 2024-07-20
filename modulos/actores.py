import os
import funciones.corefile as cf
import json


def gestor_actores():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    bd = {
        'blockbuster': {
            'peliculas': {
                'id_p': '',
                'nombre': '',
                'duracion': '',
                'sipnosis': '',
                'generos': {}
            },
            'actores': {
                'id_p': '',
                'nombre': '',
                'rol': ''
            },
            'formato': {
                'id_p': '',
                'nombre': '',
                'nroCopias': '',
                'valorPrestamo': ''
            }
        }
    }
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)

def listar():
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
            print(json.dumps(bd, indent=4))
    else:
        print("El archivo no existe.")
    