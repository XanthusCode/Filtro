import funciones.corefile as cf
import modulos.generos as g
import modulos.actores as a
import modulos.formatos as f
import modulos.peliculas as p
import modulos.reportes as r
import os

opciones = ['Administrador de generos','Administrador de actores','Adminstrador de formatos','Gestor de informes','Gestor de peliculas','Salir']
opGeneros = ['crear genero','Listar generos','Menu principal']
opActores = ['crear actor','Listar actores','Menu principal']
opFormatos = ['crear Formatos','Listar Formatos','Menu principal']
opPeliculas = ['Agregar pelicula','Editar pelicula','Eliminar pelicula','Eliminar Actor','Buscar pelicula','Listar todas las peliculas','Menu principal']
opInformes = ['Listar informe de un genero especifico', 'listar peliculas donde el protagonista es Silvestre stallone', 'Busacr pelicula y mostrar la sipnosis y actores', 'menu principal']


def menu_principal():
    p.cf.check_file(p.pelicula)
    os.system('cls')
    header = """
    *******************************************
    * SISTEMA GESTOR DE PELICULAS BLOCKBUSTER *
    *******************************************
    """
    print(header)
    for i,item in enumerate(opciones):
            print(f'{(i + 1)} - {item}')

def menu_generos():
    
    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE GÉNEROS *
    ***********************
    """
    while isActiveP:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(tittle)
        for i, item in enumerate(opGeneros):
            print(f'{(i + 1)} - {item}')
        try:
            op = int(input(':) '))
        except ValueError:
            print('Error en el dato ingresado. Por favor, ingrese un número.')
            input('Presione Enter para continuar...')
            continue
        else:
            if op == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                tittle = """
                ***********************
                * CREACIÓN DE GÉNEROS *
                ***********************
                """
                print(tittle)
                g.crearGenero()
            elif op == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                tittle = """
                **********************
                * LISTADO DE GÉNEROS *
                **********************
                """
                print(tittle)
                g.listarGeneros()
            elif op == 3:
                isActiveP = False
            else:
                print('Opción no válida. Por favor, ingrese una opción del 1 al 3.')
                input('Presione Enter para continuar...')
def menu_actores():
    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE ACTORES *
    ***********************
    """
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opActores):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                a.gestor_actores()
            elif(op == 2):
                a.listar()
            elif(op == 3):
                isActiveP = False

def menu_formatos():
    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE FORMATOS *
    ***********************
    """
    while isActiveP:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(tittle)
        for i, item in enumerate(opFormatos):
            print(f'{(i + 1)} - {item}')
        try:
            op = int(input(':) '))
        except ValueError:
            print('Error en el dato ingresado')
        else:
            if op == 1:
                tittle = """
                ***********************
                * CREACION DE FORMATOS *
                ***********************
                """
                print(tittle)
                f.crearFormato()
            elif op == 2:
                tittle = """
                ***********************
                * LISTADO DE FORMATOS *
                ***********************
                """
                print(tittle)
                f.listarFormatos()
            elif op == 3:
                isActiveP = False

def menu_peliculas():
    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE PELICULAS *
    ***********************
    """
    while isActiveP:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(tittle)
        for i, item in enumerate(opPeliculas):
            print(f'{(i + 1)} - {item}')
        try:
            op = int(input(':) '))
        except ValueError:
            print('Error en el dato ingresado')
        else:
            if op == 1:
                p.add_movie()
            elif op == 2:
                p.modify()
            elif op == 3:
                p.delete()
            elif op == 4:
                p.delete_actor()
            elif op == 5:
                p.search()
            elif op == 6:
                p.list_all_movies()
            elif op == 7:
                isActiveP = False
def menu_informes():
    """Mostrar menú de informes y manejar la interacción del usuario."""
    isActiveP = True
    title = """
    ***********************
    * GESTOR DE INFORMES *
    ***********************
    """
    while isActiveP:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title)
        for i, item in enumerate(opInformes):
            print(f'{(i + 1)} - {item}')
        
        try:
            op = int(input('Ingrese su opción: '))
        except ValueError:
            print('Error en el dato ingresado. Por favor, ingrese un número.')
            input('Presione Enter para continuar...')
        else:
            if op == 1:
                r.listar_informe_genero()
            elif op == 2:
                # Aquí necesitas especificar el nombre del protagonista o manejarlo de alguna manera
                protagonista = input('Ingrese el nombre del protagonista: ')
                r.listar_peliculas_protagonista(protagonista)
            elif op == 3:
                r.buscar_pelicula_y_mostrar()
            elif op == 4:
                isActiveP = False
            else:
                print('Opción no válida. Por favor, ingrese una opción del 1 al 4.')
            input('Presione Enter para continuar...')