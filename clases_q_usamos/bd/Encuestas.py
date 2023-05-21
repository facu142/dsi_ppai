from typing import List
from Preguntas import *
from datetime import datetime

class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.descripcion = descripcion
        self.valor = valor

class Pregunta:
    def __init__(self, pregunta, respuesta: List[RespuestaPosible]):
        self.pregunta = pregunta
        self.respuesta = respuesta

class Encuesta: # Esta clase ni siquiera la usamos???
    encuestas=[]
    def __init__(self, descripcion, fechaFinVigencia, pregunta: List[Pregunta]):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia,
        self.pregunta = pregunta
        self.encuestas.append(self)


encuesta1 = Encuesta('descripcion1', datetime(2024,8,23,12,0,0), [pregunta1,pregunta2])
encuesta2 = Encuesta('descripcion2', datetime(2024,8,23,12,0,0), [pregunta3,pregunta4])
encuesta3 = Encuesta('descripcion3', datetime(2024,8,23,12,0,0), [pregunta5,pregunta6])
encuesta4 = Encuesta('descripcion4', datetime(2024,8,23,12,0,0), [pregunta7,pregunta8])
encuesta5 = Encuesta('descripcion5', datetime(2024,8,23,12,0,0), [pregunta9,pregunta10])
encuesta6 = Encuesta('descripcion6', datetime(2024,8,23,12,0,0), [pregunta1,pregunta4])
encuesta7 = Encuesta('descripcion7', datetime(2024,8,23,12,0,0), [pregunta3,pregunta6])
encuesta8 = Encuesta('descripcion8', datetime(2024,8,23,12,0,0), [pregunta5,pregunta8])
encuesta9 = Encuesta('descripcion9', datetime(2024,8,23,12,0,0), [pregunta7,pregunta10])
encuesta10 = Encuesta('descripcion10', datetime(2024,8,23,12,0,0), [pregunta9,pregunta4])


def creador(coleccion):
    return coleccion

def main():
    for encuesta in Encuesta.encuestas:
        print("Encuesta")
        for i in range(len(encuesta.pregunta)):
            print("Pregunta Nro",i+1)
            print(encuesta.pregunta[i].pregunta)
        print("\n")

if __name__ == '__main__':
    main()