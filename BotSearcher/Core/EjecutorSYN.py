from SC12K_utils import *
from EjecutorSondeo import EjecutorSondeo
import sys

from scapy.all import *

class EjecutorSYN(EjecutorSondeo) :
	def init(self):
		self._atributos['Ports'] = "80, 20-22,100-120"
	pass
		
	def ejecutarPaso(self, ipv6):
		print "Ejecutor: " + ipv6
		logging.debug('IP: ' + ipv6)
		logging.debug(self._inicializado)
		if not self._inicializado:
		    portIntervals=map(lambda x: x.split('-'), self._atributos['Ports'].split(','))
		    logging.debug('Ports: ' + str(portIntervals))
		    self._inicializado
		
		ip_p = IP(src='10.0.2.15', dst=ipv6)
		for i in range(len(portIntervals)):
		  current = portIntervals[i]
		  if len(current) == 1:
		    p = sr1(ip_p/TCP(dport=int(current[0]), flags="S"), timeout=3)
		  else:
		    p = sr1(ip_p/TCP(dport=(int(current[0]),int(current[1])), flags="S"), timeout=3)
		    
		return True
	
	def getResultInfo():
		pass
	