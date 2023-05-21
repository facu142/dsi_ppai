class Estado:
    estados=[]
    def __init__(self, nombre):
        self.nombre = nombre
        self.estados.append(self)

estado1 = Estado('Finalizada')
estado2 = Estado('EnCurso')
estado3 = Estado('Cancelado')
estado5 = Estado('PendienteDeEscucha')
estado6 = Estado('Correcta')
estado7 = Estado('Observacion')
estado8 = Estado('Descartado')


def main():
    pass

if __name__ == '__main__':
    main()