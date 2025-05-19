from collections import Counter
import matplotlib.pyplot as pit 

def mostrar_estadisticas(historial):
    jugadas = historial["jugadas_usuario"]
    ia_jugadas = historial["jugadas_ia"]

resultados = {"ganadas":0,"perdidas":0,"empatadas":0}

for i, ia in zip(jugadas,ia_jugadas):
    if i == ia:
        resultados["empatadas"] += 1
    elif (j - ia) %3 ==1:
        resultados["ganadas"] += 1
    else: 
        resultados["perdidas"]+=1
total = len(jugadas)
print(f"\nEstadisticas finales:")                
print(f"-partidas jugadas {total}")
print(f"-ganadas:{resultados['ganadas']}")
print(f"-perdidas:{resultados['perdidas']}")
print(f"-Empatadas:{resultados['empatadas']}")
plt.bar(resultados.keys(),resultados.values())
Plt.title()

