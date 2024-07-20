import os
import iu.menu as mn
import modulos.peliculas as b

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla según el sistema operativo
        mn.menu_principal()  # Mostrar el menú principal
        
        try:
            op = int(input('Ingrese su opción: '))
        except ValueError:
            print('Error en el dato ingresado. Por favor, ingrese un número.')
            input('Presione Enter para continuar...')
            continue
        
        if op == 1:
            mn.menu_generos()
        elif op == 2:
            mn.menu_actores()
        elif op == 3:
            mn.menu_formatos()
        elif op == 4:
            mn.menu_informes()
        elif op == 5:
            mn.menu_peliculas()
        elif op == 6:
            print('Adiós, gracias por visitarnos!!')
            break
        else:
            print('Opción no válida. Por favor, ingrese una opción del 1 al 6.')
        
        input('Presione Enter para continuar...')

if __name__ == '__main__':
    main()