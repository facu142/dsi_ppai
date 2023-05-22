from typing import List
from Clientes import *
from Estados import *
from CambiosEstado import *
from RespuestasPosibles import *
from RespuestasDeCliente import *

class Llamada:
    ArrLlamadas=[]
    def __init__(self, descripcionOperador: str, detalleAccionRequerida: str, duracion: int, encuestaEnviada: bool,
                 observacionAuditor: str, respuestasDeEncuesta: List[RespuestaDeCliente],
                 cambioEstado: List[CambioEstado],
                 cliente: Cliente):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
        self.respuestasDeEncuesta = respuestasDeEncuesta
        self.cambioEstado = cambioEstado
        self.cliente = cliente
        self.ArrLlamadas.append(self)

llamada1 = Llamada('descripcion1', 'detalle1', 12, False, '', [], [cambioEstado1Ll1, cambioEstado2Ll1, cambioEstado3Ll1], cliente1)
llamada2 = Llamada('descripcion2', 'detalle2', 5, False, '', [], [cambioEstado1Ll2, cambioEstado2Ll2, cambioEstado3Ll2, cambioEstado4Ll2], cliente4)
llamada3 = Llamada('descripcion3', 'detalle3', 3, True, '', [respuestaC3,respuestaC4], [cambioEstado1Ll3, cambioEstado2Ll3, cambioEstado3Ll3, cambioEstado4Ll3, cambioEstado5Ll3], cliente2)
llamada4 = Llamada('descripcion3', 'detalle3', 3, True, '', [respuestaC1,respuestaC2], [cambioEstado1Ll3, cambioEstado2Ll3, cambioEstado3Ll3, cambioEstado4Ll3, cambioEstado5Ll3], cliente5)
llamada5 = Llamada('descripcion5', 'detalle5', 20, True, '', [respuestaC5,respuestaC6], [cambioEstado1Ll5, cambioEstado2Ll5, cambioEstado4Ll5, cambioEstado5Ll5], cliente3)



def creador(coleccion):
    return coleccion

def main():
    pass

if __name__ == '__main__':
    main()