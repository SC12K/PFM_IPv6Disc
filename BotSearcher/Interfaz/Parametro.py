from Instruccion import Instruccion

class Parametro(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "Parametro"
	
	def run(self, params):
		print "Parametro"
		return True
		
	def help(self):
		return "Help for Parametro"