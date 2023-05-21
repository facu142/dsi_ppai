from typing import List

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

llamada1 = Llamada()


llamadas = [llamada1,llamada2,llamada3,llamada4,llamada5,llamada6,llamada7,llamada8,llamada9,llamada10]

def creador(coleccion):
    return coleccion

def main():
    pass

if __name__ == '__main__':
    main()