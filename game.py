from ai import PiedraPapelTijerasAi
from utils import cargar_historial,guardar_historial 
from stats import mostrar_estadisticas

opciones= ["piedra","papel","tijera"]

def jugar():
    print("quieres reiniciar el historial?s/n")
    if input().lower()=="s":
        historial = {"jugadas_usuario":[],"jugadas ia":[]}
    else:
        historial = cargar_historial() undefined variable 'cargar_historial'
    ia = PiedraPapelTijerasAi()
    ia.entrenar(historial["jugadas_usuario"]) no value for argument 'jugadas_usuario' in unbound method call 
    
    while True:
        print("Elije: 0-piedra|1-papel|2-tijeras|9-salir")
        try:
            jugador = int(input("tu jugada:"))
            if jugador == 9:
                break
            if jugador not in[0,1,2]:
                print("jugada invalida")
                continue
        except ValueError:
            print("Entrada Invalida")
            continue
        ia = ai.predecir(historial["jugadas_usuario"])
        print(f"IA juega:{opciones[ia]}")

        if jugador == ia:
            print("Empate.")
        elif(jugador- ia) %3 ==1:
            print("ganaste")
        else:
            print("perdiste.")
        historial["jugadas_usuario"].append(jugador)
        historial["jugadas_ia"].append(ia)
        ai.entrenar(historial["jugadas_usuario"])
        guardar_historial(historial)
        mostrar_estadisticas(historial)

        
