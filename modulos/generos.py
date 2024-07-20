import os
import json
import funciones.corefile as cf

def crearGenero():
    id = input('Ingrese el ID del género: ')
    nombre_G = input('Ingrese el nombre del género: ')
    
    # Validar entradas
    if not id or not nombre_G:
        print("Todos los campos son obligatorios.")
        return
    
    # Crear el nuevo género
    nuevo_genero = {
        'id': id,
        'nombre_G': nombre_G
    }
    
    # Cargar datos existentes
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
    else:
        bd = {'blockbuster': {'peliculas': {'generos': {}}, 'actores': {}, 'formato': {}}}
    
    # Asegurar que 'generos' sea un diccionario
    if 'generos' not in bd['blockbuster']['peliculas']:
        bd['blockbuster']['peliculas']['generos'] = {}
    
    # Agregar el nuevo género a la lista de géneros
    bd['blockbuster']['peliculas']['generos'][id] = nuevo_genero

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)
    
    print("Género creado correctamente.")