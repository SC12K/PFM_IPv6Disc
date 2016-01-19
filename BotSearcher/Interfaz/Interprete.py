import sys
sys.path.append('../')
from SC12K_utils import *
import Instruccion
import xml.etree.ElementTree as xmlparser

class Interprete(object):
    """
    Interficie de usuario que nos permite manejar las sondas, los ejecutores,
    los dispensadores, las salidas y la cola de ejeucion.
    """
    class Ayuda(Instruccion.Instruccion):
        """
        La Ayuda es una Instruccion basica del interprete.
        """      
        def init(self):
	    """
            Inicializa el nombre de la instruccion.
            """ 
            self.name = "Ayuda"

        def run(self, params, interprete):
	    """
            Ejecuta la instruccion Ayuda. Ejecutara la instruccion help() de una
            instruccion dada o la Ayuda general.
            
            @param params:
                1. None : Escribe por pantalla la ayuda general y la lista de 
                    instrucciones disponibles.
                2. <NombreCorrecto> : Escribe por pantalla la ayuda de la
                    instruccion dada.
                3. <NombreIncorrecto> : Si la instruccion no existe, escribe por
                    pantalla 
            @type params: string
            
            @param interprete: Nos permite lanzar la funcion ejecHelp del
                Interprete.
            @type interprete: Interprete
            
            @returns: Devuelve Falso cuando la instruccion dada no existe y
                cierto en cualquier otro caso.
            """ 
            if (params == None) :
                res = self.help()
                print res
            else :
                res = interprete.ejecHelp(params)
                if res == None :
                    print "La instrucción no existe"
                    return False
                else :
                    print res

            return True

        def help(self):
	    """
            Auyuda general del Interprete.
            
            @returns: devuelve un string con el texto a escribir por pantalla.
            """
            res = "BotSearcherIPv6 te ayuda a ejecutar diferentes escaners\n"
            res +=" programados y centralizar la información.\n"
            res +="utiliza 'ayuda <comando>' para ver la ayuda de un comando."
            return res

    def __init__(self):
        """
        Inicializa el interprete y muestra la firma por pantalla.
        """
        logging.info('Abriendo interprete...')
        print "BotSearcher IPv6 Manager"
        print " ____   ____ _ ____  _  __  _____"                    
        print "/ ___| / ___/ |___ \| |/ / |_   _|__  __ _ _ __ ___"  
        print "\___ \| |   | | __) | ' /    | |/ _ \/ _` | '_ ` _ \\"
        print " ___) | |___| |/ __/| . \    | |  __/ (_| | | | | | |"
        print "|____/ \____|_|_____|_|\_\   |_|\___|\__,_|_| |_| |_|"
        print ""
        print "Interprete para la configuracion de la ejecucion de busquedas."
        print ""
        self.repertorio = dict()

    def ejecInstr(self, instr, params) :
        """
        Ejecuta una instruccion dado un nombre con unos parametros dados.
        
        @param instr: nombre de la instruccion a ejecutar
        @type instr: string
        
        @param params: Texto con los parametros de ejecucion.
        @type params: string
        
        @returns: Devuelve Falso si la instruccion no se encuentra en el
            repertorio.
            Si se encuentra, devuelve el valor de la ejecucion de la instruccion.
        """
        logging.debug('ejecInstr repo keys: ' + str(self.repertorio.viewkeys()))
        if instr in self.repertorio :
            #separar parametros de instruccion
            return self.repertorio[instr].run(params,self)
        else :
            return False

    def cargarInstruccion(self, path, modulename, classname):
        """
        Carga una instruccion al repertorio.
        
        @param path: carpeta donde se encuentra el modulo.
        @type path: string
        
        @param modulename: Fichero *.py que contiene la instruccion.
        @type modulename: string
        
        @param classname: Nombre de la clase deribada de Instruccion.
        @type classname: string
        
        @returns: Devuelve None si hay algun problema. En otro caso devuelve una
        instancia de la funcion.
        """
        logging.debug("cargarInstruccion: " + path + "" + modulename + "" +\
                      classname)
        clase = cargarClase(path, modulename, classname)
        logging.debug('cargarInstruccion atributos y funciones de ' + classname
                     + ' : ' + str(dir(clase)))
        if clase == None:
            return None
        
        if not self.checkInstr(clase):
            return None
        instancia = clase()
        
        return instancia

    def checkInstr(self, InstrClass) :
        """
        Metodo que comprueba si una clase cargada es una instruccion valida
        para la ejecucion en el interprete.
        
        @param InstrClass: clase a comprobar.
        @type InstrClass: Instruccion.
        
        @return: Devuelve Cierto si la clase cargada es valida. Falso en otro
            caso.
        """
        methods = dir(InstrClass)
        if 'run' in methods and 'help' in methods:
            return True
        else:
            return False

    def cargarRepertorio(self, xmlfile) :
        """
        Carga el repertorio de instrucciones a partir de un fichero XML con el
        siguiente formato:
        
        <instrucciones>
        <instruccion nombre='EjemploClase' modulo='EjemploModulo' path='./'/>
        </instrucciones>
        
        @param xmlfile: Nombre del fichero xml a cargar.
        @type xmlfile: string
        """
        instruccion = self.Ayuda()
        self.repertorio[instruccion.name]= instruccion
        #importar el fichero:
        tree = xmlparser.parse(xmlfile)
        root = tree.getroot()
        for child in root:
            logging.info('Cargando instruccion: ' + child.attrib['path'] + " " 
                         + child.attrib['modulo'] +" "+ child.attrib['nombre'])
            instruccion = self.cargarInstruccion(child.attrib['path'],
                                                 child.attrib['modulo'],
                                                 child.attrib['nombre'])
            if instruccion != None:
                self.repertorio[instruccion.name]= instruccion
            else:
                logging.error("Instruccon no cargada: " + child.attrib['nombre'])

    def ejecHelp(self, instr) :
        """
        Ejecuta la instruccion help() de una Instruccion dada.

        @param instr: Nombre de la instruccion.
        @type instr: string
        """
        if instr in self.repertorio :
            return self.repertorio[instr].help()
        else :
            return None

    def ejecutarBucle(self) :
        """
        Bucle principal de ejecucion del interprete. Lee las instrucciones y las
        ejecuta.
        Usando Exit salimos el programa.
        """
        instr = ''
        while instr != "Exit":		
            instr = raw_input('$>>')
            logging.info('Instruccion introducida: ' + instr)
            instrParts = instr.split(' ', 1)
            if len(instrParts) != 2 :
                logging.info('\tNo contiene parametros')
                execu = self.ejecInstr(instrParts[0], None)
                if instrParts[0] == 'Ayuda':
                    for instrName in self.repertorio.viewkeys():
                        print "\t*  " + instrName
                    print "\t*  Exit"
            else : 
                logging.info('\tContiene parametros')
                execu = self.ejecInstr(instrParts[0], instrParts[1])
                
            if(not execu and instrParts[0] != "Exit"):
                logging.warning('\tError de ejecucion')
                print "Error en la ejecucion."
                if instrParts[0] in self.repertorio :
                    logging.warning('\tLa instruccion existe.')
                    print self.repertorio[instrParts[0]].help()
                else :
                    logging.warning('\tLa instruccion no existe.')
                    print "La instruccion no existe. Usa 'Ayuda'"