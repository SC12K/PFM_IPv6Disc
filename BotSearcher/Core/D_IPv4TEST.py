import sys
sys.path.append('../')
from SC12K_utils import *
from DispensadorIPv6 import DispensadorIPv6
from struct import unpack
from socket import AF_INET, inet_aton


class D_IPv4TEST(DispensadorIPv6):
    """
    Implementacion de un DispensadorIPv6 que genera direcciones IPv4 para
    realizar tests en local. Al ser de TEST no se comentan los metodos.
    """
    def init(self):
        logging.debug(self.__class__.__name__ + ': inicializa()')
        self._atributos["ipv4Ini"] = "0.0.0.0"

    def inicializa(self):
        logging.debug(self.__class__.__name__ + ': inicializa()')
        ipv4p = self._atributos["ipv4Ini"].split('.')
        self._dirInts = [int(ipv4p[0]),int(ipv4p[1]),int(ipv4p[2]),\
                         int(ipv4p[3])]
        return True

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
        ipv4 = self.getDireccionIPv4String()
        self.incrementarIPv4()
        return ipv4