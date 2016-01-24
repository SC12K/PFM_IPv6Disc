from logger import *
from GestorDeEjecucion import *
from Instruccion import Instruccion
import getopt

class ListaEjecucion(Instruccion) :
    """
    Muestra por pantalla la lista de Sondas de la cola de ejecucion.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'ListaEjecucion'
        """
        self.name = "ListaEjecucion"

    def run(self, params, interprete):
        """
        Muestra por pantalla la cola de ejecucion de sondas.
        Ejecuta la funcion GestorDeEjecucion.listarEjecucion()
        
        @param params: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve True siempre.
        """
        logging.debug("Ejecutando Lista Ejecucion. Parametros: " + str(params))
        print GdE.listarEjecucion()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion ListaEjecucion.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Lista Ejecucion help")
        return "Help for Lista Ejecucion"
      
     
class PonerEnCola(Instruccion) :
    """
    Anade una sonda de nombre dado a la cola de ejecucion
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'PonerEnCola'
        """
        self.name = "PonerEnCola"

    def run(self, params, interprete):
        """
        Anade una sonda de nombre dado a la cola de ejecucion. La sonda debe
        haber sido creada y configurada usando el Gestor de sondas.
        Ejecuta las funciones GestorDeSondas.getSonda(<nombre>) y
        GestorDeEjecucion.anadirSonda(<nombre>)
        
        @param params: <nombre>: nombre de la sonda.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Cierto si el dispensador se ha cargado correctamente.
        """
        logging.debug("Ejecutando Poner En Cola. Parametros: " + str(params))
        try:
            options, args = getopt.getopt(params.split(),'n:',['nombre='])
            logging.debug("Options: " + str(options))
            logging.debug("Args: " + str(args))
        except:
            logging.debug("Argumentos incorrectos")
            self.help()
            return False

        if len(options) == 0:
            self.help()
            return False
     
        for opt in options:
            if opt[0] == '-n' or opt== 'nombre':
                nombre = opt[1]
            else:
                self.help()
                return False

        sonda = GdS.getSonda(nombre)
        if not (sonda == None):
            logging.info("Anadiendo sonda " + nombre + " Dispensador: " + sonda.getNombreDispensador() + " Ejecutor: " + sonda.getNombreEjecutor() + " a la cola de ejecucion")
            return GdE.anadirSonda(sonda)
        else:
            logging.warning("Error al cargar " + nombre);
        return False

    def help(self):
        """
        Genera el texto de ayuda de la instruccion PonerEnCola.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        res = ""
        res+= "******************************* Nueva Sonda ***********************************\n"
        res+= "PonerEnCola --nombre <nombre>\n"
        res+= "PonerEnCola -n Nombre\n"
        res+= "Anade una sonda a la cola de ejecucion. Se ejecutara al llegar su turno.\n"
        res+= "*******************************************************************************"
        return res
     	      
class EliminarDeEjecucion(Instruccion) :
    """
    Elimina una sonda de nombre dado a la cola de ejecucion
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'EliminarDeEjecucion'
        """
        self.name = "EliminarDeEjecucion"

    def run(self, params, interprete):
        """
        Elimina la sonda con nombre dado como parametro de la lista de Sondas
        y del arbol xml si existe
        Ejecuta la funcion GestorDeEjecucion.eliminarSonda(indice)
        
        @param params: <index>: recibe un indice como unico parametro.
        @type params: int
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando EliminarDeEjecucion. Parametros: " + str(params))
        if params == "" or params == None:
            self.help()
            return False

        paramList = params.split(' ',1)
        if len(paramList) == 1 :
            index = int(paramList[0])
        else :
            self.help()
            return False

        return GdE.eliminarSonda(index)

    def help(self):
        """
        Genera el texto de ayuda de la instruccion EliminarDeEjecucion.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando EliminarDeEjecucion help")
        res = ""
        res+= "************************** Eliminar Sonda ****************************\n"
        res+= "EliminarDeEjecucion <index> : Elimina el sonda de nombre dado\n"
        res+= "de la cola de ejecucion. Ver la cola de ejecucion para adquirir el indice.\n"
        res+= "****************************************************************************"
        return res

class Ejecutar(Instruccion) :
    """
    Inicia la ejecucion de las sondas.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'Ejecutar'
        """
        self.name = "Ejecutar"

    def run(self, params, interprete):
        """
        Inicia la ejecucion de la Cola de Ejecucion. Las sondas, una a una, se 
        iran ejecutando.
        
        @param params: <index>: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando Ejecutar. Parametros: " + str(params))
        GdE.Ejecutar()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion Ejecutar.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Ejecutar help")
        res = ""
        res+= "************************** Eliminar Sonda ****************************\n"
        res+= "Ejecutar: Inicia la ejecucion de las sondas a traves de un demonio.\n"
        res+= "Al quedarse sin en la lista, el demonio se detendra hasta que se anadan\n"
        res+= "mas y empezara automaticamente.\n"
        res+= "****************************************************************************"
        return res

class Parar(Instruccion) :
    """
    Detiene la ejecucion de las sondas.
    """
    def init(self):
        """
        Inicializa el nombre de la instruccion: 'Parar'
        """
        self.name = "Parar"

    def run(self, params, interprete):
        """
        Detiene la ejecucion de la Cola de Ejecucion. La ejecucion actual queda
        en standby.
        
        @param params: <index>: Esta instruccion no necesita parametros.
        @type params: string
        
        @param interprete: interprete para usar algunas funciones de este.
        @type interprete: Interprete
        
        @return: Devuelve Falso si hay algun problema con los parametros o 
        eliminando la funcion de eliminacion.
        """
        logging.debug("Ejecutando Parar. Parametros: " + str(params))
        GdE.Parar()
        return True

    def help(self):
        """
        Genera el texto de ayuda de la instruccion Parar.
        
        @return: Devuelve el texto a pintar por pantalla.
        """
        logging.debug("Ejecutando Parar help")
        res = ""
        res+= "************************** Eliminar Sonda ****************************\n"
        res+= "Parar: Detiene la ejecucion.\n"
        res+= "****************************************************************************"
        return res