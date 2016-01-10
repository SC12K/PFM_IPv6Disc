from DispensadorIPv6 import DispensadorIPv6

class D_IPv4MappedIPv6(DispensadorIPv6) :
	def __init__(self):
		self._name = "hello"
	
	def getDireccionIPv6(self):
		return "FF80::1"
	
	def setParametro(self, key, value):
		if key == "name":
			self._name = name

	def getParamValue(self, key):
		val = ""
		if key == "name":
			val = self._name
			
		return val