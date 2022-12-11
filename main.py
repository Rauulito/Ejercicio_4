from componentes import *
from ordenadores import *

if __name__ == '__main__':

    # Para poder probar generamos unos cuantos componentes de todos los tipos
    UC1 = Unidad_central("fabUC1", "modUC1", 1200)
    UC2 = Unidad_central("fabUC2", "modUC1", 1500)
    UC3 = Unidad_central("fabUC3", "modUC1", 2000)
    TE1 = Teclado("fabTE1", "modTE1", 100, 3, "conecA")
    TE2 = Teclado("fabTE2", "modTE2", 120, 3, "conecA")
    RA1 = Raton("fabRA1", "modRA1", 50, 3, "conecB")
    RA2 = Raton("fabRA2", "modRA2", 60, 3, "conecB")
    TA1 = Tableta("fabTA1", "modTA1", 200, 3, "conecC")
    TA2 = Tableta("fabTA2", "modTA2", 250, 3, "conecC")
    PA1 = Pantalla("fabPA1", "modPA1", 300, 3)
    PA2 = Pantalla("fabPA2", "modPA2", 400, 3)
    II1 = Impresora_inyeccion("fabII1", "modII1", 150, 3, "cartuII1")
    II2 = Impresora_inyeccion("fabII2", "modII2", 350, 3, "cartuII2")
    IL1 = Impresora_laser("fabIL1", "modIL1", 700, 3, "tonerIL1", 50)

    # Prueba de construcción de ordenador
    engineer = HardwareEngineer()
    engineer.Construir_Ordenador(UC1, TE1, IL1)
    ordenador1 = engineer.ordenador
    print("ORDENADOR 1")
    Imprimir(ordenador1)

    # Prueba de cambio de precio de uno de los componentes
    UC1.cambioprecio(1000)
    print("CAMBIO PRECIO - ORDENADOR 1: ")
    Imprimir(ordenador1)

    # Prueba de añadir nuevos componentes
    AñadirEntrada(ordenador1,RA2)
    AñadirEntrada(ordenador1,TA2)
    AñadirSalida(ordenador1,PA2)
    AñadirSalida(ordenador1,II2)
    print("AÑADIR COMPONENTES - ORDENADOR 1: ")
    Imprimir(ordenador1)

    # Prueba de quitar componentes
    QuitarEntrada(ordenador1,TA2)
    QuitarSalida(ordenador1,II2)
    print("QUITAR COMPONENTES - ORDENADOR 1: ")
    Imprimir(ordenador1)

    # Para poder probar la lista total generamos algunos ordenadores
    engineer = HardwareEngineer()
    engineer.Construir_Ordenador(UC2, RA1, PA1)
    ordenador2 = engineer.ordenador

    engineer = HardwareEngineer()
    engineer.Construir_Ordenador(UC3, TA1, II1)
    ordenador3 = engineer.ordenador

    # Prueba de añadir ordenadores en la lista
    print("PRUEBA AÑADIR ORDENADORES A LA LISTA: ")
    ListaOrdenadores = mi_lista(0,0,[])
    ListaOrdenadores.poner(ordenador1)
    ListaOrdenadores.poner(ordenador2)
    ListaOrdenadores.poner(ordenador3)
    print(ListaOrdenadores)
    ImprimirLista(ListaOrdenadores.lista)

    # Prueba de quitar ordenadores de la lista
    print("PRUEBA QUITAR ORDENADORES A LA LISTA: ")
    ListaOrdenadores.quitar(ordenador2)
    print(ListaOrdenadores)
    ImprimirLista(ListaOrdenadores.lista)
