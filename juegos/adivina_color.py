import random

def jugar():
    colores = ["rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosado"]
    color_secreto = random.choice(colores)
    intentos = 3

    print("""# ------------------------------------
# |         ADIVINA EL COLOR         |
# |   Tienes 3 intentos disponibles  |
# ------------------------------------""")

    while intentos > 0:
        intento = input("# Ingresa un color: ").lower()

        if intento == color_secreto:
            print(f"""# ------------------------------------
# |     ¡CORRECTO! El color era {color_secreto.upper():^10}   |
# ------------------------------------""")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"# Incorrecto. Te quedan {intentos} intento(s).")
            else:
                print(f"""# ------------------------------------
# |     ¡HAS PERDIDO!                |
# |     El color era {color_secreto.upper():^10}     |
# ------------------------------------""")

    input("Presiona cualquier tecla para volver al menú...")
