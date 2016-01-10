import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion

class EliminarEjecutor(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "EliminarEjecutor"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando EliminarEjecutor. Parametros: " + str(params))
		if params == "" or params == None:
			self.help()
			return False

		paramList = params.split(' ',1)
		if len(paramList) == 1 :
			nombre = paramList[0]
		else :
			self.help()
			return False
			
		return GdS.eliminarEjecutor(nombre)
		
	def help(self):
		logging.debug("Ejecutando EliminarEjecutor help")
		res = ""
		res+= "************************** Eliminar Ejecutor ****************************\n"
		res+= "EliminarEjecutor <nombre> : Elimina el ejecutor de nombre dado\n"
		res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, no\n"
		res+= "funcionara en la siguiente ejecucion."
		res+= "****************************************************************************"
		return res
		
class EliminarDispensador(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "EliminarDispensador"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando EliminarDispensador. Parametros: " + str(params))
		if params == "" or params == None:
			self.help()
			return False

		paramList = params.split(' ',1)
		if len(paramList) == 1 :
			nombre = paramList[0]
		else :
			self.help()
			return False
			
		return GdS.eliminarDispensador(nombre)
		
	def help(self):
		logging.debug("Ejecutando EliminarDispensador help")
		res = ""
		res+= "************************** Eliminar Dispensador ****************************\n"
		res+= "EliminarDispensador <nombre> : Elimina el dispensador de nombre dado\n"
		res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, no\n"
		res+= "funcionara en la siguiente ejecucion."
		res+= "****************************************************************************"
		return res
		
class EliminarSonda(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "EliminarSonda"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando EliminarSonda. Parametros: " + str(params))
		if params == "" or params == None:
			self.help()
			return False

		paramList = params.split(' ',1)
		if len(paramList) == 1 :
			nombre = paramList[0]
		else :
			self.help()
			return False
			
		return GdS.eliminarSonda(nombre)
		
	def help(self):
		logging.debug("Ejecutando EliminarSonda help")
		res = ""
		res+= "************************** Eliminar Sonda ****************************\n"
		res+= "EliminarSonda <nombre> : Elimina el sonda de nombre dado\n"
		res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, no\n"
		res+= "funcionara en la siguiente ejecucion."
		res+= "****************************************************************************"
		return res