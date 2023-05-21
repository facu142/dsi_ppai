import random

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

cliente1 = Cliente("44203020", "Juan Mateo Blencio", "3547623905")
cliente2 = Cliente("12345678", "Juan Pérez", "123456789")
cliente3 = Cliente("87654321", "María González", "987654321")
cliente4 = Cliente("56789123", "Carlos López", "567890123")
cliente5 = Cliente("98765432", "Laura Rodríguez", "987654321")
cliente6 = Cliente("23456789", "Pedro Sánchez", "123456789")
cliente7 = Cliente("67891234", "Ana Martínez", "987654321")
cliente8 = Cliente("34567891", "Luis Hernández", "567890123")
cliente9 = Cliente("89123456", "Sofía Torres", "987654321")
cliente10 = Cliente("45678912", "Andrés Flores", "123456789")

clientes = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10]

def main():

    class Cliente:
        def __init__(self, dni, nombreCompleto, nroCelular):
            self.dni = dni
            self.nombreCompleto = nombreCompleto
            self.nroCelular = nroCelular

    nombres = ["Sofía", "Isabella", "Valentina", "Camila", "Emma", "Mía", "Luciana", "Victoria", "Martina", "Amanda",
    "Mateo", "Santiago", "Benjamín", "Lucas", "Emilio", "Sebastián", "Diego", "Daniel", "Samuel", "Nicolás",
    "Luisa", "María", "Ana", "Laura", "Catalina", "Gabriela", "Carolina", "Fernanda", "Daniela", "Juliana",
    "Juan", "Carlos", "Miguel", "Pedro", "Andrés", "Felipe", "Javier", "Alejandro", "Raúl", "Ricardo",
    "Valeria", "Ximena", "Florencia", "Abril", "Ariana", "Carla", "Giselle", "Lorena", "Renata", "Vanessa"]

    apellidos = [ "García", "Rodríguez", "Martínez", "López", "Hernández", "González", "Pérez", "Sánchez", "Ramírez", "Flores",
    "Torres", "Rivera", "Soto", "Díaz", "Rojas", "Romero", "Vargas", "Mendoza", "Guerrero", "Ortega",
    "Silva", "Cruz", "Reyes", "Álvarez", "Castillo", "Méndez", "Ramos", "Moreno", "Jiménez", "Cortez",
    "Acosta", "Paz", "Aguilar", "Chávez", "Ríos", "Medina", "Delgado", "Castro", "Rocha", "Fuentes",
    "Arias", "Morales", "Valdez", "Vega", "Escobar", "Miranda", "Navarro", "Santos", "Espinoza", "Cabrera"]

    cantidadDeClientes = 5
    clientesLista = clienteIndividual = ''
    
    for i in range(12, 12+cantidadDeClientes):
        dni = random.randint(40000000, 50000000)
        nombreCompleto = str(random.choice(nombres)+' '+random.choice(apellidos))
        nroCelular = random.randint(3547623905,9999999999)
        
        if i == 0:
            clientesLista = f'[cliente{i+1},'
            clienteIndividual = f'cliente{i+1} = Cliente({str(dni)},{str(nombreCompleto)},{str(nroCelular)})\n'
        elif i == (cantidadDeClientes+1):
            clientesLista += f'cliente{i+1}]'
            clienteIndividual += f'cliente{i+1} = Cliente({str(dni)},{str(nombreCompleto)},{str(nroCelular)})'
        else:
            clientesLista += f'cliente{i},'
            clienteIndividual += f'cliente{i+1} = Cliente({str(dni)},{str(nombreCompleto)},{str(nroCelular)})\n'
    
    print()
    print(clientesLista)
    print()
    print(clienteIndividual)
    print()
        
if __name__ == '__main__':
    main()