"""
Repertorio de instrucciones del Gestro de Sondas.
Las instrucciones disponibles permiten crear, configurar, eliminar y ver las
sondas, los dispensadores y los ejecutores.
"""
import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion
import getopt
#------------------------------- Funciones de Carga ----------------------------
class NuevaSonda(Instruccion):
    """
    La instruccion NuevaSonda permite crear una sonda con un dispensador y 
    un ejecutor previamente cargado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'NuevaSonda'
        """
        self.name = "NuevaSonda"

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
        logging.debug("Ejecutando Nueva Sonda. Parametros: " + str(params))
        options, args = getopt.getopt(params.split(),'n:d:e:',
                                      ['nombre=', 'dispensador=','ejecutor='])
        logging.debug("Options: " + str(options))
        logging.debug("Args: " + str(args))
        for opt in options:
            if opt[0] == '-n' or opt== 'nombre':
                nombre = opt[1]
            elif opt[0] == '-d' or opt== 'dispensador':
                dispensador = opt[1]
            elif opt[0] == '-e' or opt== 'ejecutor':
                ejecutor = opt[1]
            else:
                self.help()
                return False
        logging.info("Anadiendo sonda " + nombre + " Dispensador: " +
		     dispensador + " Ejecutor: " + ejecutor)
        return GdS.anadirSonda(nombre, dispensador, ejecutor)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion NuevaSonda.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        res = ""
        res+= "******************************* Nueva Sonda "
        res+= "***********************************\n"
        res+= "NuevaSonda --nombre <nombre> --dispensador <DispensadorIPv6>\n"
        res+= "        --ejecutor <EjecutorSondeo>"
        res+= "NuevaSonda -n Nombre -d Dispensador -e EjecutorSondeo\n"
        res+= "Crea una nueva sonda con un dispensador y un ejecutor "
        res+= "previamente cargados\n"
        res+= "Usando el nombre nos podemos referir a ella para configurarla.\n"
        res+= "****************************************************************"
        res+= "***************"
        return res

class CargarDispensador(Instruccion):
    """
    La instruccion CargarDispensador permite cargar un dispensador dado una
    direccion de fichero o bien una direccion y un nombre de clase.
    """
    
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'CargarDispensador'
        """
        self.name = "CargarDispensador"

    def run(self, params, interprete):
        """
        Carga un dispensador a partir de un path y lo anade a la Lista de 
        dispensadores para configurarse. Calcula la carpeta, el modulo y el
        nombre de la clase a partir de un path dado o de un path y una clase.
        Ejecuta la funcion GestorDeSondas.cargarDispensador(<folder>,<module>,
        <classname>)
        
        @param params: Los parametros pueden ser:
            - <path>: se calcula la carpeta, el modulo y el nombre de la clase
                a partir de un <path>. El modulo y la clase tendran el mismo
                nombre.
            - <path> <classname>: se calcula la carpeta y el modulo a partir del
                <path> y se usa como nombre de clase <classname>
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si el dispensador se ha cargado correctamente.
        """
        logging.debug("Ejecutando CargarDispensador. Parametros: "
                      + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        folder, module = pathToFolderModule(paramList[0])
	
        if len(paramList) > 1 :
            disp = paramList[1]
        else :
            disp = module

        return GdS.cargarDispensador(folder, module, disp)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion CargarDispensador.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando CargarDispensador help")
        res = ""
        res+= "************************** Cargar Dispensador ******************"
        res+= "************\n"
        res+= "CargarDispensador <path> : Carga el modulo .py dado en el path y"
        res+= " la clase\n"
        res+= "con el mismo nombre que el modulo.\n"
        res+= "CargarDispensador <path> <classname> : Carga el modulo .py dado"
        res+= " en el path y\n"
        res+= "la classe de nombre dado.\n"
        res+= "****************************************************************"
        res+= "************"
        return res

class CargarEjecutor(Instruccion):
    """
    La instruccion CargarEjecutor permite cargar un dispensador dado una
    direccion de fichero o bien una direccion y un nombre de clase.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'CargarEjecutor'
        """
        self.name = "CargarEjecutor"
	
    def run(self, params, interprete):
        """
        Carga un ejecutor a partir de un path y lo anade a la Lista de 
        ejecutores para configurarse. Calcula la carpeta, el modulo y el
        nombre de la clase a partir de un path dado o de un path y una clase.
        Ejecuta la funcion GestorDeSondas.cargarEjecutor(<folder>,<module>,
        <classname>)
        
        @param params: Los parametros pueden ser:
            - <path>: se calcula la carpeta, el modulo y el nombre de la clase
                a partir de un <path>. El modulo y la clase tendran el mismo
                nombre.
            - <path> <classname>: se calcula la carpeta y el modulo a partir del
                <path> y se usa como nombre de clase <classname>
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si el ejecutor se ha cargado correctamente.
        """
        logging.debug("Ejecutando CargarEjecutor. Parametros: " + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        folder, module = pathToFolderModule(paramList[0])

        if len(paramList) > 1 :
            disp = paramList[1]
        else :
            disp = module

        return GdS.cargarEjecutor(folder, module, disp)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion CargarEjecutor.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando CargarEjecutor help")
        res = ""
        res+= "************************** Cargar Ejecutor *********************"
        res+= "*********\n"
        res+= "CargarEjecutor <path> : Carga el modulo .py dado en el path y la"
        res+= " clase\n"
        res+= "con el mismo nombre que el modulo.\n"
        res+= "CargarEjecutor <path> <classname> : Carga el modulo .py dado en "
        res+= "el path y\n"
        res+= "la classe de nombre dado.\n"
        res+= "****************************************************************"
        res+= "************"
        return res

#-------------------------------- Funciones de Lista ---------------------------
class ListarSondas(Instruccion):
    """
    Genera y muestra una Lista de Sondas.
    Muestra por pantalla su nombre, su tipo de dispensador y su tipo de
    ejecutor.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListarSondas'
        """
        self.name = "ListarSondas"

    def run(self, params, interprete):
        """
        Muestra por pantalla la lista de sondas.
        Ejecuta la funcion GestorDeSondas.listarSondas()
        
        @param params: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Listar Sondas. Parametros: " + str(params))
        GdS.listarSondas()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListarSondas.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Listar Sondas help")
        res = ""
        res+= "*************************** Listar Sondas **********************"
        res+= "*********\n"
        res+= "ListarSondas: Muestra por pantalla la lista de sondas.\n"
        res+= "****************************************************************"
        res+= "*********\n"
        return res
		
