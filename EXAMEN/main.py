import os
import iu.menu as mn
import modulos.peliculas as b

while True:
    os.system('cls')
    menu = mn.menu_principal() 
    try:
        op = int(input(':)'))
    except ValueError:
        print('Error en el dato ingresado')
    else:
        if(op == 1):
            mn.menu_generos()
        elif(op == 2):
            mn.menu_actores()
        elif(op == 3):
            mn.menu_formatos()
        elif(op == 4):
            mn.menu_informes
        elif(op == 5):
            mn.menu_peliculas()
        elif(op == 6):
            print('Adios, gracias por visitarnos!!')
            break