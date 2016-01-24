from logger import *
from GestorDeModulos import *
from GestorDeSondas import *
from GestorDeResultados import *
from Escritor import Escritor
from InfoResultados import InfoResultados

class GestorDeResultados(object):
    """
    Gestor que permite gestionar los diferentes modulos escritores.
    Estos modulos gestionan el guardado de los resultados generados por las
    sondas.
    
    Permite la carga, eliminacion y configuracion de estos modulos.
    """
    
    def __init__(self):
        """
        Inicializa el gestor de escritores.
        """
        self._escritores = dict()
        """
        Lista de modulos escritores a los que propagar la informacion.
        """
        self._tree = None

    def cargarXML(self, xmlfile):
        """
        Carga los modulos dispensadores y ejecutores y las sondas guardadas
        a partir de un fichero xml dado. Elimina del fichero de configuracion
        aquellos dispensadores, ejecutores o sondas que no se pueden cargar.
        
        @param xmlfile: nombre del fichero xml.
        @type xmlfile: string
        """
        logging.info('Cargando modulos desde el fichero ' + xmlfile)
        
        root = xmlparser.parse(xmlfile).getroot()
        self._tree = root.find('escritores')
        
        if self._tree == None:
            self._tree = xmlparser.SubElement(root, 'escritores')
        else:
            for xml_escritor in root.findall('escritor'):
                print 'Cargando escritor ' + xml_escritor.attrib['nombre']
                if not self._cargarEscritor(xml_escritor.attrib['nombre'],
                                            xml_escritor.attrib['tipo']):
                    self._tree.remove(xml_escritor)
                
    def crearEscritor(self, nombre, tipoescritor):
        """
        Interficie para crear escritores.
        Pregunta si desea guardar el escritor de forma permanente. En caso
        afirmativo la anade al arbol xml.
        
        @param nombre: nombre del escritor.
        @type nombre: string
        
        @param tipoescritor: nombre del tipo de escritor..
        @type tipoescritor: string
        
        @return: Devuelve Falso hay algun error al anadir la escritor y Cierto
        si se anade de forma correcta.
        """
        if nombre in self._escritores:
            logging.warning("El escritor " + nombre + " ya existe")
            print "El escritor " + nombre + " ya existe"
            return False

        result = self._crearEscritor(nombre, tipoescritor)

        if result:
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'nombre' : nombre, 'escritor': tipoescritor}
                elem = xmlparser.SubElement(self.tree.getroot(),"instEscritor",
                                            attrib=attributes)
                self._escritores[nombre].newTreeRoot(elem)
        return result
      
    def _crearEscritor(self, nombre, tipoescritor):
        """
        Funcion de creacion de instancias de escritores para su configurado.
        
        @param nombre: nombre del escritor.
        @type nombre: string
        
        @param tipoescritor: nombre del escritor.
        @type tipoescritor: string
        
        @return: Devuelve Falso hay algun error al crear o anadir el escritor y
        Cierto si se anade de forma correcta.
        """
        escritor = GdM.instanciarModulo("escritor", tipoescritor)
        if escritor == None or not self._checkEsc(escritor):
            logging.warning("El escritor tipo " + tipoescritor + " no existe")
            print "El escritor tipo " + tipoescritor + " no existe"
            return False

        self._escritores[nombre] = escritor
        return True
    
    def _checkEsc(self, clase):
        """
        Metodo que comprueba si una clase cargada es un escritor valido.
        
        @param clase: clase a comprobar.
        @type clase: instancia de objeto
        
        @return: Devuelve Cierto si la clase cargada es un escritor
        valido. Falso en otro caso.
        """
        methods = dir(clase)
        if 'informar' in methods:
            return True
        else:
            return False
    
    def listarParametros(self, escritor):
        """
        Devuelve la lista de parametros del escritor de nombre dado y los
        escribe por pantalla.
        
        @param escritor: nombre de la escritor.
        @type escritor: string
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if not (sonda in self._escritores):
            return False
        
        modulo = self._escritores[escritor]
        keylist = modulo.getParamList()
        print 'Escritor: ' + escritor
        for i in keylist:
            print '\t* ' + i + "\t= " + modulo.getParamValue(i)
        return True 

    def setParametro(self, escritor, key, value):
        """
        Permite establecer el valor de un parametro a un escritor de nombre
        dado.
        
        @param escritor: nombre del escritor.
        @type escritor: string
        
        @param key: Nombre del parametro a modificar.
        @type key: string
        
        @param value: Valor a establecer en el parametro.
        @type value: Cualquiera
        
        @return: Devuelve Falso si la escritor no existe y Cierto en otro caso.
        """
        if escritor in self._escritores:
            return self._escritores[escritor].setParametro(key, value)
        return False
    
    def listarEscritores(self):
        """
        Dibuja por pantalla la lista de escritores.
        """
        nameKeys = self._escritores.viewkeys()
        print("--------------------------- Escritores -------------------------"
              "----")
        print "  Nombre\t\t\t\tParametros"
        for key in nameKeys:
            print "  " + key
            for param in self._escritores[key].getParamList():
                print "\t" + param
        print("----------------------------------------------------------------"
              "----")

    def eliminarEscritores(self, nombre):
        """
        Elimina el escritor de la lista de escritores y del arbol xml si
        existe.
        
        @param nombre: nombre del escritor a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si el escritor no existe y Cierto en otro caso.
        """
        if nombre in self._escritores:
            del self._escritores[nombre]
            for escritor in self._tree.findall("escritor"):
                if escritor.attrib['nombre'] == nombre:
                    root.remove(escritor)
                    break
            return True
        else:
            print "No existe el escritor " + nombre
            return False
	  
    def getEscritor(self, nombre):
        """
        Devuelve un escritor a partir de un nombre dado.
        
        @param nombre: nombre del escritor a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si la escritor no existe y Cierto en otro caso.
        """
        if nombre in self._escritor:
            return self._escritor[nombre]
        else:
            return None
    
    def guardarXML(self):
        return self._tree
      
global GdR
"""
Variable global para referenciar al Gestor de Resultados
"""
GdR = GestorDeResultados()