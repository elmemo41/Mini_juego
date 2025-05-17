import pickle
import os

HISTORIAL_PATH = "historial.pkl"
MODEL_PATH = "modelo_entrenado.pkl"


def guardar_historial(historial):
    with open(HISTORIAL_PATH, "wb") as f:
        pickle.dump(historial, f)


def cargar_historial():
    if os.path.exists(HISTORIAL_PATH):
        with open(HISTORIAL_PATH, "rb") as f:
            return pickle.load(f)
    return {"jugadas_usuario": [], "jugadas_ia": []}


def guardar_modelo(modelo):
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(modelo, f)


def cargar_modelo():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb")as f:
            return pickle.load(f)
    return None


def obtener_opcion(max_opcion):
    while True:
        try:
            opcion = int(input("# ELIGE UNA OPCION:"))
            if 1 <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Por favor ingresa un numero entre 1 y {max_opcion}")
        except ValueError:
            print("Entrada no valida. Ingresa un numero.")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
