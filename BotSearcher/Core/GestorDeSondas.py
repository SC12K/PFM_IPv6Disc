import sys
sys.path.append('../')
from SC12K_utils import *
from DispensadorIPv6 import DispensadorIPv6
from EjecutorSondeo import EjecutorSondeo
from Sonda import Sonda
import xml.etree.ElementTree as xmlparser

class GestorDeSondas():
#--------------------------------------------------------------------------------------------------------
#-------------------------------------------- GESTOR DE SONDAS ------------------------------------------

	def __init__(self):
		self._Sondas = dict()
		self._Dispensadores = dict()
		self._Ejecutores = dict()
		pass
		
	def cargar(self, xmlfile):
		logging.info('Cargando modulos desde el fichero ' + xmlfile)
		#importar el fichero:
		self.tree = xmlparser.parse(xmlfile)
		root = self.tree.getroot()
		
		for xml_dispensador in root.findall('dispensador'):
			print 'Cargando dispensador ' + xml_dispensador.attrib['clase']
			if not self._cargarDispensador(xml_dispensador.attrib['folder'],xml_dispensador.attrib['modulo'],xml_dispensador.attrib['clase']):
				root.remove(xml_dispensador)
			
		for xml_ejecutor in root.findall('ejecutor'):
			print 'Cargando ejecutor ' + xml_ejecutor.attrib['clase']
			if not self._cargarEjecutor(xml_ejecutor.attrib['folder'],xml_ejecutor.attrib['modulo'],xml_ejecutor.attrib['clase']):
				root.remove(xml_ejecutor)
			
		for xml_sonda in root.findall('sonda'):
			print 'Creando sonda ' + xml_sonda.attrib['nombre']
			if not self._anadirSonda(xml_sonda.attrib['nombre'], xml_sonda.attrib['dispensador'], xml_sonda.attrib['ejecutor']):
				root.remove(xml_sonda)
			else:
				self._Sondas[xml_sonda.attrib['nombre']].cargarDesdeTree(xml_sonda)
			
	def	guardar(self):
		self.tree.write('modulos.xml')
	
	def listarParametros(self, sonda,doe):
		if sonda in self._Sondas:
			return self._Sondas[sonda].listParam(doe)
		return False
		
	def setParametro(self, sonda, doe, key, value):
		if sonda in self._Sondas:
			return self._Sondas[sonda].setParametro(doe, key, value)
		return False
