from typing import List
from Clientes import *
from Estados import *
from CambiosEstado import *
from RespuestasPosibles import *
from RespuestasDeCliente import *

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular


class Estado:
    def __init__(self, nombre):
        self.nombre = nombre


class CambioEstado:
    def __init__(self, fechaHoraInicio, estado: Estado):
        #optimo seria utilizar fecha con el datetime.datetime()
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado


class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.descripcion = descripcion
        self.valor = valor


class RespuestaDeCliente:
    def __init__(self, fechaEncuesta: str, respuestaSeleccionada: RespuestaPosible): # ver formato de fecha
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada


class Llamada:
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

llamada1 = Llamada('descripcion1', 'detalle1', 12, False, '', [], [cambioEstado1Ll1, cambioEstado2Ll1, cambioEstado3Ll1], cliente1)
llamada2 = Llamada('descripcion2', 'detalle2', 5, False, '', [], [cambioEstado1Ll2, cambioEstado2Ll2, cambioEstado3Ll2, cambioEstado4Ll2], cliente4)
llamada3 = Llamada('descripcion3', 'detalle3', 3, True, '', [respuestaC3,respuestaC4], [cambioEstado1Ll3, cambioEstado2Ll3, cambioEstado3Ll3, cambioEstado4Ll3, cambioEstado5Ll3], cliente2)
llamada4 = Llamada('descripcion4', 'detalle4', 10, True, 'Mal audio', [respuestaC1,respuestaC2], [cambioEstado1Ll4, cambioEstado2Ll4, cambioEstado3Ll4, cambioEstado4Ll4, cambioEstado5Ll4], cliente5)
llamada5 = Llamada('descripcion5', 'detalle5', 20, True, '', [respuestaC5,respuestaC6], [cambioEstado1Ll5, cambioEstado2Ll5, cambioEstado3Ll5, cambioEstado4Ll5, cambioEstado5Ll5], cliente3)

llamadas = [llamada1,llamada2,llamada3,llamada4,llamada5]

def creador(coleccion):
    return coleccion

def main():
    pass

if __name__ == '__main__':
    main()