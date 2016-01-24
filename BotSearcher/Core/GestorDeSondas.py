from logger import *
from GestorDeModulos import *
from Sonda import Sonda
import xml.etree.ElementTree as xmlparser

class GestorDeSondas(object):
    """
    Gestor que permite la edicion de sondas. Permite la carga de modulos
    dispensadores y ejecutores de forma interactiva y su configuracion. La
    creacion de nuevas sondas, la carga y el guardado.
    """
    
    def __init__(self):
        self._sondas = dict()
        """
        Lista de sondas creadas. Guardadas como (nombre, instancia).
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
        #importar el fichero y obtiene la raiz:
        root = xmlparser.parse(xmlfile).getroot()
        self._tree = root.find('sondas')
        
        if self._tree == None:
            self._tree = xmlparser.SubElement(root, 'sondas')
        else:
            for xml_sonda in root.findall('sonda'):
                print 'Creando sonda ' + xml_sonda.attrib['nombre']
                if not self._anadirSonda(xml_sonda.attrib['nombre'],
                                         xml_sonda.attrib['dispensador'],
                                         xml_sonda.attrib['ejecutor']):
                    root.remove(xml_sonda)
                else:
                    self._sondas[xml_sonda.attrib['nombre']].\
                                                      cargarDesdeTree(xml_sonda)

    def	guardarXML(self):
        """
        Guarda los modulos dispensadores y ejecutores y las sondas creadas
        en el fichero xml. Se cargaran automaticamente en la siguiente carga.
        """
        return self._tree

    def listarParametros(self, sonda, doe):
        """
        Devuelve la lista de parametros del dispensador o del ejcutor de una
        sonda y los escribe por pantalla.
        
        @param sonda: nombre de la sonda.
        @type sonda: string
        
        @param doe: 'dispensador o ejecutor'. Cuando es Cierto indica
        Dispensador y Falso indica Ejecutor.
        @type doe: boolean
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if sonda in self._sondas:
            return self._sondas[sonda].listParam(doe)
        return False
		
    def setParametro(self, sonda, doe, key, value):
        """
        Permite establecer el valor de un parametro a una sonda de 
        nombre dado.
        
        @param sonda: nombre de la sonda.
        @type sonda: string
        
        @param doe: 'dispensador o ejecutor'. Cuando es Cierto indica
        Dispensador y Falso indica Ejecutor.
        @type doe: boolean
        
        @param key: Nombre del parametro a modificar.
        @type key: string
        
        @param value: Valor a establecer en el parametro.
        @type value: Cualquiera
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if sonda in self._sondas:
            return self._sondas[sonda].setParametro(doe, key, value)
        return False

    def anadirSonda(self,nombre, dispensadorIPv6, ejecutorSondeo):
        """
        Interficie para anadir sondas.
        Pregunta si desea guardar la sonda de forma permanente. En caso
        afirmativo la anade al arbol xml.
        
        @param nombre: nombre de la sonda.
        @type nombre: string
        
        @param dispensadorIPv6: nombre del dispensador.
        @type dispensadorIPv6: string
        
        @param ejecutorSondeo: nombre de la ejecutor.
        @type ejecutorSondeo: string
        
        @return: Devuelve Falso hay algun error al anadir la sonda y Cierto si
        se anade de forma correcta.
        """
        if nombre in self._sondas:
            logging.warning("La sonda " + nombre + " ya existe")
            print "La sonda " + nombre + " ya existe"
            return False
        
        result = self._anadirSonda(nombre, dispensadorIPv6, ejecutorSondeo)
        if result:
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'nombre' : nombre, 'dispensador': dispensadorIPv6,
                            'ejecutor' : ejecutorSondeo}
                elem = xmlparser.SubElement(self._tree,"sonda",
                                            attrib=attributes)
                self._sondas[nombre].newTreeRoot(elem)
        return result

    def _anadirSonda(self, nombre, dispensadorIPv6, ejecutorSondeo):
        """
        Funcion de creacion de sondas. Crea una instancia del dispensador y el
        ejecutor de nombre dado y los agrupa en una sonda con nombre dado.
        Finalmente la anade a la lista de sondas para su configurado.
        
        @param nombre: nombre de la sonda.
        @type nombre: string
        
        @param dispensadorIPv6: nombre del dispensador.
        @type dispensadorIPv6: string
        
        @param ejecutorSondeo: nombre de la ejecutor.
        @type ejecutorSondeo: string
        
        @return: Devuelve Falso hay algun error al crear o anadir la sonda y
        Cierto si se anade de forma correcta.
        """
        disp = GdM.instanciarModulo("dispensador", dispensadorIPv6)
        if disp == None:
            logging.warning("Dispensador IPv6 " + dispensadorIPv6
                            + " no existe")
            print "Dispensador IPv6 " + dispensadorIPv6 + " no existe"
            return False

        ejec = GdM.instanciarModulo("ejecutor", ejecutorSondeo)
        if ejec == None:
            logging.warning("Ejecutor de Sondeo " + ejecutorSondeo
                            + " no existe")
            print "Ejecutor de Sondeo " + ejecutorSondeo + " no existe"
            return False

        sonda = Sonda(nombre, disp, ejec)
        self._sondas[nombre] = sonda
        return True

    def listarSondas(self):
        """
        Dibuja por pantalla la lista de sondas.
        Muestra el tipo de dispensador y de ejecutor contiene.
        """
        nameKeys = self._sondas.viewkeys()
        print("---------------------------- Sondas ----------------------------"
              "----")
        print "Nombre\t\t\tDispensadorIPv6\t\t\tSondeo"
        for key in nameKeys:
            print(key + "\t\t\t" + self._sondas[key].getNombreDispensador() +\
                  "\t\t\t" + self._sondas[key].getNombreEjecutor())
        print("----------------------------------------------------------------"
              "----")

    def eliminarSonda(self, nombre):
        """
        Elimina la sonda de la lista de sondas y del arbol xml si existe.
        
        @param nombre: nombre de la sonda a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if nombre in self._sondas:
            del self._sondas[nombre]
            for sonda in self._tree.findall("sonda"):
                if sonda.attrib['nombre'] == nombre:
                    self._tree.remove(sonda)
            return True
        else:
            print "No existe la sonda " + nombre
            return False

    def getSonda(self, nombre):
        """
        Devuelve una sonda a partir de un nombre dado.
        
        @param nombre: nombre de la sonda a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if nombre in self._sondas:
            return self._sondas[nombre]
        else:
            return None

    def checkDispensador(self, clase):
        """
        Metodo que comprueba si una clase cargada es un DispensadorIPv6 valido.
        
        @param clase: clase a comprobar.
        @type clase: DispensadorIPv6
        
        @return: Devuelve Cierto si la clase cargada es un DispensadorIPv6
        valido. Falso en otro caso.
        """
        methods = dir(clase)
        if 'getDireccionIPv6' in methods:
            return True
        else:
            return False

    def checkEjecutor(self, clase):
        """
        Metodo que comprueba si una clase cargada es un EjecutorSondeo valido.
        
        @param clase: clase a comprobar.
        @type clase: EjecutorSondeo
        
        @return: Devuelve Cierto si la clase cargada es un EjecutorSondeo
        valido. Falso en otro caso.
        """
        methods = dir(clase)
        if 'getResultInfo' in methods:
            return True
        else:
            return False

global GdS
"""
Variable global para referenciar el Gestor de Sondas.
"""
GdS = GestorDeSondas()