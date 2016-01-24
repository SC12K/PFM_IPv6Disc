from logger import *
from SC12KModulo import SC12KModulo
from InfoResultados import InfoResultados

class Escritor(SC12KModulo):
    """
    Modelo para la implementacion de modulos que gestionen la escritura de
    resultados en diferentes formatos.
    
    Cada implementacion debe reimplementar los metedos:
    allimentar(InfoResultados)
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
      
    def alimentar(infoResultados):
        """
        B{Este metodo debe ser sobrescrito.} Funcion que implementa el algoritmo
        de escritura que se quiere usar.
        Recibira informacion en formato infoResultados y la tendra que adaptar
        a su propio formato y almacenarla para ser escrita o escribirla
        directamente.
        """
        logging.error(self.__class__.__name__ + ': getDireccionIPv6: Metodo no\
                      implementado implementado!')