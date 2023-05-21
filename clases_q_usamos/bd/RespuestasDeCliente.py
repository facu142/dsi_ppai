from RespuestasPosibles import *
#esta mal planteado
class RespuestaDeCliente:
    respuestaCliente=[]
    def __init__(self, fechaEncuesta: str, respuestaSeleccionada: RespuestaPosible): # ver formato de fecha
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada
        self.respuestaCliente.append(self)

respuestaC1 = RespuestaDeCliente('01/12/2022', respuestaP10)
respuestaC2 = RespuestaDeCliente('02/08/2022', respuestaP2)
respuestaC3 = RespuestaDeCliente('03/09/2022', respuestaP3)
respuestaC4 = RespuestaDeCliente('04/10/2022', respuestaP8)
respuestaC5 = RespuestaDeCliente('05/11/2022', respuestaP5)
respuestaC6 = RespuestaDeCliente('06/01/2023', respuestaP6)
respuestaC7 = RespuestaDeCliente('07/04/2023', respuestaP9)
respuestaC8 = RespuestaDeCliente('08/03/2023', respuestaP10)
respuestaC9 = RespuestaDeCliente('09/02/2023', respuestaPA)
respuestaC10 = RespuestaDeCliente('10/01/2023', respuestaPB)

def main():
    for respuestas in RespuestaDeCliente.respuestaCliente:
        print(respuestas.respuestaSeleccionada.descripcion)

if __name__ == '__main__':
    main()