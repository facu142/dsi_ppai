from typing import List
from RespuestasPosibles import *
from Entity import Pregunta

# Encuesta 1 
pregunta1 = Pregunta('En una escala del 1 al 10, ¿qué tan satisfecho estás con nuestros productos/servicios?', [respuestaP1,respuestaP2,respuestaP3, respuestaP4, respuestaP5, respuestaP6, respuestaP7, respuestaP8, respuestaP9, respuestaP10])
pregunta2 = Pregunta('¿En una escala del 1 al 10, ¿qué tan probable es que vuelvas a utilizar nuestros productos/servicios en el futuro?', [respuestaP1,respuestaP2,respuestaP3, respuestaP4, respuestaP5, respuestaP6, respuestaP7, respuestaP8, respuestaP9, respuestaP10])
# Encuesta 4 USADA
pregunta7 = Pregunta('¿En una escala del 1 al 10, ¿qué tan rápido fue el tiempo de respuesta de nuestro equipo de atención al cliente?', [respuestaP1,respuestaP2,respuestaP3, respuestaP4, respuestaP5, respuestaP6, respuestaP7, respuestaP8, respuestaP9, respuestaP10])

# Encuesta 2 
pregunta3 = Pregunta('¿Recibiste la asistencia necesaria durante todo el proceso de compra o utilización de nuestros productos/servicios? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
pregunta4 = Pregunta('¿La calidad de nuestros productos/servicios cumplió con tus expectativas? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
# Encuesta 3 USADA
pregunta5 = Pregunta('¿El proceso de compra/facturación fue claro y sin complicaciones? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
pregunta6 = Pregunta('¿El personal de atención al cliente fue capaz de resolver tus dudas o inquietudes? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
pregunta8 = Pregunta('¿La solución proporcionada a tu consulta/problema fue satisfactoria? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
pregunta9 = Pregunta('¿La atención al cliente que recibiste fue amable y cordial? (1: Sí, 2: No)', [respuestaPA,respuestaPB])
pregunta10 = Pregunta('¿Recomendarías nuestros productos/servicios a otros? (1: Sí, 2: No)', [respuestaPA,respuestaPB])


def main():
    '''for i in range(len(Pregunta.preguntas)):
        print("pregunta", i)
        print(Pregunta.preguntas[i].pregunta)'''

if __name__ == '__main__':
    main()