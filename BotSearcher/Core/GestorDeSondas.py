import sys
sys.path.append('../')
from SC12K_utils import *
from DispensadorIPv6 import DispensadorIPv6
from EjecutorSondeo import EjecutorSondeo

class GestorDeSondas():
	def __init__(self):
		self._Sondas = dict()
		self._Dispensadores = dict()
		self._Ejecutor = dict()
		pass
	
	def anadirSonda(self, dispensadorIPv6, ejecutorSondeo):
		pass
		
	def cargarDispensador(self,folder, modulename, disp):
		if disp in self._Dispensadores:
			print "El dispensador " + disp + " ya esta cargado."
		else:
			printD("Fold " + folder)
			printD("Mod " + modulename)
			printD("Dips " + disp)
			clase = cargarClase(folder, modulename, disp)
			if clase != None :
				printD(dir(clase))
				self._Dispensadores[disp] = clase
				if self.checkDisp(clase):
					return True
				else:
					return False
			else :
				return False
	
	def checkDisp(self, DispClass):
		methods = dir(DispClass)
		if 'getDireccionIPv6' in methods:
			return True
		else:
			return False
	
	def cargarEjecutor(self,folder, modulename, disp):
		if disp in self._Ejecutor:
			print "El ejecutor " + disp + " ya esta cargado."
		else:
			printD("Fold " + folder)
			printD("Mod " + modulename)
			printD("Dips " + disp)
			clase = cargarClase(folder, modulename, disp)
			if clase != None :
				printD(dir(clase))
				self._Ejecutor[disp] = clase
				if self.checkEjec(clase):
					return True
				else:
					return False
			else :
				return False
				
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
			print "Sonda1\t\tIPv4discover\t\tSYN"
		print "--------------------------------------------------------------------"
		
	def listarDispensadores(self):
		nameKeys = self._Dispensadores.viewkeys()
		print "------------------------- Dispensadores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
		
	def listarEjecutores(self):
		nameKeys = self._Ejecutor.viewkeys()
		print "--------------------------- Ejecutores ----------------------------"
		print "  Nombre\t\t\t\tParametros"
		for key in nameKeys:
			print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
		print "--------------------------------------------------------------------"
	
	def eliminarSonda(self, id):
		pass
		
	def cargar(self):
		pass