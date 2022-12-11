#En este archivo se encuentran las clases y funciones necesarias para la creación de ordenadores y
# la gestión de las listas de ordenadores.
#Se ha utilizado el patrón de diseño Builder para la creación de los ordenadores.
class Ordenador:
    def __init__(self):
        self.Unidad_central = None
        self.Perifericos_entrada = []
        self.Perifericos_salida = []

class OrdenadorBuilder:
    def __init__(self):
        self.ordenador = Ordenador()

    def GenerarUnidadCentral(self, Unidad_central):
        self.ordenador.Unidad_central = Unidad_central

    def AñadirPerifericoEntrada(self, Periferico_entrada):
        self.ordenador.Perifericos_entrada.append(Periferico_entrada)

    def AñadirPerifericoSalida(self, Periferico_salida):
        self.ordenador.Perifericos_salida.append(Periferico_salida)

class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def Construir_Ordenador(self, Unidad_central, Periferico_entrada, Periferico_salida):
        self.builder = OrdenadorBuilder()
        steps = (self.builder.GenerarUnidadCentral(Unidad_central),
                self.builder.AñadirPerifericoEntrada(Periferico_entrada),
                self.builder.AñadirPerifericoSalida(Periferico_salida))
        [step for step in steps]

    @property
    def ordenador(self):
        return self.builder.ordenador

def Precio(ordenador):
    Precio = ordenador.Unidad_central.precio
    for elem in ordenador.Perifericos_entrada:
        Precio = Precio + elem.precio
    for elem in ordenador.Perifericos_salida:
        Precio = Precio + elem.precio
    return Precio

def Imprimir(ordenador):
    print("   Precio Ordenador: ", Precio(ordenador), "€")
    print("   Componentes: ")
    print("      ", ordenador.Unidad_central)
    for elem in ordenador.Perifericos_entrada:
        print("      ", elem)
    for elem in ordenador.Perifericos_salida:
        print("      ", elem)

def AñadirEntrada(ordenador, Periferico_entrada):
    ordenador.Perifericos_entrada.append(Periferico_entrada)

def AñadirSalida(ordenador, Periferico_salida):
    ordenador.Perifericos_salida.append(Periferico_salida)

def QuitarEntrada(ordenador, Periferico_entrada):
    ordenador.Perifericos_entrada.remove(Periferico_entrada)

def QuitarSalida(ordenador, Periferico_salida):
    ordenador.Perifericos_salida.remove(Periferico_salida)

class mi_lista:
    def __init__(self, contador, precio_total, lista):
        self.contador = 0
        self.precio_total_lista = 0
        self.lista = []

    def poner(self, ordenador):
        self.lista.append(ordenador)
        self.contador = self.contador + 1
        self.precio_total_lista = self.precio_total_lista + Precio(ordenador)

    def quitar(self, ordenador):
        self.lista.remove(ordenador)
        self.contador = self.contador - 1
        self.precio_total_lista = self.precio_total_lista - Precio(ordenador)

    def __str__(self):
        return "LISTA: Hay {} Ordenadores - Precio Total Lista {} €".format(self.contador,self.precio_total_lista)

def ImprimirLista(lista):
    for elem in lista:
        Imprimir(elem)
