class RespuestaPosible:
    def __init__(self, descripcion: str, valor: str):
        self.descripcion = descripcion
        self.valor = valor

# Sriven para preguntas 1 2 7
respuestaP1 = RespuestaPosible('1', '1')
respuestaP2 = RespuestaPosible('2', '2')
respuestaP3 = RespuestaPosible('3', '3')
respuestaP4 = RespuestaPosible('4', '4')
respuestaP5 = RespuestaPosible('5', '5')
respuestaP6 = RespuestaPosible('6', '6')
respuestaP7 = RespuestaPosible('7', '7')
respuestaP8 = RespuestaPosible('8', '8')
respuestaP9 = RespuestaPosible('9', '9')
respuestaP10 = RespuestaPosible('10', '10')

# Sirven para pregunta 3 4 5 6 8 9 10
respuestaPA = RespuestaPosible('1', 'SI')
respuestaPB = RespuestaPosible('2', 'NO')


repuestasPosibles = [respuestaP1,respuestaP2,respuestaP3, respuestaP4, respuestaP5, respuestaP6, respuestaP7, respuestaP8, respuestaP9, respuestaP10, respuestaPA, respuestaPB]