import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion

class ListarSondas(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "ListarSondas"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Listar Sondas. Parametros: " + str(params))
		GdS.listarSondas()
		return True
		
	def help(self):
		logging.debug("Ejecutando Listar Sondas help")
		return "Help for Listar Sondas"
		
class ListarDispensadores(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "ListarDispensadores"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Listar Dispensadores. Parametros: " + str(params))
		GdS.listarDispensadores()
		return True
		
	def help(self):
		logging.debug("Ejecutando Listar Dispensadores help")
		return "Help for Listar Dispensadores"

class ListarEjecutores(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "ListarEjecutores"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Listar Ejecutores. Parametros: " + str(params))
		GdS.listarEjecutores()
		return True
		
	def help(self):
		logging.debug("Ejecutando Listar Ejecutores help")
		return "Help for Listar Ejecutores"