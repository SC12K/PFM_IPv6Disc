from logger import *
from EjecutorSondeo import EjecutorSondeo

from scapy.all import IP, ICMP, sr

class Ping(EjecutorSondeo) :
    def init(self):
        """
        Inicializa los parametros configurables:
            
            - Timeout : Tiempo de espera para recibir un mensaje.
        """
        pass

    def inicializa(self):
        """
        No hace falta inicializacion del algoritmo.
        
        @return:
            - Cierto siempre.
        @rtype: boolean
        """
        
        return True

    def ejecutarPaso(self, ipv6):
        """
        Implementa un rastreo de tipo PING.
        
        @param ipv6: Reperesentacion de una direccion IPv6 de la forma
        2001:0000:0000:0000:0000:0000:0000:0000
        @type ipv6: string
        
        @return: Devuelve Cierto si ha ido correcto.
        @rtype: boolean
        """
        print "Ejecutor: " + ipv6
        logging.debug('IP: ' + ipv6)
        if not self._inicializado:
            self._inicializado = True

        logging.debug("Configurando paquete IP...")
        ip_p = IP(src='10.0.2.15', dst=ipv6)
        logging.debug("Ejecutando")
        p = sr(ip_p/ICMP(), timeout=2)
        logging.debug("AnalizandoResultado")
        if p == None : 
            logging.debug('No PC in ' + ipv6)
        else:
            logging.debug('No PC in ' + ipv6)

        return True

    def getResultInfo(self):
        """
        Metodo por implementar a falta de saber como sera la comunicacion 
        """
        pass