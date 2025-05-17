import random
from utils import obtener_opcion, cls


def lanzamiento():
    return random.randint(1, 6)


def juego_dados():

    while True:
        input("presiona enter para lanzar los dados")

        if lanzamiento() == 6:
            print("""-------
|*   *|
|*   *|
|*   *|
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)

            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")
            break

        elif lanzamiento() == 5:
            print("""-------
|*   *|
|  *  |
|*   *|
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)
            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")
                break
        elif lanzamiento() == 4:
            print("""-------
|*   *|
|     |
|*   *|
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)
            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")
                break
        elif lanzamiento() == 3:
            print("""-------
| *   |
|  *  |
|   * |
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)
            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")
                break
        elif lanzamiento() == 2:
            print("""-------
| *   |
|     |
|   * |
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)
            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")
                break
        elif lanzamiento() == 1:
            print("""-------
|     |
|  *  |
|     |
-------""")
            print("Quiere lanzar el dado otra vez \n 1)si 2)no")
            opcion = obtener_opcion(2)
            if opcion == 1:
                juego_dados()
            else:
                print("Hasta luego")

            break

        else:
            print("Pongalo bien1")


juego_dados()
