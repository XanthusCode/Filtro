import os
import json
import funciones.corefile as cf
def crearFormato():
    id_f = input('Ingrese la ID del formato: ')
    nombre_f = input('Ingrese el nombre del formato: ')
    nroCopias = input('Ingrese el número de copias que tiene el formato: ')
    valorPrestamo = input('Ingrese el valor del préstamo: ')
    
    # Validar entradas
    if not id_f or not nombre_f:
        print("Todos los campos son obligatorios.")
        return
    
    # Crear el nuevo formato
    nuevo_formato = {
        'id': id_f,
        'nombre': nombre_f,
        'nroCopias': nroCopias,
        'valorPrestamo': valorPrestamo
    }
    
    # Cargar datos existentes
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
    else:
        bd = {'blockbuster': {'peliculas': {}, 'actores': {}, 'formato': {}}}
    
    # Asegurar que 'formato' sea un diccionario
    if 'formato' not in bd['blockbuster']:
        bd['blockbuster']['formato'] = {}
    
    # Agregar el nuevo formato a la lista de formatos
    bd['blockbuster']['formato'][id_f] = nuevo_formato

    # Guardar los datos actualizados en el archivo
    with open(cf.RUTA, 'w') as rut:
        json.dump(bd, rut, indent=4)
    
    print("Formato creado correctamente.")
    input('Presione Enter para continuar...')
    
def listarFormatos():
    if os.path.isfile(cf.RUTA):
        with open(cf.RUTA, 'r') as rut:
            bd = json.load(rut)
            formatos = bd.get('blockbuster', {}).get('formato', {})
            
            if not formatos:
                print("No hay formatos registrados.")
            else:
                print("Listado de formatos:")
                for formato_id, formato in formatos.items():
                    print(f"ID: {formato['id']}, Nombre: {formato['nombre']}, Número de Copias: {formato['nroCopias']}, Valor del Préstamo: {formato['valorPrestamo']}")
    else:
        print("El archivo no existe.")
    
    input('Presione Enter para continuar...')