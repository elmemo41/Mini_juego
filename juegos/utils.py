import os
import pickle

HISTORIAL_PATH = "historial.pkl"
MODEL_PATH = "modelo.pkl"

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
        with open(MODEL_PATH, "rb") as f:  
            return pickle.load(f)
    return None  