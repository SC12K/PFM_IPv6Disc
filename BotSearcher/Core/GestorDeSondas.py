import sys
sys.path.append('../')
from SC12K_utils import *
from DispensadorIPv6 import DispensadorIPv6
from EjecutorSondeo import EjecutorSondeo
from Sonda import Sonda

class GestorDeSondas():
	def __init__(self):
		self._Sondas = dict()
		self._Dispensadores = dict()
		self._Ejecutores = dict()
		pass
	
	def anadirSonda(self, nombre, dispensadorIPv6, ejecutorSondeo):
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
		sonda.ejecutarPaso()
		
		return True
		
	def cargarDispensador(self,folder, modulename, disp):
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
	
	def cargarEjecutor(self,folder, modulename, disp):
		sobr = 'Y'
		if disp in self._Ejecutores:
			print "El ejecutor " + disp + " ya esta cargado."
			sobr = raw_input("Escriba 'Y' para sobrescribirlo")
		
		if sobr == 'Y':
			logging.info('cargarEjecutor Folder: ' + folder + ' Module ' + modulename + ' Ejecutor ' + disp)
			clase = cargarClase(folder, modulename, disp)
			if clase != None :
				self._Ejecutores[disp] = clase
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
				
	def checkEjec(self, DispClass):
		methods = dir(DispClass)
		if 'getResultInfo' in methods:
			return True
		else:
			return False
	
	
	def listarSondas(self):
		nameKeys = self._Sondas.viewkeys()
		print "---------------------------- Sondas --------------------------------"
		print "Nombre\t\t\tDispensadorIPv6\t\t\tSondeo"
		for key in nameKeys:
			print key + "\t\t\t" + self._Sondas[key].getNombreDispensador() + "\t\t\t" + self._Sondas[key].getNombreEjecutor()
		print "--------------------------------------------------------------------"
		
	def listarDispensadores(self):
		nameKeys = self._Dispensadores.viewkeys()
		print "------------------------- Dispensadores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
		
	def listarEjecutores(self):
		nameKeys = self._Ejecutores.viewkeys()
		print "--------------------------- Ejecutores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
	
	def eliminarSonda(self, id):
		pass
		
	def cargar(self):
		pass