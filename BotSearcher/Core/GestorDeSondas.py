import sys
sys.path.append('../')
from SC12K_utils import *
from DispensadorIPv6 import DispensadorIPv6
from EjecutorSondeo import EjecutorSondeo
from Sonda import Sonda
import xml.etree.ElementTree as xmlparser

class GestorDeSondas(object):
    """
    Gestor que permite la edicion de sondas. Permite la carga de modulos
    dispensadores y ejecutores de forma interactiva y su configuracion. La
    creacion de nuevas sondas, la carga y el guardado.
    """
#-------------------------------------------------------------------------------
#------------------------------- GESTOR DE SONDAS ------------------------------

    def __init__(self):
        self._Sondas = dict()
        """
        Lista de sondas creadas. Guardadas como (nombre, instancia).
        """
        self._Dispensadores = dict()
        """
        Lista de dispensadores cargados. Guardados como (nombre, clase).
        """
        self._Ejecutores = dict()
        """
        Lista de ejecutores cargados. Guardados como (nombre, clase).
        """

    def cargar(self, xmlfile):
        """
        Carga los modulos dispensadores y ejecutores y las sondas guardadas
        a partir de un fichero xml dado. Elimina del fichero de configuracion
        aquellos dispensadores, ejecutores o sondas que no se pueden cargar.
        
        @param xmlfile: nombre del fichero xml.
        @type xmlfile: string
        """
        logging.info('Cargando modulos desde el fichero ' + xmlfile)
        #importar el fichero:
        self.tree = xmlparser.parse(xmlfile)
        root = self.tree.getroot()

        for xml_dispensador in root.findall('dispensador'):
            print 'Cargando dispensador ' + xml_dispensador.attrib['clase']
            if not self._cargarDispensador(xml_dispensador.attrib['folder'],
                                           xml_dispensador.attrib['modulo'],
                                           xml_dispensador.attrib['clase']):
                root.remove(xml_dispensador)

        for xml_ejecutor in root.findall('ejecutor'):
            print 'Cargando ejecutor ' + xml_ejecutor.attrib['clase']
            if not self._cargarEjecutor(xml_ejecutor.attrib['folder'],
                                        xml_ejecutor.attrib['modulo'],
                                        xml_ejecutor.attrib['clase']):
                root.remove(xml_ejecutor)

        for xml_sonda in root.findall('sonda'):
            print 'Creando sonda ' + xml_sonda.attrib['nombre']
            if not self._anadirSonda(xml_sonda.attrib['nombre'],
                                     xml_sonda.attrib['dispensador'],
                                     xml_sonda.attrib['ejecutor']):
                root.remove(xml_sonda)
            else:
                self._Sondas[xml_sonda.attrib['nombre']].\
                                                      cargarDesdeTree(xml_sonda)

    def	guardar(self):
        """
        Guarda los modulos dispensadores y ejecutores y las sondas creadas
        en el fichero xml. Se cargaran automaticamente en la siguiente carga.
        """
        self.tree.write('modulos.xml')

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
        if sonda in self._Sondas:
            return self._Sondas[sonda].listParam(doe)
        return False
		
    def setParametro(self, sonda, doe, key, value):
        if sonda in self._Sondas:
            return self._Sondas[sonda].setParametro(doe, key, value)
        return False

#-------------------------------------------------------------------------------
#----------------------------------- SONDAS ------------------------------------
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
        result = self._anadirSonda(nombre, dispensadorIPv6, ejecutorSondeo)
        if result:
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'nombre' : nombre, 'dispensador': dispensadorIPv6,
                            'ejecutor' : ejecutorSondeo}
                elem = xmlparser.SubElement(self.tree.getroot(),"sonda",
                                            attrib=attributes)
                self._Sondas[nombre].newTreeRoot(elem)
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
        if not (dispensadorIPv6 in self._Dispensadores):
            logging.warning("Dispensador IPv6 " + dispensadorIPv6
                            + " no existe")
            print "Dispensador IPv6 " + dispensadorIPv6 + " no existe"
            return False

        if not (ejecutorSondeo in self._Ejecutores):
            logging.warning("Ejecutor de Sondeo " + ejecutorSondeo
                            + " no existe")
            print "Ejecutor de Sondeo " + ejecutorSondeo + " no existe"
            return False

        if nombre in self._Sondas:
            logging.warning("La sonda " + nombre + " ya existe")
            print "La sonda " + nombre + " ya existe"
            return False

        disp = self._Dispensadores[dispensadorIPv6]()
        ejec = self._Ejecutores[ejecutorSondeo]()
        sonda = Sonda(nombre, disp, ejec)
        self._Sondas[nombre] = sonda
        return True

    def listarSondas(self):
        """
        Dibuja por pantalla la lista de sondas.
        Muestra el tipo de dispensador y de ejecutor contiene.
        """
        nameKeys = self._Sondas.viewkeys()
        print("---------------------------- Sondas ----------------------------"
              "----")
        print "Nombre\t\t\tDispensadorIPv6\t\t\tSondeo"
        for key in nameKeys:
            print(key + "\t\t\t" + self._Sondas[key].getNombreDispensador() +\
                  "\t\t\t" + self._Sondas[key].getNombreEjecutor())
        print("----------------------------------------------------------------"
              "----")

    def eliminarSonda(self, nombre):
        """
        Elimina la sonda de la lista de sondas y del arbol xml si existe.
        
        @param nombre: nombre de la sonda a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si la sonda no existe y Cierto en otro caso.
        """
        if nombre in self._Sondas:
            del self._Sondas[nombre]
            root = self.tree.getroot()
            for sonda in root.findall("sonda"):
                if sonda.attrib['nombre'] == nombre:
                    root.remove(sonda)
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
        if nombre in self._Sondas:
            return self._Sondas[nombre]
        else:
            return None

