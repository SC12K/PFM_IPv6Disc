from Instruccion import Instruccion

class ListarSondas(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "ListarSondas"
	
	def run(self, params):
		print "Listar Sondas"
		return True
		
	def help(self):
		return "Help for Listar Sondas"