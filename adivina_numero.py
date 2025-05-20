import random
numero = random.randint(1,20)
intentos = 5
intentospersona = 0 
print("bienvenidos al juego de adivina el numero tienes 5 intentos")
mi_nombre = input("como te llamas? ")
print(f"ok {mi_nombre}, estoy pensando en un numero entre el 1 al 20" )
repuesta_del_usuario = input("crees poder adivinar?" )


while intentospersona < intentos:
    num = int(input(f"intento {intentospersona + 1}\ningrese el numero"))
    intentospersona += 1
    if num == numero:
      print(f"!felicidades adivinaste el numero secreto! en {intentospersona} intentos")
      break
    elif num < numero:
      print("muy bajo intenta un numero mas alto")
    elif num > numero:
      print("muy alto intenta un numero mas bajo")
    else:
      print("game over")


















