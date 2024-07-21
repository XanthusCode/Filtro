import os
import funciones.corefile as cf
import json



def gestor_actores():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Ingreso de un nuevo actor")
    id_a = input('Ingrese la ID del actor: ')
    nombre_a = input('Ingrese el nombre del actor: ')
    rol_a = input('Ingrese el rol del actor: ')

    # Crear el nuevo actor
    nuevo_actor = {
        'id': id_a,
        'nombre': nombre_a,
        'rol': rol_a
    }

    # Cargar datos existentes
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
    else:
        bd = {'blockbuster': {'peliculas': {}, 'actores': {}, 'formato': {}}}
    
    # Asegurar que 'actores' sea un diccionario
    if 'actores' not in bd['blockbuster']:
        bd['blockbuster']['actores'] = {}
    
    # Agregar el nuevo actor a la lista de actores
    bd['blockbuster']['actores'][id_a] = nuevo_actor

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)
    
    print("Actor creado correctamente.")
    input('Presione Enter para continuar...')
    

def listar():
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
            actores = bd.get('blockbuster', {}).get('actores', {})
            
            if not actores:
                print("No hay actores registrados.")
            else:
                print("Listado de actores:")
                for actor_id, actor in actores.items():
                    print(f"ID: {actor['id']}, Nombre: {actor['nombre']}, Rol: {actor['rol']}")
    else:
        print("El archivo no existe.")
    
    input('Presione Enter para continuar...')