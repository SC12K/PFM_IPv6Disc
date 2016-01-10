
class Sonda:
	def __init__(self, nombre, dispensador, ejecutor):
		self.id = 0
		self._dispensador = dispensador
		self._ejecutor = ejecutor
		self._name = nombre
		
	def ejecutarPaso(self):
		self._ejecutor.ejecutarPaso(self._dispensador.getDireccionIPv6())
		
	def getResultInfo(self):
		pass
	
	def setName(self, name):
		self._name = name
	
	def getName(self):
		return self._name
		
	def getNombreDispensador(self):
		return self._dispensador.__class__.__name__
		
	def getNombreEjecutor(self):
		return self._ejecutor.__class__.__name__