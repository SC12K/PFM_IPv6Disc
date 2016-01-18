import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion
import getopt

class ListaEjecucion(Instruccion) :

        def __init__(self):
		self.init()
		
	def init(self):
		self.name = "ListaEjecucion"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Lista Ejecucion. Parametros: " + str(params))
		print GdE.listarEjecucion()
		return True
		
	def help(self):
		logging.debug("Ejecutando Lista Ejecucion help")
		return "Help for Lista Ejecucion"
	      
	     
class PonerEnCola(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "PonerEnCola"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Poner En Cola. Parametros: " + str(params))
		try:
			options, args = getopt.getopt(params.split(),'n:',['nombre='])
			logging.debug("Options: " + str(options))
			logging.debug("Args: " + str(args))
		except:
			logging.debug("Argumentos incorrectos")
			self.help()
			return False

		if len(options) == 0:
			self.help()
			return False
		      
		for opt in options:
			if opt[0] == '-n' or opt== 'nombre':
				nombre = opt[1]
			else:
				self.help()
				return False
			      
		sonda = GdS.getSonda(nombre)
		if not (sonda == None):
			logging.info("Anadiendo sonda " + nombre + " Dispensador: " + sonda.getNombreDispensador() + " Ejecutor: " + sonda.getNombreEjecutor() + " a la cola de ejecucion")
			return GdE.anadirSonda(sonda)
		else:
			logging.warning("Error al cargar " + nombre);
			return False
		
		
	def help(self):
		res = ""
		res+= "******************************* Nueva Sonda ***********************************\n"
		res+= "PonerEnCola --nombre <nombre>\n"
		res+= "PonerEnCola -n Nombre\n"
		res+= "Anade una sonda a la cola de ejecucion. Se ejecutara al llegar su turno.\n"
		res+= "*******************************************************************************"
		return res
	      	      
class EliminarDeEjecucion(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "EliminarDeEjecucion"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando EliminarDeEjecucion. Parametros: " + str(params))
		if params == "" or params == None:
			self.help()
			return False

		paramList = params.split(' ',1)
		if len(paramList) == 1 :
			index = int(paramList[0])
		else :
			self.help()
			return False

		return GdE.eliminarSonda(index)
		
	def help(self):
		logging.debug("Ejecutando EliminarDeEjecucion help")
		res = ""
		res+= "************************** Eliminar Sonda ****************************\n"
		res+= "EliminarDeEjecucion <index> : Elimina el sonda de nombre dado\n"
		res+= "de la cola de ejecucion. Ver la cola de ejecucion para adquirir el indice.\n"
		res+= "****************************************************************************"
		return res

class Ejecutar(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "Ejecutar"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Ejecutar. Parametros: " + str(params))
		GdE.Ejecutar()
		return True
		
	def help(self):
		logging.debug("Ejecutando Ejecutar help")
		res = ""
		res+= "************************** Eliminar Sonda ****************************\n"
		res+= "Ejecutar: Inicia la ejecucion de las sondas a traves de un demonio.\n"
		res+= "Al quedarse sin en la lista, el demonio se detendra hasta que se anadan\n"
		res+= "mas y empezara automaticamente.\n"
		res+= "****************************************************************************"
		return res

class Parar(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "Parar"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Parar. Parametros: " + str(params))
		GdE.Parar()
		return True
		
	def help(self):
		logging.debug("Ejecutando Parar help")
		res = ""
		res+= "************************** Eliminar Sonda ****************************\n"
		res+= "Parar: Detiene la ejecucion.\n"
		res+= "****************************************************************************"
		return res	      
