from juegos import adivina_color


def menu_principal():
    while True:
        print("""# ------------------------------------
# |                                  |
# |         MENÚ PRINCIPAL           |
# |                                  |
# ------------------------------------
# 1) Adivina el número
# 2) Adivina el color
# 3) Juego de dados
# 4) Piedra, papel o tijeras
# 5) Salir
# ------------------------------------""")
        opcion = input("# SELECCIONA UNA OPCIÓN (1-5): ")

        if opcion == "1":
            print("# Esta opción aún no está disponible.")
            input("Presiona cualquier tecla para continuar...")

        elif opcion == "2":
            print("""# ------------------------------------
# |      INICIANDO: ADIVINA COLOR    |
# ------------------------------------""")
            adivina_color.jugar()

        elif opcion == "3":
            print("# Esta opción aún no está disponible.")
            input("Presiona cualquier tecla para continuar...")

        elif opcion == "4":
            print("# Esta opción aún no está disponible.")
            input("Presiona cualquier tecla para continuar...")

        elif opcion == "5":
            print("""# ------------------------------------
# |         ¡HASTA LUEGO!            |
# ------------------------------------""")
            break
        else:
            print("# Opción no válida. Intenta de nuevo.")

menu_principal()
