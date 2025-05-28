from ai import PiedraPapelTijeraAi
from utils import cargar_historial,guardar_historial
from stats import mostrar_estadisticas

opciones = ["Piedra","Papel","Tijera"]

def jugar():
    print("Quieres reiniciar el historial?(s/n)")
    if input().lower() == "s":
        historial = {"jugadas_usuario": [], "jugadas_ia": []}
    else:
        historial = cargar_historial()
    ai = PiedraPapelTijeraAi()
    ai.entrenar(historial["jugadas_usuario"])

    while True:
        print("Elije: 0-Piedra|1-Papel|2-tijeras|9-salir")
        try:
            jugador = int(input("Tu jugada: "))
            if jugador == 9:
                break
            if jugador not in[0,1,2]:
                print("Jugada invalida")
                continue
        except ValueError:
            print("entrada invalida")
            continue
        ia =ai.predecir(historial["jugadas_usuario"])
        print(f"IA juega:{opciones[ia]}")

        if jugador == ia:
            print("Empate.")
        elif(jugador - ia) %3 == 1:
            print("Ganaste")
        else:
            print("Perdiste. ")

        historial["jugadas_usuario"].append(jugador)
        historial["jugadas_ia"].append(ia)
        ia.entrenar(historial["jugadas_usuario"])
        guardar_historial(historial)
        mostrar_estadisticas(historial)

if __name__ == "__main__":
    jugar()
