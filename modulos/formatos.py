import os
import json
import funciones.corefile as cf

def formato():
    id_p = input('Ingrese el ID de la película: ')
    nombre = input('Ingrese el nombre del formato: ')
    nroCopias = input('Ingrese el número de copias que tiene el formato: ')
    valorPrestamo = input('Ingrese el valor del préstamo: ')
    
    # Validar las entradas (puedes mejorar las validaciones según tus necesidades)
    if not id_p or not nombre or not nroCopias or not valorPrestamo:
        print("Todos los campos son obligatorios.")
        return

    # Cargar datos existentes
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
    else:
        bd = {'blockbuster': {'peliculas': {}, 'actores': {}, 'formato': {}}}
    
    # Actualizar el formato en el diccionario
    bd['blockbuster']['formato'] = {
        'id_p': id_p,
        'nombre': nombre,
        'nroCopias': nroCopias,
        'valorPrestamo': valorPrestamo
    }

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)
    
    print("Formato actualizado correctamente.")