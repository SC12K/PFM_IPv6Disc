from logger import *

class SC12KModulo(object):
    """
    Plantilla basica para los modelos de los modulos dispensadores, 
    ejecutores y escritores..
    """
    def __init__(self):
        """
        B{Este metodo no puede ser sobrescrito.} Ejecuta la inicializacion de 
        del modulo. Una inicializacion interna (_init()) y la
        inicializacion de los parametros que se podran utilizar a traves de 
        _atributos.
        """
        self._init()
        self.init()

    def _init(self):
        """
        B{Este metodo no puede ser sobrescrito.} Inicializacion de _atributos e
        indicando que no ha sido _inicializado.
        Despues de modificar los parametros. Nuestro proceso se inicializara
        con los nuevos parametros automaticamente a traves del metodo
        inicializaAlgoritmo()
        """
        self._atributos = dict()
        self._inicializado = False

    def init(self):
        """
        B{Este metodo debe ser sobrescrito.} Es la inicializacion del 
        modulo. Debe anadir como minimo la lista de parametros al
        diccionario self._atributos.
        
        Es una Inicializacion inicial, se debe tener en cuenta que
        posteriormente se modificaran los atributos y se ejecutara
        inicializa antes de la primera vuelta de ejecucion.
        """
        logging.error(self.__class__.__name__ + ': init: Metodo no implementado\
                      implementado!')    
            
    def reinicializa(self):
        """
        B{Este metodo no puede ser sobrescrito.} Metodo que utiliza
        inicializa y lo marca como inicializado si es correcto.
        
        @return:
            - Cierto si la inicializacion ha sido correcta.
            - Falso en otro caso.
        @rtype: boolean
        """
        self._inicializado = self.inicializa()
        
        return self._inicializado
      
    def estaInicializado(self):
        """
        B{Este metodo no puede ser sobrescrito.} Comprueba si el modulo esta
        inicializado.
        
        @return:
            - Cierto si esta inicializado.
            - Falso en otro caso.
        @rtype: boolean
        """
        return self._inicializado
        
    def setParametro(self, key, value):
        """
        B{Este metodo no puede ser sobrescrito.} Establece el valor de una
        clave con el valor dado. 
        
        @param key: Clave del diccionario de _atributos. Debe estar previamente
        inicializada en init().
        @type key: string

        @param value: Valor que se quiere dar al atributo con nombre <key>
        @type value: all
        
        @return: Cierto si la clave existe. Falso en otro caso.
        """
        logging.debug(self.__class__.__name__ + ' setParametro')
        if key in self._atributos:
            self._atributos[key] = str(value)
            return True
        return False

    def getParamValue(self, key):
        """
        B{Este metodo no puede ser sobrescrito.} Devuelve el valor de un
        parametro concreto, dada una clave.

        @param key: Clave del diccionario de _atributos. Debe estar previamente
        inicialiada en init().
        @type key: string

        @return: Si no existe la clave devuelve None, en otro caso devuelve el
        valor guardado del atributo.
        """
        logging.debug('Modulo getParamValue')
        if key in self._atributos:
            return self._atributos[key]

        return None

    def getParamList(self):
        """
        Obtiene la lista de parametros validos. Es decir, la lista de claves
        del diccionario _atributos.
        """
        logging.debug(self.__class__.__name__ + ' getParamList')
        return self._atributos.keys()

    def cargarDesdeTree(self, tree):
        """
        B{Este metodo no puede ser sobrescrito.} Carga los atributos del Modelo
        en el diccionario de _atributos. Elimina aquellos atributos mal formados
        o que no se reconocen.
        
        @param tree: arbol xml para parsear los atributos.
        @type tree: xml.etree.ElementTree
        """
        logging.debug(self.__class__.__name__ + ' cargarDesdeTree')
        dellist = []
        for attr in tree.attrib:
            logging.debug('\tAttr --> ' + attr + " : " + tree.attrib[attr])
            if attr in self._atributos:
                self._atributos[attr] = tree.attrib[attr]
            else:
                dellist = dellist +  [attr]

        for attr in dellist:
            del tree.attrib[attr]