from logger import *
from SC12KModulo import SC12KModulo

class DispensadorIPv6(SC12KModulo):
    """
    Modelo para modulos que proporcionen direcciones IPv6. Estos modulos se
    encargan de implementar algoritmos para generar direcciones IPv6 para el
    rastreo, o bien conseguir estas direcciones de un fichero o una base de
    datos.
    
    Cada implementacion debe reimplementar los metedos:
    init(), inicializa(), getDireccionIPv6()
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
        logging.error(self.__class__.__name__ + ': getDireccionIPv6: Metodo no\
                      implementado implementado!')
        return False
    
    def getDireccionIPv6(self):
        """
        B{Este metodo debe ser sobrescrito.} Funcion que debe impementar el
        algoritmo que genera direccioens IPv6.
        Este metodo debe generar direcciones IPv6 diferentes cada vez que se 
        llame. Sera el metodo usado para iterar generando direcciones.
        
        Se recomienda el uso de self._inicializado para la inicializacion
        del algoritmo en la primera iteracion.

        @return:
            - DireccionIPv6
            - "" Fin del algoritmo.
        @rtype: string
        """
        logging.error(self.__class__.__name__ + ': getDireccionIPv6: Metodo no\
                      implementado implementado!')
        return ""