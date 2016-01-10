import sys
sys.path.append('../')
from SC12K_utils import *

class Instruccion :

	def __init__(self):
		self.init()
		
	def init(self):
		logging.error('init No implementado!')
		self.name = ""
	
	def run(self, params, interprete):
		logging.error('run No implementado!')
		pass
		
	def help(self):
		logging.error('help No implementado!')
		pass