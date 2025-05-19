from sklearn.naive_bayes import MultinomialNB
import numpy as np 
from utils import guardar_modelo,cargar_modelo

class PiedraPapelTijerasAi:
    def __init__(self):
        modelo_guardado = cargar_modelo()
        if modelo_guardado:
        self.modelo = MultinomialNB()
        self.entrenando = True
        else:
        self.modelo = MultinomialNB()
        self.entrenado = False
    def entrenar(self, jugadas_usuario):
        if len(jugadas_usuario) < 3:
            return
        x, y = [],[]
        for i in range(len(jugadas_usuario)-2):
            x.append(jugadas_usuario[i:i+2])
            y.append(jugadas_usuario[i+2])
        self.modelo.fit(x,y)
        self.entrenado = True
        guardar_modelo(self.modelo)
        
    def predecir(self, jugadas_usuario):
        if not self.entrenado or len(jugadas_usuario)<2:
            return np.random.choice([0,1,2])
        entrada = {jugadas_usuario[-2]}
