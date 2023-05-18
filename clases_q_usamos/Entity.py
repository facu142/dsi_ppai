from typing import List
import datetime

class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.descripcion = descripcion
        self.valor = valor

    def getDescripcionRta(self):
        return self.descripcion


class RespuestaDeCliente:
    def __init__(self, pregunta: str, respuesta: RespuestaPosible):
        self.respuestaSeleccionada = respuesta
        self.pregunta = pregunta

    def getDescripcionRta(self):
        return self.respuestaSeleccionada.getDescripcionRta() # aca agregue return


class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def esFinalizada(self):
        return self.nombre == "Finalizada"

    def esIniciada(self):
        return self.nombre == "Iniciada"

    def getNombre(self):
        return self.nombre


class CambioEstado:
    def __init__(self, fechaHoraInicio, estado: Estado):
        #optimo seria utilizar fecha con el datetime.datetime()
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getNombreEstado(self):
        return self.estado.getNombre()


class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def esCliente(self):
        pass
        # TODO: ???
        # return True

    def getNombre(self):
        return self.nombreCompleto


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


    def calcularDuracion(self):
        return self.duracion

    # TODO: No me queda claro que debe hacer este metodo
    # CREEMOS Q ESTA BIEN, NO ESTOY SEGURO DE NADA
    def determinarEstadoInicial(self):
        if len(self.cambioEstado) > 0:
            return self.cambioEstado[0].estado.getNombre()
        return None

    def determinarUltimoEstado(self):
        if len(self.cambioEstado) > 0:
            return self.cambioEstado[-1].estado.getNombre()
        return None

    # TODO: ????
    "fecha inicio y fecha fin con el datetime.datetime() "
    def esDePeriodo(self, fecha_inicio,fecha_inicio_llamada,fecha_fin_llamada, fecha_fin):
        '''for cambio_estado in self.cambioEstado:
            fecha_inicio_cambio = cambio_estado.getFechaHoraInicio().date()'''
        if fecha_inicio <= fecha_inicio_llamada and  fecha_fin_llamada <= fecha_fin:
                return True
        return False

    def getDuracion(self):
        return self.duracion

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()

    def getRespuestas(self):
        return self.respuestasDeEncuesta

    # TODO: ver este metodo "new()"
    """
    @classmethod
    def new(cls, descripcionOperador, cliente):
        cambio_estado_inicial = CambioEstado(datetime.datetime.now(), Estado("Iniciada"))
        return cls(descripcionOperador, "", 0, False, "", [], [cambio_estado_inicial], cliente)
    """

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador

    def setDuracion(self, duracion):
        self.duracion = duracion

    def setEstadoActual(self, estado):
        fecha_hora_actual = datetime.datetime.now()
        cambio_estado = CambioEstado(fecha_hora_actual, estado)
        self.cambioEstado.append(cambio_estado)

    def obtenerDatosLlamada(self):
        cliente = self.getNombreClienteDeLlamada() # cliente
        estado = self.determinarUltimoEstado() # estado actual REVISAR
        duracion = self.calcularDuracion() # duracion de la llamada
        datos = self.getRespuestas() # respuestas seleccionadas
        for respuesta in datos:
            a = respuesta.getDescripcionRta() # no esta terminado, no encuentro forma de llegar a las preguntas y a la encuesta, lo unico q pense es haciendo una comparacion

class Pregunta:
    def __init__(self, pregunta, respuesta: List[RespuestaPosible]):
        self.pregunta = pregunta
        self.respuesta = respuesta

    def getDescripcion(self):
        return self.descripcion # ?? no tiene atributo descripcion
        # return self.pregunta

    def listarRespuestasPosibles(self):
        # TODO: Acá debería llamar a un metodo de la boundary para mostrar??
        for respuesta in self.respuesta:
            print(respuesta)


class Encuesta:
    def __init__(self, descripcion, fechaFinVigencia, pregunta: List[Pregunta]):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia,
        self.pregunta = pregunta

    def armarEncuesta(self):
        # TODO: nose :(
        print("La encuesta es: ")
        pass         


    def esVigente(self):
        fecha_actual = datetime.datetime.now().date()
        return fecha_actual <= self.fechaFinVigencia

    def getDescripcionEncuesta(self):
        return self.descripcion
