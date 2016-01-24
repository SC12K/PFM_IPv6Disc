"""
Repertorio de instrucciones del Gestro de Sondas.
Las instrucciones disponibles permiten crear, configurar, eliminar y ver las
sondas, los dispensadores y los ejecutores.
"""
from logger import *
from Instruccion import Instruccion
from GestorDeResultados import *
import getopt

class NuevoEscritor(Instruccion):
    """
    La instruccion NuevoEscritor permite crear una sonda con un dispensador y 
    un ejecutor previamente cargado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'NuevoEscritor'
        """
        self.name = "NuevoEscritor"

    def run(self, params, interprete):
        """
        Carga una sonda con nombre <nombre>, dispensador tipo <disp> y ejecutor
        tipo <ejec> y la anade a la Lista de Sondas para configurarse.
        Ejecuta la funcion GestorDeSondas.anadirSonda(<nombre>,<disp>,<ejec>)
        
        @param params: Usa parametros C-style:
            - -n, --nombre <nombre>: nombre de la sonda a crear.
            - -d, --dispensador <disp>: nombre del dispensador de la sonda
            - -e, --ejecutor <ejec>: nombre del ejecutor de  la sonda.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si la sonda se ha anadido correctamente.
        """
        logging.debug("Ejecutando NuevoEscritor. Parametros: " + str(params))
        return False
        #options, args = getopt.getopt(params.split(),'n:d:e:',
                                      #['nombre=', 'dispensador=','ejecutor='])
        #logging.debug("Options: " + str(options))
        #logging.debug("Args: " + str(args))
        #for opt in options:
            #if opt[0] == '-n' or opt== 'nombre':
                #nombre = opt[1]
            #elif opt[0] == '-d' or opt== 'dispensador':
                #dispensador = opt[1]
            #elif opt[0] == '-e' or opt== 'ejecutor':
                #ejecutor = opt[1]
            #else:
                #self.help()
                #return False
        #logging.info("Anadiendo sonda " + nombre + " Dispensador: " +
		     #dispensador + " Ejecutor: " + ejecutor)
        #return GdS.anadirSonda(nombre, dispensador, ejecutor)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion NuevaSonda.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        res = ""
        #res+= "******************************* Nueva Sonda "
        #res+= "***********************************\n"
        #res+= "NuevaSonda --nombre <nombre> --dispensador <DispensadorIPv6>\n"
        #res+= "        --ejecutor <EjecutorSondeo>"
        #res+= "NuevaSonda -n Nombre -d Dispensador -e EjecutorSondeo\n"
        #res+= "Crea una nueva sonda con un dispensador y un ejecutor "
        #res+= "previamente cargados\n"
        #res+= "Usando el nombre nos podemos referir a ella para configurarla.\n"
        #res+= "****************************************************************"
        #res+= "***************"
        return res

class ListarEscritores(Instruccion):
    """
    Genera y muestra una Lista de Escritores.
    Muestra por pantalla su nombre y tipo
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListarEscritores'
        """
        self.name = "ListarEscritores"

    def run(self, params, interprete):
        """
        Muestra por pantalla la lista de sondas.
        Ejecuta la funcion GestorDeEscritores.listarEscritores()
        
        @param params: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Listar Escritores. Parametros: " + str(params))
        GdE.listarEscritores()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListarSondas.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Listar Sondas help")
        res = ""
        #res+= "*************************** Listar Sondas **********************"
        #res+= "*********\n"
        #res+= "ListarSondas: Muestra por pantalla la lista de sondas.\n"
        #res+= "****************************************************************"
        #res+= "*********\n"
        return res

class EliminarEscritor(Instruccion):
    """
    Elimina una escritor de nombre dado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarEscritor'
        """
        self.name = "EliminarEscritor"

    def run(self, params, interprete):
        """
        Elimina la escritor con nombre dado como parametro de la lista de
        escritor y del arbol xml si existe.
        Ejecuta la funcion GestorDeSondas.eliminarSonda(<nombre>)
        
        @param params: <nombre>: Nombre de la sonda a eliminar.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarEscritor. Parametros: " + str(params))
        return False
        #if params == "" or params == None:
            #self.help()
            #return False

        #paramList = params.split(' ',1)
        #if len(paramList) == 1 :
            #nombre = paramList[0]
        #else :
            #self.help()
            #return False

        #return GdS.eliminarSonda(nombre)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarSonda.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarSonda help")
        res = ""
        #res+= "************************** Eliminar Sonda **********************"
        #res+= "************\n"
        #res+= "EliminarSonda <nombre> : Elimina el sonda de nombre dado\n"
        #res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, "
        #res+= "no\n"
        #res+= "funcionara en la siguiente ejecucion."
        #res+= "****************************************************************"
        #res+= "************"
        return res

