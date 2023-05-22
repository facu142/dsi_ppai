from datetime import datetime, date
import random
from Estados import *


class CambioEstado:
    def __init__(self, fechaHoraInicio, estado: Estado):
        #optimo seria utilizar fecha con el datetime.datetime()
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado


# Cambios de estado de llamada 1
cambioEstado1Ll1 = CambioEstado(datetime(2009, 2, 3, 15, 0, 0),estado1)
cambioEstado2Ll1 = CambioEstado(datetime(2009, 2, 3, 15, 1, 0),estado3)
cambioEstado3Ll1 = CambioEstado(datetime(2009, 2, 3, 15, 2, 0),estado8)

# Cambios de estado de llamada 2
cambioEstado1Ll2 = CambioEstado(datetime(2010, 11, 7, 10, 43, 0),estado1)
cambioEstado2Ll2 = CambioEstado(datetime(2010, 11, 7, 10, 44, 0),estado2)
cambioEstado3Ll2 = CambioEstado(datetime(2010, 11, 7, 10, 45, 0),estado3)
cambioEstado4Ll2 = CambioEstado(datetime(2010, 11, 7, 10, 46, 0),estado8)

# Cambios de estado de llamada 3 LLAMADA FINALIZADA
cambioEstado1Ll3 = CambioEstado(datetime(2015, 12, 7, 10, 30, 0),estado1)
cambioEstado2Ll3 = CambioEstado(datetime(2015, 12, 7, 10, 31, 0),estado2)
cambioEstado3Ll3 = CambioEstado(datetime(2015, 12, 7, 10, 32, 0),estado2)
cambioEstado4Ll3 = CambioEstado(datetime(2015, 12, 7, 10, 33, 0),estado5)
cambioEstado5Ll3 = CambioEstado(datetime(2015, 12, 7, 10, 34, 0),estado6)

# Cambios de estado de llamada 4 LLAMADA FINALIZADA
cambioEstado1Ll4 = CambioEstado(datetime(2012, 5, 5, 20, 15, 0),estado1)
cambioEstado2Ll4 = CambioEstado(datetime(2012, 5, 5, 20, 16, 0),estado2)
#cambioEstado3Ll4 = CambioEstado(datetime(2012, 5, 5, 20, 17, 0),estado4)
cambioEstado4Ll4 = CambioEstado(datetime(2012, 5, 5, 20, 18, 0),estado5)
cambioEstado5Ll4 = CambioEstado(datetime(2012, 5, 5, 20, 20, 0),estado7) # estado de observacion

# Cambios de estado de llamada 5 LLAMADA FINALIZADA
cambioEstado1Ll5 = CambioEstado(datetime(2013, 7, 14, 14, 0, 0),estado1)
cambioEstado2Ll5 = CambioEstado(datetime(2013, 7, 14, 14, 1, 0),estado2)
#cambioEstado3Ll5 = CambioEstado(datetime(2013, 7, 14, 14, 2, 0),estado4)
cambioEstado4Ll5 = CambioEstado(datetime(2013, 7, 14, 14, 3, 0),estado5)
cambioEstado5Ll5 = CambioEstado(datetime(2013, 7, 14, 14, 4, 0),estado6)

cambiosDeEstados = [cambioEstado1Ll1, cambioEstado2Ll1, cambioEstado3Ll1,
                    cambioEstado1Ll2, cambioEstado2Ll2, cambioEstado3Ll2, cambioEstado4Ll2,
                    cambioEstado1Ll3, cambioEstado2Ll3, cambioEstado3Ll3, cambioEstado4Ll3, cambioEstado5Ll3,
                    cambioEstado1Ll4, cambioEstado2Ll4, '''cambioEstado3Ll4''', cambioEstado4Ll4, cambioEstado5Ll4,
                    cambioEstado1Ll5, cambioEstado2Ll5, '''cambioEstado3Ll5''', cambioEstado4Ll5, cambioEstado5Ll5]

'''
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
'''

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