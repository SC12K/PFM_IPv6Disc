from logger import *
import sys
from SC12KModulo import SC12KModulo
import xml.etree.ElementTree as xmlparser

class GestorDeModulos(object):
    """
    Gestor encargado de gestionar todos los modulos antes de ser instanciados.
    
    Utiliza etiquetas para diferenciar los tipos de modulos. Si una etiqueta no
    existe al solicitar anadirle un modulo, se crea.
    """
    
    def __init__(self):
        """
        Inicializa el diccionario de modulos.
        """
        self._modulos = dict()
        self._tree = None
    
    def cargarXML(self, xmlfile):
        """
        Carga los modulos disponibles desde un fichero dado y guarda el arbol xml
        para guardar posteriormente.
        
        @param xmlfile: nombre del fichero xml.
        @type xmlfile: string
        """
        logging.info('Cargando modulos desde el fichero ' + xmlfile)
        #importar el fichero y obtiene la raiz:
        root = xmlparser.parse(xmlfile).getroot()
        #selecciona el apartado "modulos"
        #Si find devuelve None, se crea el nodo modulos de donde colgaran los
        #modulos.
        self._tree = root.find('modulos')
        if self._tree == None:
            self._tree = xmlparser.SubElement(root, 'modulos')
        else:
            for xml_modulo in self._tree.findall('modulo'):
                print('Cargando modulo ' + xml_modulo.attrib['etiqueta'] + " " 
                      + xml_modulo.attrib['clase'])
            
                clase_ = self._cargarModulo(xml_modulo.attrib['carpeta'],
                                            xml_modulo.attrib['modulo'],
                                            xml_modulo.attrib['clase'])
            
                if clase_ == None:
                    print('Error al cargar el modulo '
                          + xml_modulo.attrib['etiqueta'] + " " 
                          + xml_modulo.attrib['clase'])
                    continue 
            
                if xml_modulo.attrib['etiqueta'] not in self._modulos:
                    self._modulos[xml_modulo.attrib['etiqueta']] = dict()
            
                self._modulos[xml_modulo.attrib['etiqueta']]\
                             [xml_modulo.attrib['clase']] = clase_
                         
      
    def cargarModulo(self, etiqueta, carpeta, modulo, clase):
        """
        Interficie para cargar un modulo de tipo SC12KModulo o sus deribados.
        Pregunta si desea guardar el modulo de forma permanente.
        En caso afirmativo la anade al arbol xml.
        
        Utiliza etiquetas para almacenar los modulos clasificados.
        
        @param carpeta: carpeta donde esta el modulo.
        @type carpeta: string
        
        @param modulo: nombre del modulo.
        @type modulo: string
        
        @param clase: nombre de la clase.
        @type clase: string
        
        @return: Devuelve Falso hay algun error al cargar el modulo y Cierto si
        se carga de forma correcta.
        """
        if etiqueta not in self._modulos:
            logging.debug('creando diccionario para etiqueta ' + etiqueta)
            self._modulos[etiqueta] = dict()
            
        logging.debug('cargando etiquetas ' + etiqueta)
        modulosE = self._modulos[etiqueta]
        
        if clase in modulosE:
            print "El modulo " + clase + " ya esta cargado en la etiqueta " +\
                  etiqueta
            if raw_input("Escriba 'Y' para sobrescribirlo ") != Y:
                return True

        clase_ = self._cargarModulo(carpeta, modulo, clase)
        
        if clase_ != None:
            print "Cargado"
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'etiqueta' : etiqueta, 'carpeta' : carpeta,
			    'modulo': modulo, 'clase' : clase}
                xmlparser.SubElement(self._tree,'modulo',
                                     attrib=attributes)
            
            self._modulos[etiqueta][clase] = clase_
            return True
        else:
	    print "No se ha podido cargar la clase"
            return False
      
    def _cargarModulo(self, carpeta, modulo, clase):
        """
        Funcion interna de carga de modulos. Realiza realmente la carga.
        
        @param carpeta: carpeta donde esta el modulo.
        @type carpeta: string
        
        @param modulo: nombre del modulo.
        @type modulo: string
        
        @param clase: nombre del clase.
        @type clase: string
        
        @return: Devuelve Falso hay algun error al cargar el modulo y
        Cierto si se carga de forma correcta.
        """
        

        logging.info('cargar Modulo carpeta: ' + carpeta + ' modulo '
                     + modulo + 'clase ' + clase)

        try:
            if (carpeta != "" and carpeta != "./"):
                sys.path.append(carpeta)
            _modulo = __import__(modulo)
            clase_ = getattr(_modulo, clase)
            return clase_
        except Exception as E:
            logging.warning('\tError al abrir el archivo')
            print "Error: Error al abrir el archivo"
            print E
            clase_ = None
            return clase_
  
    def verModulos(self):
        """
        Permite listar todos los modulos clasificados por etiqueta.
        """
        result = True
        print "- Modulos -"
        for etiqueta in self._modulos:
            if not self.verModulosE(etiqueta):
                result = False
        return result
      
    def verModulosE(self, etiqueta):
        """
        Permite ver los modulos de una etiqueta concreta.
        
        @param etiqueta: Etiqueta que se quiere mostrar.
        @type etiqueta: string
        """
        if not (etiqueta in self._modulos):
            return False
        
        print "- Modulos : " + etiqueta + " -"
        
        for modulo in self._modulos[etiqueta]:
            print "\t"  + modulo
        
    
    def eliminarModulo(self, etiqueta, nombre):
        """
        Elimina el modulo de la lista de modulo y del arbol xml si
        existe.
        
        @param nombre: nombre del modulo a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si el modulo no existe y Cierto en otro caso.
        """
        if not (etiqueta in self._modulos):
            print "No existe la etiqueta " + etiqueta
            return False
        
        if not (nombre in self._modulos[etiqueta]):
            print "No existe la clase " + nombre
            return False

        del self._modulos[nombre]
        for xmlE in self._tree.findall('modulo'):
            if xmlE.attrib['etiqueta'] == etiqueta:
                continue
            if xmlE.attrib['clase'] == nombre:
                self._tree.remove(xmlE)
                break
        return True
    
    def instanciarModulo(self, etiqueta, nombre):
        """
        Crea una instancia de un modulo cargado previamente.
        
        @param etiqueta: Etiqueta de la clase a eliminar.
        @type etiqueta: string
        
        @param nombre: Nombre de la clase a eliminar.
        @type nombre: string
        """
        if not (etiqueta in self._modulos):
           return None

        if not (nombre in self._modulos[etiqueta]):
           return None
        
        return self._modulos[etiqueta][nombre]()
      
    def guardarXML(self):
        return self._tree
      
      
global GdM
"""
Variable global para referenciar el Gestor de Modulos.
"""
GdM = GestorDeModulos()