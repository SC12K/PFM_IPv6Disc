import Instruccion
from SC12K_utils import printD
import xml.etree.ElementTree as xmlparser

import importlib as il

class Interprete :
	
	class Ayuda(Instruccion.Instruccion):
		def init(self):
			self.name = "Ayuda"
		
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
			res = "BotSearcherIPv6 te ayuda a ejecutar diferentes escaners programados y\n"
			res +="centralizar la información.\n"
			res +="utiliza 'ayuda <comando>' para ver la ayuda de un comando."
			return res
		
	
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
		
	
	def ejecInstr(self, instr, params) :
		printD(self.repertorio.keys)
		if instr in self.repertorio :
			#separar parametros de instruccion
			return self.repertorio[instr].run(params,self)
		else :
			return False

	def cargarInstruccion(self, path, modulename, classname):
		if (path != "" and path != "./"):
			sys.path.append(path)
		module = __import__(modulename)
		class_ = getattr(module, classname)
		instance = class_()
		return instance
	
	def cargarRepertorio(self, xmlfile) :
		instruccion = self.Ayuda()
		self.repertorio[instruccion.name]= instruccion
		
		#importar el fichero:
		tree = xmlparser.parse(xmlfile)
		root = tree.getroot()
		for child in root:
			instruccion = self.cargarInstruccion(child.attrib['path'], child.attrib['modulo'], child.attrib['nombre'])
			self.repertorio[instruccion.name]= instruccion
		
		
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
				if instrParts[0] == 'Ayuda':
					for instrName in self.repertorio.viewkeys():
						print "\t*  " + instrName
			else : 
				execu = self.ejecInstr(instrParts[0], instrParts[1])
				
			if(not execu and instrParts[0] != "Exit"):
				print "Error en la ejecucion."

				if instrParts[0] in self.repertorio :
					print self.repertorio[instrParts[0]].help()
				else :
					print "La instruccion no existe. Usa 'Ayuda'"