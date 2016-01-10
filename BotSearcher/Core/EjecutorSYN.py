from EjecutorSondeo import EjecutorSondeo

class EjecutorSYN(EjecutorSondeo) :
	def __init__(self):
		pass
		
	def ejecutarPaso(self, ipv6):
		print "Ejecutor: " + ipv6
		return True
	
	def setParametro(key, value):
		if key == "name":
			self_name = name
		else:
			return False
		return True
	
	def getResultInfo():
		pass
	
	def getParamValue(key):
		val = ""
		if key == "name":
			val = self._name
		return val