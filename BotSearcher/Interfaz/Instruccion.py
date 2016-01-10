import sys
sys.path.append('../')
from SC12K_utils import *

class Instruccion :

	def __init__(self):
		self.init()
		
	def init(self):
		logging.error(self.__class__.__name__ + ' : init: Metodo no implementado implementado!')
		self.name = ""
	
	def run(self, params, interprete):
		logging.error(self.__class__.__name__ + ' : run Metodo no implementado implementado!')
		pass
		
	def help(self):
		logging.error(self.__class__.__name__ + ' : help Metodo no implementado implementado!')
		pass