class ListarDispensadores(Instruccion):
    """
    Genera y muestra una Lista de Dispensadores.
    Mostrando su tipo y sus parametros.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListarDispensadores'
        """
        self.name = "ListarDispensadores"
	
    def run(self, params, interprete):
        """
        Muestra por pantalla la lista de dispensadores.
        Ejecuta la funcion GestorDeSondas.listarDispensadores()
        
        @param params: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Listar Dispensadores. Parametros: "
                      + str(params))
        GdS.listarDispensadores()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListarDispensadores.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Listar Dispensadores help")
        res = ""
        res+= "*********************** Listar Dispensadores *******************"
        res+= "*********\n"
        res+= "ListarDispensadores: Muestra por pantalla la lista de "
        res+= "dispensadores.\n"
        res+= "****************************************************************"
        res+= "*********\n"
        return res

class ListarEjecutores(Instruccion):
    """
    Genera y muestra una Lista de Ejecutores.
    Mostrando su tipo y sus parametros.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListarEjecutores'
        """
        self.name = "ListarEjecutores"

    def run(self, params, interprete):
        """
        Muestra por pantalla la lista de ejecutores.
        Ejecuta la funcion GestorDeSondas.listarEjecutores()
        
        @param params: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Listar Ejecutores. Parametros: "
                      + str(params))
        GdS.listarEjecutores()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListarEjecutores.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Listar Ejecutores help")
        res = ""
        res+= "************************* Listar Ejecutores ********************"
        res+= "*********\n"
        res+= "ListarEjecutores: Muestra por pantalla la lista de Ejecutores.\n"
        res+= "****************************************************************"
        res+= "*********\n"
        return res

#------------------------------ Funciones de Eliminar --------------------------
class EliminarSonda(Instruccion):
    """
    Elimina una sonda de nombre dado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarSonda'
        """
        self.name = "EliminarSonda"

    def run(self, params, interprete):
        """
        Elimina la sonda con nombre dado como parametro de la lista de Sondas
        y del arbol xml si existe
        Ejecuta la funcion GestorDeSondas.eliminarSonda(<nombre>)
        
        @param params: <nombre>: Nombre de la sonda a eliminar.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarSonda. Parametros: " + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        if len(paramList) == 1 :
            nombre = paramList[0]
        else :
            self.help()
            return False

        return GdS.eliminarSonda(nombre)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarSonda.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarSonda help")
        res = ""
        res+= "************************** Eliminar Sonda **********************"
        res+= "************\n"
        res+= "EliminarSonda <nombre> : Elimina el sonda de nombre dado\n"
        res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, "
        res+= "no\n"
        res+= "funcionara en la siguiente ejecucion."
        res+= "****************************************************************"
        res+= "************"
        return res

class EliminarDispensador(Instruccion):
    """
    Elimina un dispensador de nombre dado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarDispensador'
        """
        self.name = "EliminarDispensador"

    def run(self, params, interprete):
        """
        Elimina el dispensador con nombre dado como parametro de la lista de
        dispensadores y del arbol xml si existe
        Ejecuta la funcion GestorDeSondas.eliminarDispensador(<nombre>)
        
        @param params: <nombre>: Nombre del dispensador a eliminar.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarDispensador. Parametros: "
                      + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        if len(paramList) == 1 :
            nombre = paramList[0]
        else :
            self.help()
            return False

        return GdS.eliminarDispensador(nombre)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarDispensador.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarDispensador help")
        res = ""
        res+= "************************** Eliminar Dispensador ****************"
        res+= "************\n"
        res+= "EliminarDispensador <nombre> : Elimina el dispensador de nombre"
        res+= "dado\n"
        res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, "
        res+= "no\n"
        res+= "funcionara en la siguiente ejecucion."
        res+= "****************************************************************"
        res+= "************"
        return res

