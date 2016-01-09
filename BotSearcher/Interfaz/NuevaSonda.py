from Instruccion import Instruccion

class NuevaSonda(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "NuevaSonda"
	
	def run(self, params):
		print "Nueva Sonda"
		return True
		
	def help(self):
		return "Help for Nueva Sonda"