from SC12K_utils import *
from EjecutorSondeo import EjecutorSondeo
import sys

from scapy.all import *

class Ping(EjecutorSondeo) :
	def init(self):
	  pass
		
	def ejecutarPaso(self, ipv6):
		print "Ejecutor: " + ipv6
		logging.debug('IP: ' + ipv6)
		if not self._inicializado:
			self._inicializado = True

		logging.debug("Configurando paquete IP...")
		ip_p = IP(src='10.0.2.15', dst=ipv6)
		logging.debug("Ejecutando")
		p = sr(ip_p/ICMP(), timeout=1)
		logging.debug("AnalizandoResultado")
		if p == None : 
		    logging.debug('No PC in ' + ipv6)
		else:
		    logging.debug('No PC in ' + ipv6)
		    
		return True
	
	def getResultInfo(self):
		pass
	