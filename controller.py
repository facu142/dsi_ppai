from typing import List
from .clases_q_usamos.Entity import Llamada, RespuestaCliente, RespuestaPosible, Cliente, CambioEstado, Estado, Pregunta, Encuesta   
import datetime
# from vistas import *

# Llamadas???
class Controlador:
    def __init__(self, fechaInicio: str, periodo: str, llamadas: List[Llamada]):
        self.fechaInicio = fechaInicio
        self.periodo = periodo
        self.llamada = llamadas
            
    def getHoraActual():
        hora_actual = datetime.datetime.now().time()
        return hora_actual

    def tomaPeriodoSeleccionado(self):
        # conexion la ventana que recibiria la fecha desde y hasta
        pass
    #no se si iria asi, o lo emprolijamos mas
    def tieneRespuestas(llamadas):
        llamadas_con_respuesta=[]
        for llamada in llamadas:
            if llamada.respuestasDeEncuesta: llamadas_con_respuesta.append(llamada)
            #nos devuelve las llamadas que tienen respuestas
        return llamadas_con_respuesta
    
    def validarLlamadasPorPeriodo(self, fechaPeriodoHasta, fechaPeriodoDesde):   
        #fechaPeriodoDesde,fechaPeriodoHasta=tomaPeriodoSeleccionado(self)     
        llamadas_con_respuesta = self.tieneRespuestas(self.llamada)
        llamadas_Periodo=[]
        for llamada in llamadas_con_respuesta:
            #es necesario ir a buscar el primer Estado? si en teoria con el cambioEstado[0] ya sabemos q es el 1ro"
            horaInicial=llamada.cambioEstado[0].getFechaHoraInicio()
            #getHoraActual
            hora_actual = self.getHoraActual()
            duracion = hora_actual - horaInicial
            #fechaInicio y fechaFin son los datos que se obtienen de la funcion tomaPeriodoSeleccionado()
            if llamada.esDePeriodo(fecha_inicio,duracion, fecha_fin): llamadas_Periodo.append(llamada)
        return llamadas_Periodo

# Sistema: Muestra los datos de la llamada: cliente, estado actual, duración de la llamada,
#y los datos de las respuestas del cliente asociados a la llamada: Respuestas seleccionadas, descripción de las
#preguntas y descripción de la encuesta que incluye las preguntas.
#Permite generar un csv o imprimir el resultado de la encuesta asociada a la llamada seleccionada.
    def tomarLLamadas(self, llamada):
        nombre_cliente = llamada.getNombreClienteDeLlamada()
        estado = llamada.determinarUltimoEstado()
        duracion = llamada.calcularDuracion()
        datos_respuestas_clientes = llamada.getRespuestas() # esta va a ser una lista
        for respuestaDeCliente in datos_respuestas_clientes:
            respuesta = respuestaDeCliente.respuestaSeleccionada # mmmmm no se no se
            descripcion_pregunta = RespuestaPosible.getDescripcionRta() # mmmmm no se no se
            # faltan las 2 descripciones
        
    
    def tomarOpcGenerarCSV(self):
        pass
    
    def generarCSV(self):
        pass
    
    def finalizarCU(self):
        pass