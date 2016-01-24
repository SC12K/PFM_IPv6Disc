"""
Repertorio de instrucciones del Gestro de Modulos.
Las instrucciones disponibles permiten cargar, etiquetar y eliminar modulos.
"""
from logger import *
from Instruccion import Instruccion
from GestorDeModulos import *
from SC12K_utils import *
import getopt

class CargarModulo(Instruccion):
    """
    La instruccion CargarModulo permite cargar un moduos y anadirlos al 
    gestor de modulos dada una etiqueta, una direccion de fichero o bien
    una direccion y un nombre de clase.
    """
    
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'CargarModulo'
        """
        self.name = "CargarModulo"

    def run(self, params, interprete):
        """
        Carga un modulo a partir de un path y lo anade a la Lista de 
        modulos. Calcula la carpeta, el modulo y el nombre de la clase a partir
        de un path dado o de un path y una clase.
        Ejecuta la funcion GestorDeModulos.cargarModulo(<carpetar>,<modulo>,
        <clase>)
        
        @param params: Los parametros pueden ser:
            - <etiqueta> <path>: se calcula la carpeta, el modulo y el nombre de
                la clase a partir de un <path>. El modulo y la clase tendran el
                mismo nombre.
            - <etiqueta> <path> <classname>: se calcula la carpeta y el modulo a
                partir del <path> y se usa como nombre de clase <classname>
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si el modulo se ha cargado correctamente.
        """
        logging.debug("Ejecutando CargarModulo. Parametros: "
                      + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',3)
        if len(paramList) > 1:
	    etiqueta = paramList[0]
            carpeta, modulo = pathToFolderModule(paramList[1])
        else:
	    return False

        if len(paramList) > 2:
            clase = paramList[2]
        else :
            clase = modulo

        return GdM.cargarModulo(etiqueta, carpeta, modulo, clase)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion CargarDispensador.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando CargarDispensador help")
        res = ""
        res+= "************************** Cargar Dispensador ******************"
        res+= "************\n"
        res+= "CargarModulo <etiqueta> <path> : Carga el modulo .py dado en el "
        res+= "path y\n"
        res+= "la clase con el mismo nombre que el modulo.\n"
        res+= "CargarMoculo <etiqueta> <path> <nombre> : Carga el modulo .py "
        res+= "dado en el path\n"
        res+= "y la classe de nombre dado.\n"
        res+= "****************************************************************"
        res+= "************"
        return res

class ListarModulos(Instruccion):
    """
    Genera y muestra una Lista de Modulos.
    Mostrando su tipo y sus parametros.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListarDispensadores'
        """
        self.name = "ListarModulos"
	
    def run(self, params, interprete):
        """
        Muestra por pantalla la lista de Modulos.
        Ejecuta la funcion GestorDeModulos.VerModulos()
        
        @param params: puede recibir una etiqueta.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Listar Modulos. Parametros: "
                      + str(params))
        if params == None:
            GdM.verModulos()
            return True

        etiqueta = params.split(' ', 2)[0]
        GdM.verModulosE(etiqueta)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListarDispensadores.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Listar Modulos help")
        res = ""
        res+= "*********************** Listar Modulos *******************"
        res+= "*********\n"
        res+= "ListarModulos: Muestra por pantalla la lista de modulos\n"
        res+= "ListarModulos <etiqueta>: Muestra por pantalla la lista de "
        res+= "modulos de una etiqueta\n"
        res+= "****************************************************************"
        res+= "*********\n"
        return res

class EliminarModulo(Instruccion):
    """
    Elimina un modulo de nombre dado.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarModulo'
        """
        self.name = "EliminarModulo"

    def run(self, params, interprete):
        """
        Elimina el modulo con nombre dado como parametro de la lista de
        dispensadores y del arbol xml si existe
        Ejecuta la funcion GestorDeModulos.eliminarModulo(<nombre>)
        
        @param params: <nombre>: Nombre del modulo a eliminar.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarModulo. Parametros: "
                      + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',3)
        if len(paramList) == 2 :
            etiqueta = paramList[0]
            nombre = paramList[1]
        else :
            self.help()
            return False

        return GdM.eliminarModulo(etiqueta, nombre)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarDispensador.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarModulo help")
        res = ""
        res+= "************************** Eliminar Modulo ****************"
        res+= "************\n"
        res+= "EliminarModulo <etiqueta> <nombre> : Elimina el modulo de "
        res+= "nombre dado\n"
        res+= "Si elimina un modulo que esta en uso por alguna sonda guardada, "
        res+= "no\n"
        res+= "funcionara en la siguiente ejecucion."
        res+= "****************************************************************"
        res+= "************"
        return res