#-------------------------------------------------------------------------------
#-------------------------------- DISPENSADORES --------------------------------			
    def cargarDispensador(self, folder, modulename, disp):
        """
        Interficie para cargar dispensadores.
        Pregunta si desea guardar el dispensadores de forma permanente. En caso
        afirmativo la anade al arbol xml.
        
        @param folder: carpeta donde esta el modulo.
        @type folder: string
        
        @param modulename: nombre del modulo.
        @type modulename: string
        
        @param disp: nombre del dispensador.
        @type disp: string
        
        @return: Devuelve Falso hay algun error al cargar el dispensador y
        Cierto si se carga de forma correcta.
        """
        result = self._cargarDispensador(folder, modulename, disp)
        if result:
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'folder' : folder, 'modulo': modulename,
                            'clase' : disp}
                xmlparser.SubElement(self.tree.getroot(),"dispensador",
                                     attrib=attributes)
        return result

    def _cargarDispensador(self, folder, modulename, disp):
        """
        Funcion de carga de dispensadores. Carga una clase derivada de 
        DispensadorIPv6 y la guarda en la lista de dispensadores.
        Posteriormente se podran crear instancias de dicha clase.
        
        @param folder: carpeta donde esta el modulo.
        @type folder: string
        
        @param modulename: nombre del modulo.
        @type modulename: string
        
        @param disp: nombre del dispensador.
        @type disp: string
        
        @return: Devuelve Falso hay algun error al cargar el dispensador y
        Cierto si se carga de forma correcta.
        """
        sobr = 'Y'
        if disp in self._Dispensadores:
            print "El dispensador " + disp + " ya esta cargado."
            sobr = raw_input("Escriba 'Y' para sobrescribirlo")

        if sobr == 'Y':
            logging.info('cargarDispensador Folder: ' + folder + ' Module'
                         + modulename + 'Dispensador ' + disp)
            clase = cargarClase(folder, modulename, disp)
            if clase != None :
                self._Dispensadores[disp] = clase
                if self.checkDisp(clase):
                    logging.info('\tOk')
                    print "Cargado"
                    return True
                else:
                    logging.warning('\tLa clase no coincide con el patron. '
                                    + str(dir(clase)))
                    print "Error: La clase no coincide con el patron."
                    return False
            else :
                logging.warning('\tError al abrir el archivo')
                print "Error: Error al abrir el archivo"
                return False
        else:
            return True

    def checkDisp(self, DispClass):
        """
        Metodo que comprueba si una clase cargada es un DispensadorIPv6 valido.
        
        @param DispClass: clase a comprobar.
        @type DispClass: DispensadorIPv6
        
        @return: Devuelve Cierto si la clase cargada es un DispensadorIPv6
        valido. Falso en otro caso.
        """
        methods = dir(DispClass)
        if 'getDireccionIPv6' in methods:
            return True
        else:
            return False

    def listarDispensadores(self):
        """
        Dibuja por pantalla la lista de dispensadores.
        """
        nameKeys = self._Dispensadores.viewkeys()
        print("------------------------- Dispensadores ------------------------"
              "----")
        print "  Nombre\t\t\t\tParametros"
        for key in nameKeys:
            print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
        print("----------------------------------------------------------------"
              "----")

    def eliminarDispensador(self, nombre):
        """
        Elimina el dispensador de la lista de dispensadores y del arbol xml si
        existe.
        
        @param nombre: nombre del dispensador a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si el dispensador no existe y Cierto en otro caso.
        """
        if nombre in self._Dispensadores:
            del self._Dispensadores[nombre]
            root = self.tree.getroot()
            for disp in root.findall("dispensador"):
                if disp.attrib['clase'] == nombre:
                    root.remove(disp)
                    break
            return True
        else:
            print "No existe el dispensador " + nombre
            return False