class ParametrosEscritor(Instruccion):
    """
    Permite trabajar con los parametros de los dispensadores y de los
    ejecutores. Permite listar los parametros disponibles en un dispensador o 
    en un ejecutor, ademas de modificar su valor.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'Parametros'
        """
        self.name = "ParametrosEscritor"

    def run(self, params, interprete):
        """
        Permite trabajar con los parametros de los dispensadores y de los
        ejecutores de una sonda.
        
        @param params: Usa parametros C-style:
            - -s <nombre>: nombre de la sonda a crear.
            - -d|e: dispensador o ejecutor. Establece si se listara los
                parametros del dispensador o del ejecutor de la sonda.
            - -l: opcion para listar los parametros disponibles.
            - -k <key>: nombre del parametro a modificar.
            - -v <value>: nuevo valor del parametro.
            
        Ejemplos de uso:
            - Parametros -s Sonda1 -d -l: Lista los parametros del dispensador
                de la Sonda1.
            - Parametros -s Sonda1 -e -k Ports -v 80,20-22,100: Establece como
                valor del atributo Ports de la Sonda1 el valor '80,20-22,100'.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si lay ejecucion ha sido satisfactoria y 
        Falso en otro caso.
        """
        logging.debug("Ejecutando ParametrosEscritor. Parametros: " + str(params))
        return False
        #try:
            #options, args = getopt.getopt(params.split(),'s:delk:v:')
        #except:
            #logging.debug("Parametros incorrectos. Parametros: " + str(params))
            #return False

        #logging.debug("Options: " + str(options))
        #logging.debug("Args: " + str(args))
        #mdisp = False
        #mejec = False
        #mlist = False
        #sonda = ""
        #key = ""
        #value = ""
        #for opt in options:
            #if opt[0] == '-s':
                #sonda = opt[1]
            #elif opt[0] == '-d':
                #if not mejec:
                    #mdisp = True
            #elif opt[0] == '-e':
                #if not mdisp:
                    #mejec = True
            #elif opt[0] == '-l':
                #mlist = True
            #elif opt[0] == '-k':
                #key = opt[1]
            #elif opt[0] == '-v':
                #value = opt[1]
            #else:
                #self.help()
                #return False
	
        ##Chequeo de parametros minimos:
        #if mdisp == False and mejec == False:
            #print "No has indicado dispensador o ejecutor (-d|-e)."
            #logging.debug("\tBadArgs")
            #return False

        #if sonda == "":
            #print "No has indicado el nombre de la sonda (-s)."
            #logging.debug("\tBadArgs")
            #return False
	
        #if mlist:
            #return GdS.listarParametros(sonda, mdisp)

        ##si continua, flag mlist no estaba activado, por tanto se intentara
        ##setear un parametro.
        #if key == "":
            #print "No has indicado la key del parametro (-k)."
            #logging.debug("\tBadArgs")
            #return False

        #if value == "":
            #print "No has indicado el valor del parametro (-v)."
            #logging.debug("\tBadArgs")
            #return False

        #return GdS.setParametro(sonda, mdisp, key, value)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion Parametros.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando ParametrosEscritor help")
        return ""
        #res = "******************************* Parametros *********************"
        #res+= "***********\n"
        #res+= "Parametros -s <sonda> -d|-e -l : Muestra la lista de parametros "
        #res+= "del\n"
        #res+= "dispensador (-d) o del ejecutor (-e) perteneciente a la sonda\n"
        #res+= "Parametros -s <sonda> -d|-e -k <key1>k -v <value>\n"
        #res+= "Establece el valor, dado como value*, de los parametros, dados"
        #res+= "como key*, en la\n"
        #res+= "indicada\n"
        #res+= "****************************************************************"
        #res+= "************"
        #return res