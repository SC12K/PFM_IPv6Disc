import xml.etree.ElementTree as xmlparser
from SC12K_utils import logging

class Sonda:
	def __init__(self, nombre, dispensador, ejecutor):
		self.id = 0
		self._dispensador = dispensador
		self._ejecutor = ejecutor
		self._name = nombre
		self._treeroot = None
		
	def ejecutarPaso(self):
		logging.debug("sonda.ejecutarPaso")
		ipv6 = self._dispensador.getDireccionIPv6()
		logging.debug("IPv6: " + ipv6)
		self._ejecutor.ejecutarPaso(ipv6)
		logging.debug("finEjecucion")
		
	def getResultInfo(self):
		return "Algo"
		
	def newTreeRoot(self, tree):
		logging.debug('Sonda newTreeRoot')
		self._treeroot = tree
		#añade parametros dispensador
		idisp = xmlparser.SubElement(self._treeroot,"idisp")
		keylist = self._dispensador.getParamList()
		for key in keylist:
			idisp.set(key, self._dispensador.getParamValue(key))
		
		iejec = xmlparser.SubElement(self._treeroot,"iejec")
		keylist = self._ejecutor.getParamList()
		for key in keylist:
			iejec.set(key, self._ejecutor.getParamValue(key))
			
	def cargarDesdeTree(self, tree):
		logging.debug('Sonda cargarDesdeTree')
		idisp = tree.find('idisp')
		self._dispensador.cargarDesdeTree(idisp)
		
		iejec = tree.find('iejec')
		self._ejecutor.cargarDesdeTree(iejec)
		self._treeroot = tree
			
	
	def setName(self, name):
		logging.debug('Sonda setName')
		self._name = name
		
	def setParametro(self,deo, key, value):
		logging.debug('Sonda setParam')
		if deo:
			#si cierto dispensador
			logging.debug('\tdispensador')
			res = self._dispensador.setParametro(key,value)
			if res and not self._treeroot == None:
				self._treeroot.find('idisp').attrib[key] = value
				
		else:
			#si falso ejecutor
			logging.debug('\tejecutor')
			res = self._ejecutor.setParametro(key,value)
			if res and not self._treeroot == None:
				self._treeroot.find('iejec').attrib[key] = value
		return res
		
	def listParam(self,deo):
		logging.debug('Sonda setParam')
		if deo:
			#si cierto dispensador
			logging.debug('\tdispensador')
			print 'Dispensador: ' + self.getNombreDispensador()
			mod = self._dispensador
		else:
			#si falso ejecutor
			logging.debug('\tejecutor')
			print 'Ejecutor: ' + self.getNombreEjecutor()
			mod = self._ejecutor
			
		print 'Parametros: '
		keylist = mod.getParamList()
		for i in keylist:
			print '\t* ' + i + "\t= " + mod.getParamValue(i)
		
		return True 
	
	def getName(self):
		return self._name
		
	def getNombreDispensador(self):
		return self._dispensador.__class__.__name__
		
	def getNombreEjecutor(self):
		return self._ejecutor.__class__.__name__