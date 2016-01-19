from SC12K_utils import *

class EjecutorSondeo(object):

    def __init__(self):
        self.binit()
        self.init()

    def binit(self): 
        self._atributos = dict()
        self._inicializado = False

    def init(self):
        logging.error(self.__class__.__name__ + ': init: Metodo no implementado\
                      implementado!')

    def ejecutarPaso(self):
        logging.error(self.__class__.__name__ + ': ejecutarPaso: Metodo no \
                      implementado implementado!')
        return False

    def getResultInfo(self):
        logging.error(self.__class__.__name__ + ': getResultInfo: Metodo no \
                      implementado implementado!')

    def setParametro(self, key, value):
        if key in self._atributos:
            self._atributos[key] = str(value)

    def getParamValue(self, key):
        if key in self._atributos:
            return self._atributos[key]

        return None

    def getParamList(self):
        return self._atributos.keys()
      
    def cargarDesdeTree(self, tree):
        logging.debug('EjecutorSondeo cargarDesdeTree')
        for attr in tree.attrib:
            logging.debug('Attr completo ' + attr)
            logging.debug('\tAttr --> ' + attr[0] + " : " + attr[1])
            if attr[0] in self._atributos:
                self._atributos[attr[0]] = attr[1]