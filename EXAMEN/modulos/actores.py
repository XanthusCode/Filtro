import os
import funciones.corefile as cf
import json

def gestor_actores():
    os.system('cls')
    
    
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
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd,rut,indent=4)

def listar():
    pass
    