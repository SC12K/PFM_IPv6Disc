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
		printD("Parametro\nparams: " + str(params))
		return True
		
	def help(self):
		return "Help for Parametro"