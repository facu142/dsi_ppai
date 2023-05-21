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

llamada1 = Llamada('descripcion1', 'detalle1', 12, True, 'observacion1', [respuestaC1,respuestaC2], [cambioEstado1, cambioEstado2], cliente1)
llamada2 = Llamada('descripcion1', 'detalle1', 5, False, 'observacion1', [], [cambioEstado7, cambioEstado8], cliente4)
llamada3 = Llamada('descripcion1', 'detalle1', 3, True, 'observacion1', [respuestaC3,respuestaC4], [cambioEstado3, cambioEstado4], cliente2)
llamada4 = Llamada('descripcion1', 'detalle1', 10, False, 'observacion1', [], [cambioEstado9, cambioEstado10], cliente5)
llamada5 = Llamada('descripcion1', 'detalle1', 20, True, 'observacion1', [respuestaC5,respuestaC6], [cambioEstado5, cambioEstado6], cliente3)

llamadas = [llamada1,llamada2,llamada3,llamada4,llamada5]

def creador(coleccion):
    return coleccion

def main():
    pass

if __name__ == '__main__':
    main()