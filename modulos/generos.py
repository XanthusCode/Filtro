import os
import json
import funciones.corefile as cf


def crearGenero():
    id = input('Ingrese el ID del género: ')
    nombre_G = input('Ingrese el nombre del género: ')
    
    # Validar entradas
    if not id or not nombre_G:
        print("Todos los campos son obligatorios.")
        input('Presione Enter para continuar...')
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
        bd = {'blockbuster': {'generos': {}, 'peliculas': {}, 'actores': {}, 'formato': {}}}
    
    # Asegurar que 'generos' sea un diccionario
    if 'generos' not in bd['blockbuster']:
        bd['blockbuster']['generos'] = {}
    
    # Agregar el nuevo género a la lista de géneros
    bd['blockbuster']['generos'][id] = nuevo_genero

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)
    
    print("Género creado correctamente.")
    input('Presione Enter para continuar...')
    

def listarGeneros():
    # Verificar si el archivo existe
    if not os.path.isfile(cf.RUTA):
        print("No hay datos disponibles. El archivo no existe.")
        input('Presione Enter para continuar...')
        return
    
    # Cargar los datos del archivo
    with open(cf.RUTA, 'r') as rut:
        bd = json.load(rut)

    # Obtener los géneros
    generos = bd.get('blockbuster', {}).get('generos', {})

    # Verificar si hay géneros
    if not generos:
        print("No hay géneros registrados.")
    else:
        print("Listado de géneros:")
        for genero_id, genero in generos.items():
            print(f"ID: {genero['id']}, Nombre: {genero['nombre_G']}")

    input('Presione Enter para continuar...')