class EliminarEjecutor(Instruccion):
    """
    Elimina un ejecutor de nombre dado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarEjecutor'
        """
        self.name = "EliminarEjecutor"

    def run(self, params, interprete):
        """
        Elimina el ejecutor con nombre dado como parametro de la lista de
        ejecutores y del arbol xml si existe
        Ejecuta la funcion GestorDeSondas.eliminarEjecutor(<nombre>)
        
        @param params: <nombre>: Nombre del ejecutor a eliminar.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarEjecutor. Parametros: " + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        if len(paramList) == 1 :
            nombre = paramList[0]
        else :
            self.help()
            return False

        return GdS.eliminarEjecutor(nombre)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarEjecutor.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarEjecutor help")
        res = ""
        res+= "************************** Eliminar Ejecutor *******************"
        res+= "*********\n"
        res+= "EliminarEjecutor <nombre> : Elimina el ejecutor de nombre dado\n"
        res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, "
        res+= "no\n"
        res+= "funcionara en la siguiente ejecucion."
        res+= "****************************************************************"
        res+= "************"
        return res


#----------------------------------- Parametros --------------------------------
class Parametros(Instruccion):
    """
    Permite trabajar con los parametros de los dispensadores y de los
    ejecutores. Permite listar los parametros disponibles en un dispensador o 
    en un ejecutor, ademas de modificar su valor.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'Parametros'
        """
        self.name = "Parametros"

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
        logging.debug("Ejecutando Parametros. Parametros: " + str(params))
        try:
            options, args = getopt.getopt(params.split(),'s:delk:v:')
        except:
            logging.debug("Parametros incorrectos. Parametros: " + str(params))
            return False

        logging.debug("Options: " + str(options))
        logging.debug("Args: " + str(args))
        mdisp = False
        mejec = False
        mlist = False
        sonda = ""
        key = ""
        value = ""
        for opt in options:
            if opt[0] == '-s':
                sonda = opt[1]
            elif opt[0] == '-d':
                if not mejec:
                    mdisp = True
            elif opt[0] == '-e':
                if not mdisp:
                    mejec = True
            elif opt[0] == '-l':
                mlist = True
            elif opt[0] == '-k':
                key = opt[1]
            elif opt[0] == '-v':
                value = opt[1]
            else:
                self.help()
                return False
	
        #Chequeo de parametros minimos:
        if mdisp == False and mejec == False:
            print "No has indicado dispensador o ejecutor (-d|-e)."
            logging.debug("\tBadArgs")
            return False

        if sonda == "":
            print "No has indicado el nombre de la sonda (-s)."
            logging.debug("\tBadArgs")
            return False
	
        if mlist:
            return GdS.listarParametros(sonda, mdisp)

        #si continua, flag mlist no estaba activado, por tanto se intentara
        #setear un parametro.
        if key == "":
            print "No has indicado la key del parametro (-k)."
            logging.debug("\tBadArgs")
            return False

        if value == "":
            print "No has indicado el valor del parametro (-v)."
            logging.debug("\tBadArgs")
            return False

        return GdS.setParametro(sonda, mdisp, key, value)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion Parametros.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Parametros help")
        res = "******************************* Parametros *********************"
        res+= "***********\n"
        res+= "Parametros -s <sonda> -d|-e -l : Muestra la lista de parametros "
        res+= "del\n"
        res+= "dispensador (-d) o del ejecutor (-e) perteneciente a la sonda\n"
        res+= "Parametros -s <sonda> -d|-e -k <key1>k -v <value>\n"
        res+= "Establece el valor, dado como value*, de los parametros, dados"
        res+= "como key*, en la\n"
        res+= "indicada\n"
        res+= "****************************************************************"
        res+= "************"
        return res