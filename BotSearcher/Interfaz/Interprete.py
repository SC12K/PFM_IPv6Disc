import Instruccion
from SC12K_utils import printD

class Interprete :
	
	class Ayuda(Instruccion.Instruccion):
		def init(self):
			self.name = "ayuda"
		
		def run(self, params, interpreter):
			printD("Ayuda")
			if (params == None) :
				res = self.help()
				print res
			else :
				res = interpreter.ejecHelp(params)
				print res
				
			return True
			
		def help(self):
			return "Help for Help"
		
	
	def __init__(self):
		print "BotSearcher IPv6 Manager"
		print " ____   ____ _ ____  _  __  _____"                    
		print "/ ___| / ___/ |___ \| |/ / |_   _|__  __ _ _ __ ___"  
		print "\___ \| |   | | __) | ' /    | |/ _ \/ _` | '_ ` _ \\"
		print " ___) | |___| |/ __/| . \    | |  __/ (_| | | | | | |"
		print "|____/ \____|_|_____|_|\_\   |_|\___|\__,_|_| |_| |_|"
		print ""
		print "Interprete para la configuracion de la ejecucion de busquedas."
		print ""

		self.repertorio = dict()
		self.cargarRepertorio("")
		printD(self.repertorio.viewkeys())
		
	
	def ejecInstr(self, instr, params) :
		printD(self.repertorio.keys)
		if instr in self.repertorio :
			#separar parametros de instruccion
			return self.repertorio[instr].run(params,self)
		else :
			return False

	def cargarRepertorio(self, xmlfile) :
		instruccion = self.Ayuda()
		self.repertorio[instruccion.name]= instruccion
		pass
		
	def ejecHelp(self, instr) :
		if instr in self.repertorio :
			return self.repertorio[instr].help()
		else :
			return "La instruccion no existe"
		
		
	def ejecutarBucle(self) :
		
		instr = ''
		while instr != "exit":
		
			instr = raw_input('$>>')
			printD("instruccion " + instr)
			instrParts = instr.split(' ', 1)
			if len(instrParts) != 2 :
				execu = self.ejecInstr(instrParts[0], None)
			else : 
				execu = self.ejecInstr(instrParts[0], instrParts[1])
			
			if(not execu and instrParts[0] != "exit"):
				print "Error en la ejecucion."

				if instrParts[0] in self.repertorio :
					print self.repertorio[instrParts[0]].help()
				else :
					print "La instruccion no existe"