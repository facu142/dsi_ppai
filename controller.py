from typing import List
from .clases_q_usamos.Entity import Llamada, RespuestaCliente, RespuestaPosible, Cliente, CambioEstado, Estado, Pregunta, Encuesta   
# from vistas import *

# Llamadas???
class Controlador:
    def __init__(self, fechaInicio: str, periodo: str, llamadas: List[Llamada]):
        self.fechaInicio = fechaInicio
        self.periodo = periodo
        self.llamada = llamadas
            
    
    def tomaPeriodoSeleccionado(self):
        # conexion la ventana que recibiria la fecha desde y hasta
        pass
    

    def validarLlamadasPorPeriodo(self, fechaPeriodoHasta, fechaPeriodoDesde):
        '''for llamada in self.llamada:
            for respuestaCliente in llamada.respuestaDeEncuensta:
                if respuestaCliente''' 

# Sistema: Muestra los datos de la llamada: cliente, estado actual, duración de la llamada,
#y los datos de las respuestas del cliente asociados a la llamada: Respuestas seleccionadas, descripción de las
#preguntas y descripción de la encuesta que incluye las preguntas.
#Permite generar un csv o imprimir el resultado de la encuesta asociada a la llamada seleccionada.
    def tomarLLamadas(self, llamada):
        nombre_cliente = llamada.getNombreClienteDeLlamada()
        estado = llamada.determinarUltimoEstado()
        duracion = llamada.duracion
        datos_respuestas_clientes = llamada.getRespuestas() # esta va a ser una lista
        for respuesta in datos_respuestas_clientes:
            respuesta = respuesta.respuestaSeleccionada
            pregunta = respuesta.pregunta
        
    
    def tomarOpcGenerarCSV(self):
        pass
    
    def generarCSV(self):
        pass
    
    def finalizarCU(self):
        pass