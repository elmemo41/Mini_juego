import random
from utils import obtener_opcion, cls


def lanzamiento():
    return random.randint(1, 6)


def mostrar_dado(valor):

    caras = {
        6: """-------
|*   *|
|*   *|
|*   *|
-------""",

        5: """-------
|*   *|
|  *  |
|*   *|
-------""",

        4: """-------
|*   *|
|     |
|*   *|
-------""",

        3: """-------
| *   |
|  *  |
|   * |
-------""",

        2: """-------
| *   |
|     |
|   * |
-------""",

        1: """-------
|     |
|  *  |
|     |
-------"""
    }
    print(caras[valor])


def juego_de_dados():

    while True:
        cls()
        input("Presione enter para lanzar el dado")
        valor = lanzamiento()
        mostrar_dado(valor)

        print("Quiere lanzarlo otra vez? \n 1)si 2)no")

        opcion = obtener_opcion(2)

        if opcion == 1:
            juego_de_dados()

        elif opcion == 2:
            print("Hasta luego")
        break


juego_de_dados()
