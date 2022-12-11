# En este archivo se encuentran las clases y funciones necesarias para la defincion de los componentes que se van
# a utilizar en la creación de los ordenadores.
#Te adjunto un pequeño gráfico de la relación entre las clases que me ha salido util para programarlo utilizando las herencias.

import abc

class Componente(metaclass=abc.ABCMeta):
    def __init__(self, fabricante, modelo, precio,):
        self.fabricante = fabricante
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return "Fabricante: {}, Modelo: {}, Precio: {} €".format(self.fabricante, self.modelo, self.precio)
    def cambioprecio(self, nuevoprecio):
        self.precio = nuevoprecio

class Unidad_central(Componente):
	def __init__(self, fabricante, modelo, precio):
		Componente.__init__(self, fabricante, modelo, precio)
	def __str__(self):
		return "UNIDAD CENTRAL - " + Componente.__str__(self)

class Periferico(Componente):
	def __init__(self, fabricante, modelo, precio, puertos):
		Componente.__init__(self, fabricante, modelo, precio)
		self.puertos = puertos
	def __str__(self):
		return Componente.__str__(self) + ", Puertos: {}".format(self.puertos)

class Periferico_entrada(Periferico):
	def __init__(self, fabricante, modelo, precio, puertos, conector):
		Periferico.__init__(self, fabricante, modelo, precio, puertos)
		self.conector = conector
	def __str__(self):
		return Periferico.__str__(self) + ", Conector: {}".format(self.conector)

class Teclado(Periferico_entrada):
	def __init__(self, fabricante, modelo, precio, puertos, conector):
		Periferico_entrada.__init__(self, fabricante, modelo, precio, puertos, conector)
	def __str__(self):
		return "TECLADO - " + Periferico_entrada.__str__(self)

class Raton(Periferico_entrada):
	def __init__(self, fabricante, modelo, precio, puertos, conector):
		Periferico_entrada.__init__(self, fabricante, modelo, precio, puertos, conector)
	def __str__(self):
		return "RATON - " + Periferico_entrada.__str__(self)

class Tableta(Periferico_entrada):
	def __init__(self, fabricante, modelo, precio, puertos, conector):
		Periferico_entrada.__init__(self, fabricante, modelo, precio, puertos, conector)
	def __str__(self):
		return "TABLETA - " + Periferico_entrada.__str__(self)

class Periferico_salida(Componente):
	def __init__(self, fabricante, modelo, precio, puertos):
		Periferico.__init__(self, fabricante, modelo, precio, puertos)
	def __str__(self):
		return Periferico.__str__(self)

class Pantalla(Periferico_salida):
	def __init__(self, fabricante, modelo, precio, puertos):
		Periferico_salida.__init__(self, fabricante, modelo, precio, puertos)
	def __str__(self):
		return "PANTALLA - " + Periferico_salida.__str__(self)

class Impresora(Periferico_salida):
	def __init__(self, fabricante, modelo, precio, puertos, tipocartuchotoner):
		Periferico_salida.__init__(self, fabricante, modelo, precio, puertos)
		self.tipocartucho = tipocartuchotoner
	def __str__(self):
		return Periferico_salida.__str__(self) + ", Tipo c/t: {}".format(self.tipocartucho)

class Impresora_inyeccion(Impresora):
	def __init__(self, fabricante, modelo, precio, puertos, tipocartuchotoner):
		Impresora.__init__(self, fabricante, modelo, precio, puertos, tipocartuchotoner)
	def __str__(self):
		return "IMPRESORA INYECCION - " + Impresora.__str__(self)

class Impresora_laser(Impresora):
	def __init__(self, fabricante, modelo, precio, puertos, tipocartuchotoner, numpaginas):
		Impresora.__init__(self, fabricante, modelo, precio, puertos, tipocartuchotoner)
		self.numpaginas = numpaginas
	def __str__(self):
		return "IMPRESORA LASER - " + Impresora.__str__(self) + ", Páginas: {}".format(self.numpaginas)