import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion

class NuevaSonda(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "NuevaSonda"
	
	def run(self, params, interprete):
		printD("Nueva Sonda\nparams: " + str(params))
		return True
		
	def help(self):
		return "Help for Nueva Sonda"