#--------------------------------------------------------------------------------------------------------
#------------------------------------------------- SONDAS -----------------------------------------------
	def anadirSonda(self,nombre, dispensadorIPv6, ejecutorSondeo):
		result = self._anadirSonda(nombre, dispensadorIPv6, ejecutorSondeo)
		if result:
			if 'Y' == raw_input('Escriba Y para cargar siempre  '):
				attributes={'nombre' : nombre, 'dispensador': dispensadorIPv6, 'ejecutor' : ejecutorSondeo}
				elem = xmlparser.SubElement(self.tree.getroot(),"sonda", attrib=attributes)
				self._Sondas[nombre].newTreeRoot(elem)
		return result
	
	def _anadirSonda(self, nombre, dispensadorIPv6, ejecutorSondeo):
		if not (dispensadorIPv6 in self._Dispensadores):
			logging.warning("Dispensador IPv6 " + dispensadorIPv6 + " no existe")
			print "Dispensador IPv6 " + dispensadorIPv6 + " no existe"
			return False
			
		if not (ejecutorSondeo in self._Ejecutores):
			logging.warning("Ejecutor de Sondeo " + ejecutorSondeo + " no existe")
			print "Ejecutor de Sondeo " + ejecutorSondeo + " no existe"
			return False
			
		if nombre in self._Sondas:
			logging.warning("La sonda " + nombre + " ya existe")
			print "La sonda " + nombre + " ya existe"
			return False
			
		disp = self._Dispensadores[dispensadorIPv6]()
		ejec = self._Ejecutores[ejecutorSondeo]()
		sonda = Sonda(nombre, disp, ejec)
		self._Sondas[nombre] = sonda
		
		return True
		
	def listarSondas(self):
		nameKeys = self._Sondas.viewkeys()
		print "---------------------------- Sondas --------------------------------"
		print "Nombre\t\t\tDispensadorIPv6\t\t\tSondeo"
		for key in nameKeys:
			print key + "\t\t\t" + self._Sondas[key].getNombreDispensador() + "\t\t\t" + self._Sondas[key].getNombreEjecutor()
		print "--------------------------------------------------------------------"
			
	def eliminarSonda(self, nombre):
		if nombre in self._Sondas:
			del self._Sondas[nombre]
			root = self.tree.getroot()
			for sonda in root.findall("sonda"):
				if sonda.attrib['nombre'] == nombre:
					root.remove(sonda)
			return True
		else:
			print "No existe la sonda " + nombre
			return False

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------- DISPENSADORES --------------------------------------------			
	def cargarDispensador(self,folder, modulename, ejec):
		result = self._cargarDispensador(folder, modulename, ejec)
		if result:
			if 'Y' == raw_input('Escriba Y para cargar siempre  '):
				attributes={'folder' : folder, 'modulo': modulename, 'clase' : ejec}
				xmlparser.SubElement(self.tree.getroot(),"dispensador", attrib=attributes)
		return result
	
	def _cargarDispensador(self,folder, modulename, disp):
		sobr = 'Y'
		if disp in self._Dispensadores:
			print "El dispensador " + disp + " ya esta cargado."
			sobr = raw_input("Escriba 'Y' para sobrescribirlo")
		
		if sobr == 'Y':
			logging.info('cargarDispensador Folder: ' + folder + ' Module' + modulename + 'Dispensador ' + disp)
			clase = cargarClase(folder, modulename, disp)
			if clase != None :
				self._Dispensadores[disp] = clase
				if self.checkDisp(clase):
					logging.info('\tOk')
					print "Cargado"
					return True
				else:
					logging.warning('\tLa clase no coincide con el patron. ' + str(dir(clase)))
					print "Error: La clase no coincide con el patron."
					return False
			else :
				logging.warning('\tError al abrir el archivo')
				print "Error: Error al abrir el archivo"
				return False
		else:
			return True
	
	def checkDisp(self, DispClass):
		methods = dir(DispClass)
		if 'getDireccionIPv6' in methods:
			return True
		else:
			return False
	
	def listarDispensadores(self):
		nameKeys = self._Dispensadores.viewkeys()
		print "------------------------- Dispensadores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
	
	def eliminarDispensador(self, nombre):
		if nombre in self._Dispensadores:
			del self._Dispensadores[nombre]
			root = self.tree.getroot()
			for disp in root.findall("dispensador"):
				if disp.attrib['clase'] == nombre:
					root.remove(disp)
			return True
		else:
			print "No existe el dispensador " + nombre
			return False

#--------------------------------------------------------------------------------------------------------
#----------------------------------------------- EJECUTORES ---------------------------------------------				
	def cargarEjecutor(self,folder, modulename, ejec):
		result = self._cargarEjecutor(folder, modulename, ejec)
		if result:
			if 'Y' == raw_input('Escriba Y para cargar siempre  '):
				attributes={'folder' : folder, 'modulo': modulename, 'clase' : ejec}
				xmlparser.SubElement(self.tree.getroot(),"ejecutor", attrib=attributes)
		return result
		
	def _cargarEjecutor(self,folder, modulename, ejec):
		sobr = 'Y'
		if ejec in self._Ejecutores:
			print "El ejecutor " + ejec + " ya esta cargado."
			sobr = raw_input("Escriba 'Y' para sobrescribirlo")
		
		if sobr == 'Y':
			logging.info('cargarEjecutor Folder: ' + folder + ' Module ' + modulename + ' Ejecutor ' + ejec)
			clase = cargarClase(folder, modulename, ejec)
			if clase != None :
				self._Ejecutores[ejec] = clase
				if self.checkEjec(clase):
					logging.info('\tOk')
					print "Cargado"
					return True
				else:
					logging.warning('\tLa clase no coincide con el patron.' + str(dir(clase)))
					print "Error: La clase no coincide con el patron."		
					return False
			else :
				logging.warning('\tError al abrir el archivo')
				print "Error: Error al abrir el archivo"
				return False
		else:
			return True
				
	def checkEjec(self, EjecClass):
		methods = dir(EjecClass)
		if 'getResultInfo' in methods:
			return True
		else:
			return False
		
	def listarEjecutores(self):
		nameKeys = self._Ejecutores.viewkeys()
		print "--------------------------- Ejecutores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
	
	def eliminarEjecutor(self, nombre):
		if nombre in self._Ejecutores:
			del self._Ejecutores[nombre]
			root = self.tree.getroot()
			for ejec in root.findall("ejecutor"):
				if ejec.attrib['clase'] == nombre:
					root.remove(ejec)
			return True
		else:
			print "No existe el ejecutor " + nombre
			return False