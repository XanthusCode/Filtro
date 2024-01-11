import funciones.corefile as cf
import modulos.generos as g
import modulos.actores as a
import modulos.formatos as f
import modulos.peliculas as p
import os

opciones = ['Administrador de generos','Administrador de actores','Adminstrador de formatos','Gestor de informes','Gestor de peliculas','Salir']
opGeneros = ['crear genero','Listar generos','Menu principal']
opActores = ['crear actor','Listar actores','Menu principal']
opFormatos = ['crear Formatos','Listar Formatos','Menu principal']
opPeliculas = ['Agregar pelicula','Editar pelicula','Eliminar pelicula','Eliminar Actor','Buscar pelicula','Listar todas las peliculas','Menu principal']
opInformes = ['Listar informe de un genero especifico', 'listar peliculas donde el rpotagonista es Silvestre stallone', 'Busacr pelicula y mostrar la sipnosis y actores', 'menu principal']


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
    * GESTOR DE GENEROS *
    ***********************
    """
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opGeneros):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                tittle = """
            ***********************
            * CREACION DE GENEROS *
            ***********************
            """
                print(tittle)
                g.crearGenero()

            elif(op == 2):
                tittle = """
                **********************
                * LISTADO DE GENEROS *
                **********************
                """
                print(tittle)
            elif(op == 3):
                isActiveP = False

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
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opFormatos):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                pass
            elif(op == 2):
                pass
            elif(op == 3):
                isActiveP = False

def menu_peliculas():

    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE PELICULAS *
    ***********************
    """
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opPeliculas):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                p.add_movie()
            elif(op == 2):
                p.modify()
            elif(op == 3):
                p.delete()
            elif(op == 4):
                pass
            elif(op == 5):
                p.search()
            elif(op == 6):
                pass
            elif(op == 7):
                isActiveP = False

def menu_informes():

    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE INFORMES *
    ***********************
    """
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opInformes):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                pass
            elif(op == 2):
                pass
            elif(op == 3):
                pass
            elif(op == 4):
                isActiveP = False