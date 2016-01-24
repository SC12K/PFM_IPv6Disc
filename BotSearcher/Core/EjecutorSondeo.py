from logger import *
from SC12KModulo import SC12KModulo

class EjecutorSondeo(SC12KModulo):
    """
    Modelo para modulos que implementen algun tipo de rastreo sobre 1 direccion
    IPv6.
    Estos modulos deben generar resultados compatibles con el almacen de
    informacion centralizada.
    
    Cada implementacion debe reimplementar los metedos:
    init(), inicializa(), ejecutarPaso(), getResultInfo()
    """
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
        logging.error(self.__class__.__name__ + ': ejecutarPaso: Metodo no \
                      implementado implementado!')
        return False

    def ejecutarPaso(self, ipv6):
        """
        B{Este metodo debe ser sobrescrito.} Metodo que debe implementar un 
        rastreo sobre una IP dada y generar unos resultados.
        
        @param ipv6: Reperesentacion de una direccion IPv6 de la forma
        2001:0000:0000:0000:0000:0000:0000:0000
        @type ipv6: string
        
        @return:
            - Cierto si el rastreo ha sido correcto.
            - Falso si se ha producido un error.
        @rtype: boolean
        """
        logging.error(self.__class__.__name__ + ': ejecutarPaso: Metodo no \
                      implementado implementado!')
        return False

    def getResultInfo(self):
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
        logging.error(self.__class__.__name__ + ': getResultInfo: Metodo no \
                      implementado implementado!')