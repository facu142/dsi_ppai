from typing import List
from Preguntas import *
from datetime import datetime
from Entity import Encuesta
from Clientes import *
encuesta1 = Encuesta(cliente1,'descripcion1', datetime(2024,8,23,12,0,0), [pregunta1,pregunta2])
encuesta2 = Encuesta(cliente2,'descripcion2', datetime(2024,8,23,12,0,0), [pregunta3,pregunta4])
encuesta3 = Encuesta(cliente1,'descripcion3', datetime(2024,8,23,12,0,0), [pregunta5,pregunta6])
encuesta4 = Encuesta(cliente5,'descripcion4', datetime(2024,8,23,12,0,0), [pregunta7,pregunta8])
encuesta5 = Encuesta(cliente3,'descripcion5', datetime(2024,8,23,12,0,0), [pregunta9,pregunta10])
encuesta6 = Encuesta(cliente1,'descripcion6', datetime(2024,8,23,12,0,0), [pregunta1,pregunta4])
encuesta7 = Encuesta(cliente3,'descripcion7', datetime(2024,8,23,12,0,0), [pregunta1,pregunta6])
encuesta8 = Encuesta(cliente1,'descripcion8', datetime(2024,8,23,12,0,0), [pregunta5,pregunta8])
encuesta9 = Encuesta(cliente1,'descripcion9', datetime(2024,8,23,12,0,0), [pregunta7,pregunta9])
encuesta10 = Encuesta(cliente1,'descripcion10', datetime(2024,8,23,12,0,0), [pregunta9,pregunta4])


def creador(coleccion):
    return coleccion

def main():
   pass

if __name__ == '__main__':
    main()