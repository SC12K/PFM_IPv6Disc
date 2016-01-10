import sys
sys.path.append('../')
import SC12K_utils
from SC12K_utils import *
import Instruccion
import xml.etree.ElementTree as xmlparser

class Interprete :
	
	class Ayuda(Instruccion.Instruccion):
		def init(self):
			self.name = "Ayuda"
		
		def run(self, params, interprete):
			if (params == None) :
				res = self.help()
				print res
			else :
				res = interprete.ejecHelp(params)
				print res

			return True
			
		def help(self):
			res = "BotSearcherIPv6 te ayuda a ejecutar diferentes escaners programados y\n"
			res +="centralizar la información.\n"
			res +="utiliza 'ayuda <comando>' para ver la ayuda de un comando."
			return res
		
	
	def __init__(self):
		logging.info('Abriendo interprete...')
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
		logging.debug('ejecInstr repo keys: ' + str(self.repertorio.viewkeys()))
		if instr in self.repertorio :
			#separar parametros de instruccion
			return self.repertorio[instr].run(params,self)
		else :
			return False

	def cargarInstruccion(self, path, modulename, classname):
		clase = cargarClase(path, modulename, classname)
		logging.debug('cargarInstruccion atributos y funciones de ' + classname + ' : ' + str(dir(clase)))
		if clase == None:
			return None
		if not self.checkInstr(clase):
			return None
		instancia = clase()
		return instancia
	
		
	def checkInstr(self, InstrClass) :
		methods = dir(InstrClass)
		if 'run' in methods and 'help' in methods:
			return True
		else:
			return False
	
	def cargarRepertorio(self, xmlfile) :
		instruccion = self.Ayuda()
		self.repertorio[instruccion.name]= instruccion
		
		#importar el fichero:
		tree = xmlparser.parse(xmlfile)
		root = tree.getroot()
		for child in root:
			logging.info('Cargando instruccion: ' + child.attrib['path'] +" "+ child.attrib['modulo'] +" "+ child.attrib['nombre'])
			instruccion = self.cargarInstruccion(child.attrib['path'], child.attrib['modulo'], child.attrib['nombre'])
			if instruccion != None:
				self.repertorio[instruccion.name]= instruccion
		
		
	def ejecHelp(self, instr) :
		if instr in self.repertorio :
			return self.repertorio[instr].help()
		else :
			return "La instruccion no existe"
		
		
	def ejecutarBucle(self) :
		instr = ''
		while instr != "Exit":
		
			instr = raw_input('$>>')
			logging.info('Instruccion introducida: ' + instr)
			
			instrParts = instr.split(' ', 1)
			
			if len(instrParts) != 2 :
				logging.info('\tNo contiene parametros')
				execu = self.ejecInstr(instrParts[0], None)
				if instrParts[0] == 'Ayuda':
					for instrName in self.repertorio.viewkeys():
						print "\t*  " + instrName
					print "\t*  Exit"
			else : 
				logging.info('\tContiene parametros')
				execu = self.ejecInstr(instrParts[0], instrParts[1])
				
			if(not execu and instrParts[0] != "Exit"):
				logging.warning('\tError de ejecucion')
				print "Error en la ejecucion."

				if instrParts[0] in self.repertorio :
					logging.warning('\tLa instruccion existe.')
					print self.repertorio[instrParts[0]].help()
				else :
					logging.warning('\tLa instruccion no existe.')
					print "La instruccion no existe. Usa 'Ayuda'"