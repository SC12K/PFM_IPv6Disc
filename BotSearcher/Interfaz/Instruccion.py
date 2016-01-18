import sys
sys.path.append('../')
from SC12K_utils import *

class Instruccion :
    """
    Clase base para todas las instrucciones ejecutables, excepto Exit.
    """
    def __init__(self):
	"""
        B{Este metodo no puede ser sobrescrito.} Ejecuta la inicializacion de 
        init()
        """
        self.init()

    def init(self):
        """
        B{Este metodo debe ser sobrescrito.} Es la inicializacion de la 
        instruccion. Como minimo se debe establecer el parametro B{name}.
        """
        logging.error(self.__class__.__name__ + ' : init: Metodo no implementado implementado!')
        self.name = ""
        """
        El parametro name indica el nombre de la instruccion.
        """

    def run(self, params, interprete):
        """
        B{Este metodo debe ser sobrescrito.} Es el cuerpo de ejecucion de la
        instruccion.
        @param params: Los parametros que se reciben del interprete. Es una
        cadena de texto que debe ser tratada en el metodo run() de la
        instruccion.
        @type params: string de parametros
        
        @param interprete: los comandos pueden hacer uso de algunas funciones del interprete.
        @type interprete: tipo Interprete
        """
        logging.error(self.__class__.__name__ + ' : run Metodo no implementado implementado!')
        return False

    def help(self):
        """
        B{Este metodo debe ser sobrescrito.} Devuelve el texto de Ayuda de la 
        instruccion.
        """
        logging.error(self.__class__.__name__ + ' : help Metodo no implementado implementado!')
        return None