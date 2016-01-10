import sys
sys.path.append('../')
from SC12K_utils import *

class DispensadorIPv6() :
	def __init__(self):
		self.init()
		
	def init():
		logging.error(self.__class__.__name__ + ' : init: Metodo no implementado implementado!')
	
	def getDireccionIPv6():
		logging.error(self.__class__.__name__ + ' : getDireccionIPv6: Metodo no implementado implementado!')
		return ""
	
	def setParametro(key, value):
		logging.error(self.__class__.__name__ + ' : setParametro: Metodo no implementado implementado!')
		if key == "name":
			self._name = name

	def getParamValue(key):
		logging.error(self.__class__.__name__ + ' : getParamValue: Metodo no implementado implementado!')
		val = ""
		if key == "name":
			val = self._name
			
		return val