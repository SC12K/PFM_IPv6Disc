import sys
sys.path.append('../')
from DispensadorIPv6 import DispensadorIPv6
from struct import unpack
from socket import AF_INET, inet_aton


class D_IPv4MappedIPv6(DispensadorIPv6) :
    """
    Implementacion de un DispensadorIPv6 que genera direcciones IPv4-Mapped
    IPv6. Genera las direcciones de forma secuencial desde una direccion
    inicial.
    """
    def init(self):
        """
        Inicializa los parametros configurables:
            
            - ipv4Ini : Indica la IPv4 inicial, de la forma 0.0.0.0
        """
        self._atributos["ipv4Ini"] = "0.0.0.0"

    def esPrivada(self, ip):
        """
        Comprueba si una IPv4 esta en uno de los rangos privados de este
        protocolo.
        
        @param ip: IPv4 de la forma 0.0.0.0
        @type ip: string
        
        @return: Cierto si la IP esta en un rango privado, Falso en otro caso.
        @rtype: boolean
        """
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

    def inicializa():
        """
        Inicializa la IPv4 numerica con la direccion IPv4Ini establecida como
        parametro.
        
        @return: Cierto si se genera correctamente.
        @rtype: boolean
        """
        ipv4p = self._atributos["ipv4Ini"].split('.')
        self._dirInts = [int(ipv4p[0]),int(ipv4p[1]),int(ipv4p[2]),\
                         int(ipv4p[3])]
        return True
      
    def getDireccionIPv4String(self):
        """
        Convierte la direccion IPv4 numerica interna en un string de tipo
        0.0.0.0
        
        @return: IPv4 de la forma 0.0.0.0 en formato texto.
        """
        if self._dirInts[0] > 255:
            return ""
        else:
            ipv4_rep = ""
            for i in self._dirInts:
                ipv4_rep = ipv4_rep + format(i) + "."
                
        return ipv4_rep[:-1]

    def incrementarIPv4(self):
        """
        Incrementa la direccion IPv4 numerica interna.
        
        Cuando el digito de menor peso llega a 255 se pone a 0 y actualiza el 
        digito posterior.
        De esta forma, cuando se llega al limite, la direccion dada sera
        256.0.0.0 esto indicara que se ha recorrido todo el rango.
        """
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
        """
        Devuelve una direccion IPv4-Mapped IPv6 a partir de una IPv4 dada.
        
        Recorre el rango desde una IPv4 inicial hasta 255.255.255.255, evitando
        las IPv4 privadas.
        """
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