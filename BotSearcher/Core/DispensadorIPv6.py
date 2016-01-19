import sys
sys.path.append('../')
from SC12K_utils import *

class DispensadorIPv6(object):

    def __init__(self):
        logging.debug('DispensadorIPv6 __init__')
        self.binit()
        self.init()

    def binit(self):
        logging.debug('DispensadorIPv6 binit')
        self._atributos = dict()
        self._inicializado = False

    def init(self):
        logging.error(self.__class__.__name__ + ': init: Metodo no implementado\
                      implementado!')


    def getDireccionIPv6(self):
        logging.error(self.__class__.__name__ + ': getDireccionIPv6: Metodo no\
                      implementado implementado!')
        return ""

    def setParametro(self, key, value):
        logging.debug('DispensadorIPv6 setParametro')
        if key in self._atributos:
            self._atributos[key] = str(value)
            return True
        return False

    def getParamValue(self, key):
        logging.debug('DispensadorIPv6 getParamValue')
        if key in self._atributos:
            return self._atributos[key]

        return None

    def getParamList(self):
        logging.debug('DispensadorIPv6 getParamList')
        return self._atributos.keys()

    def cargarDesdeTree(self, tree):
        logging.debug('DispensadorIPv6 cargarDesdeTree')
        dellist = []
        for attr in tree.attrib:
            logging.debug('\tAttr --> ' + attr + " : " + tree.attrib[attr])
            if attr in self._atributos:
                self._atributos[attr] = tree.attrib[attr]
            else:
                dellist = dellist +  [attr]

        for attr in dellist:
            del tree.attrib[attr]
