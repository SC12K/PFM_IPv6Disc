from logger import *
from EjecutorSondeo import EjecutorSondeo
import sys

from scapy.all import IP, TCP, sr1

class EjecutorSYN(EjecutorSondeo) :
    """
    Implementacion de un rastreo de tipo SYN.
    """
    def init(self):
        """
        Inicializa los parametros configurables:
            
            - Ports : Puerto o puertos a rastrar. Se pueden indica los
                puertos individualmente, separados por comas (80, 81, 82) o
                bien hacerlo en rango (80-82), o combinando ambos.
            - Timeout : Tiempo de espera para recibir un mensaje.
        """
        self._atributos['Ports'] = "80, 20-22,100-120"

    def inicializa(self):
        """
        B{Este metodo debe ser sobrescrito.} Metodo que debe implementar la 
        inicializacion del algortimo, usando los prametros del diccionario
        _atributos.
        
        Si no es necesario inicializacion alguna, debe ser reimplementado
        devolviendo Cierto.
        
        @return:
            - Cierto si la inicializacion ha sido correcta.
            - Falso en otro caso.
        @rtype: boolean
        """
        self._portIntervals=map(lambda x: x.split('-'), self._atributos['Ports'].\
                          split(','))
        logging.debug('Ports: ' + str(self._portIntervals))
        
        return True

    def ejecutarPaso(self, ipv6):
        """
        Implementa un rastreo SYN de los puertos indicados en la variable Ports.
        
        @param ipv6: Reperesentacion de una direccion IPv6 de la forma
        2001:0000:0000:0000:0000:0000:0000:0000
        @type ipv6: string
        
        @return: Devuelve Cierto si ha ido correcto.
        @rtype: boolean
        """
        print "Ejecutor: " + ipv6
        logging.debug('IP: ' + ipv6)
        logging.debug(self._inicializado)
        
        ip_p = IP(src='10.0.2.15', dst=ipv6)
        for i in range(len(self._portIntervals)):
            current = self._portIntervals[i]
            if len(current) == 1:
                p = sr1(ip_p/TCP(dport=int(current[0]), flags="S"), timeout=3)
            else:
                p = sr1(ip_p/TCP(dport=(int(current[0]),int(current[1])),\
                        flags="S"), timeout=3)
        return True

    def getResultInfo(self):
        """
        Metodo por implementar a falta de saber como sera la comunicacion 
        """
        pass