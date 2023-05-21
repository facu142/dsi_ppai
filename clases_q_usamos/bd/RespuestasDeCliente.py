from RespuestasPosibles import *
from datetime import datetime, date

class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.descripcion = descripcion
        self.valor = valor

class RespuestaDeCliente:
    def __init__(self, fechaEncuesta: str, respuestaSeleccionada: RespuestaPosible): # ver formato de fecha
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada

# Respuestas de llamada 3
respuestaC3 = RespuestaDeCliente(date(2011, 8, 24), respuestaPA)
respuestaC4 = RespuestaDeCliente(date(2011, 8, 24), respuestaPA)

# Respuestas de llamada 4
respuestaC1 = RespuestaDeCliente(date(2012, 5, 9), respuestaP10)
respuestaC2 = RespuestaDeCliente(date(2012, 5, 9), respuestaPB)

# Respuestas de llamada 5
respuestaC5 = RespuestaDeCliente(date(2013, 7, 18), respuestaPB)
respuestaC6 = RespuestaDeCliente(date(2013, 7, 18), respuestaPB)

'''
respuestaC7 = RespuestaDeCliente('07/04/2023', respuestaP9)
respuestaC8 = RespuestaDeCliente('08/03/2023', respuestaP10)
respuestaC9 = RespuestaDeCliente('09/02/2023', respuestaPA)
respuestaC10 = RespuestaDeCliente('10/01/2023', respuestaPB)
'''

respuestasDeCliente = [respuestaC1,respuestaC2,respuestaC3, respuestaC4, respuestaC5, respuestaC6]

def main():
    pass

if __name__ == '__main__':
    main()