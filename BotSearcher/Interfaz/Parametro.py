import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion

class Parametro(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "Parametro"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Parametro. Parametros: " + str(params))
		return True
		
	def help(self):
		logging.debug("Ejecutando Parametro help")
		return "Help for Parametro"