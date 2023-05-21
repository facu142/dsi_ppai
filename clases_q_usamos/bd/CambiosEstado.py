from datetime import datetime, date
import random
from Estados import *

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

class CambioEstado:
    def __init__(self, fechaHoraInicio, estado: Estado):
        #optimo seria utilizar fecha con el datetime.datetime()
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado


cambioEstado1 = CambioEstado(date(2009, 2, 3),estado1)
cambioEstado2 = CambioEstado(date(2001, 9, 25),estado2)
cambioEstado3 = CambioEstado(date(2022, 11, 8),estado1)
cambioEstado4 = CambioEstado(date(1991, 12, 13),estado2)
cambioEstado5 = CambioEstado(date(2010, 8, 14),estado1)
cambioEstado6 = CambioEstado(date(2011, 2, 26),estado2)
cambioEstado7 = CambioEstado(date(1993, 8, 17),estado1)
cambioEstado8 = CambioEstado(date(2010, 8, 20),estado2)
cambioEstado9 = CambioEstado(date(2019, 3, 16),estado1)
cambioEstado10 = CambioEstado(date(2011, 7, 7),estado2)

cambiosDeEstados = [cambioEstado1,cambioEstado2,cambioEstado3,cambioEstado4,cambioEstado5,cambioEstado6,cambioEstado7,cambioEstado8,cambioEstado9,cambioEstado10]

def main(): # el main es para hacer pruebas.

    #fecha = strptime(fecha_str, "%d/%m/%Y").cambioEstado1 = date()

    def creador(coleccion):
        for i in range(10):
            dia = random.randint(1,30)
            mes = random.randint(1,12)
            año = random.randint(1990, 2022)

            fecha_str = str(f'{dia}/{mes}/{año}')

            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").cambioEstado1 = date()

            coleccion.append(fecha)
        return coleccion

    cambiosDeEstados = creador(cambiosDeEstados)
    print(cambiosDeEstados)

    cont = 0
    for cambio in cambiosDeEstados:
        
        if cont == 0:
            actual = cambio
        elif cambio.year > actual.year:
            actual = cambio
        elif cambio.year == actual.year and cambio.month > actual.month:
            actual = cambio
        elif cambio.year == actual.year and cambio.month == actual.month and cambio.day > actual.day:
            actual = cambio

        cont += 1
    
    print(actual)

if __name__ == '__main__':
    main()