#-------------------------------------------------------------------------------
#------------------------------------ EJECUTORES -------------------------------
    def cargarEjecutor(self,folder, modulename, ejec):
        """
        Interficie para cargar ejecutor.
        Pregunta si desea guardar el ejecutor de forma permanente. En caso
        afirmativo la anade al arbol xml.
        
        @param folder: carpeta donde esta el modulo.
        @type folder: string
        
        @param modulename: nombre del modulo.
        @type modulename: string
        
        @param ejec: nombre del ejecutor.
        @type ejec: string
        
        @return: Devuelve Falso hay algun error al cargar el ejecutor y
        Cierto si se carga de forma correcta.
        """
        result = self._cargarEjecutor(folder, modulename, ejec)
        if result:
            if 'Y' == raw_input('Escriba Y para cargar siempre  '):
                attributes={'folder' : folder, 'modulo': modulename,
                            'clase' : ejec}
                xmlparser.SubElement(self.tree.getroot(),"ejecutor",
                                     attrib=attributes)
        return result

    def _cargarEjecutor(self, folder, modulename, ejec):
        """
        Funcion de carga de ejecutores. Carga una clase derivada de 
        EjecutorSondeo y la guarda en la lista de ejecutores.
        Posteriormente se podran crear instancias de dicha clase.
        
        @param folder: carpeta donde esta el modulo.
        @type folder: string
        
        @param modulename: nombre del modulo.
        @type modulename: string
        
        @param ejec: nombre del ejecutores.
        @type ejec: string
        
        @return: Devuelve Falso hay algun error al cargar el ejecutores y
        Cierto si se carga de forma correcta.
        """
        sobr = 'Y'
        if ejec in self._Ejecutores:
            print "El ejecutor " + ejec + " ya esta cargado."
            sobr = raw_input("Escriba 'Y' para sobrescribirlo")
         
        if sobr == 'Y':
            logging.info('cargarEjecutor Folder: ' + folder + ' Module '
                         + modulename + ' Ejecutor ' + ejec)
            clase = cargarClase(folder, modulename, ejec)
            if clase != None :
                self._Ejecutores[ejec] = clase
                if self.checkEjec(clase):
                    logging.info('\tOk')
                    print "Cargado"
                    return True
                else:
                    logging.warning('\tLa clase no coincide con el patron.'
                                    + str(dir(clase)))
                    print "Error: La clase no coincide con el patron."		
                return False
            else :
                logging.warning('\tError al abrir el archivo')
                print "Error: Error al abrir el archivo"
                return False
        else:
            return True

    def checkEjec(self, EjecClass):
        """
        Metodo que comprueba si una clase cargada es un EjecutorSondeo valido.
        
        @param EjecClass: clase a comprobar.
        @type EjecClass: EjecutorSondeo
        
        @return: Devuelve Cierto si la clase cargada es un EjecutorSondeo
        valido. Falso en otro caso.
        """
        methods = dir(EjecClass)
        if 'getResultInfo' in methods:
            return True
        else:
            return False

    def listarEjecutores(self):
        """
        Dibuja por pantalla la lista de ejecutores.
        """
        nameKeys = self._Ejecutores.viewkeys()
        print("---------------------------- Ejecutores ------------------------"
              "----")
        print "  Nombre\t\t\t\tParametros"
        for key in nameKeys:
            print "  " + key + "\t\t\t" + "IRAN LOS PARAMETROS"
        print("----------------------------------------------------------------"
              "----")

    def eliminarEjecutor(self, nombre):
        """
        Elimina el ejecutor de la lista de ejecutores y del arbol xml si existe.
        
        @param nombre: nombre del ejecutor a eliminar.
        @type nombre: string
        
        @return: Devuelve Falso si el ejecutor no existe y Cierto en otro caso.
        """
        if nombre in self._Ejecutores:
            del self._Ejecutores[nombre]
            root = self.tree.getroot()
            for ejec in root.findall("ejecutor"):
                if ejec.attrib['clase'] == nombre:
                    root.remove(ejec)
                    break
            return True
        else:
            print "No existe el ejecutor " + nombre
            return False