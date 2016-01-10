#Devuelve la direccion IPv6 a partir de una direccion IPv4.
#Recorre el espectro de forma secuencial.
from DispensadorIPv6 import DispensadorIPv6
from struct import unpack
from socket import AF_INET, inet_aton


class D_IPv4MappedIPv6(DispensadorIPv6) :
	def __init__(self):
		self._name = "hello"
		self._dirInts = [0,0,0,0]
	
	def esPrivada(self, ip):
		ip_rep = unpack('!I',inet_aton(ip))[0]
		redesPrivadas = (
			[ 2130706432, 4278190080 ], # 127.0.0.0,   255.0.0.0
			[ 3232235520, 4294901760 ], # 192.168.0.0, 255.255.0.0
			[ 2886729728, 4293918720 ], # 172.16.0.0,  255.240.0.0
			[ 167772160,  4278190080 ], # 10.0.0.0,    255.0.0.0
		) 
		for red in redesPrivadas:
			if (ip_rep & red[1]) == red[0]:
				return True
		return False
	
	def getDireccionIPv4String(self):
		if self._dirInts[0] > 255:
			return ""
		else:
			ipv4_rep = ""
			for i in self._dirInts:
				ipv4_rep = ipv4_rep + format(i) + "."
					
			return ipv4_rep[:-1]
			
	def incrementarIPv4(self):
		self._dirInts[3] = self._dirInts[3] + 1
		
		if self._dirInts[3] > 255:
			self._dirInts[3] = 0
			self._dirInts[2] = self._dirInts[2] + 1
			
		if self._dirInts[2] > 255:
			self._dirInts[2] = 0
			self._dirInts[1] = self._dirInts[1] + 1
			
		if self._dirInts[1] > 255:
			self._dirInts[1] = 0
			self._dirInts[0] = self._dirInts[0] + 1
	
	def getDireccionIPv6(self):
		
		while self.esPrivada(self.getDireccionIPv4String()):
			incrementarIPv4()
		
		ipv6 = ""
		if self.getDireccionIPv4String() != "":
			ipv6 = "::ffff:"
			for i in range(4):
				hex_rep = format(self._dirInts[i],'x')
				if len(hex_rep) == 1:
					hex_rep = '0' + hex_rep
					
				ipv6 += hex_rep
				
				if i == 1:
					ipv6+=":"
				
		return ipv6
	
	def setParametro(self, key, value):
		if key == "name":
			self._name = name

	def getParamValue(self, key):
		val = ""
		if key == "name":
			val = self._name
			
		return val