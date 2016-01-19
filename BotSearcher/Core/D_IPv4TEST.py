import sys
sys.path.append('../')
from DispensadorIPv6 import DispensadorIPv6
from struct import unpack
from socket import AF_INET, inet_aton


class D_IPv4TEST(DispensadorIPv6):

    def init(self):
        self._atributos["ipv4Ini"] = "0.0.0.0"

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
        if not self._inicializado:
            ipv4p = self._atributos["ipv4Ini"].split('.')
            self._dirInts = [int(ipv4p[0]),int(ipv4p[1]),int(ipv4p[2]),\
                             int(ipv4p[3])]
            self._inicializado = True

        ipv4 = self.getDireccionIPv4String()
        self.incrementarIPv4()
        return ipv4