from logger import *
from Sonda import Sonda
from Escritor import Escritor
from Trabajador import Trabajador
import xml.etree.ElementTree as xmlparser

class GestorDeEjecucion(object):
    """
    Gestor para controlar la ejecucion de las sondas a traves de una cola de
    ejecucion.
    Se pueden poner sondas en cola y se ejecutaran de forma secuencial.
    Por un lado almacenara las sondas a ajecutar y se propagara la informacion a
    todos los escritores.
    """
    def __init__(self) :
        """
        Inicializa la cola de ejecucion y la lista de escritores. Tambien
        incializa el thread de ejecucion, dejandolo parado.
        """
        self._sondasFIFO = list()
        """
        Cola de ejecucion de sondas.
        """
        self._escritores = list()
        """
        Lista de escritores para propagar la informacion
        """
        self._trabajador = Trabajador(target=self.runningFunc)
        """
        Thread de trabajo.
        """
        self._trabajador.setDaemon(True)
        self._trabajador.start()
        
        self._sondaActual = None
        """
        Sonda que se esta ejecutando actualmente en el Bot.
        """

    def anadirSonda(self, sonda):
        """
        Anade una sonda dada a la cola de ejecucion.
        
        @param sonda: sonda que se quiere anadir a la ejecucion.
        @type sonda: Sonda
        """
        self._sondasFIFO.append(sonda)
        self._trabajador.trabajoPendiente.set()
        return True;

    def eliminarSonda(self, index):
        """
        Elimina una sonda de la cola de ejecucion dado un indice.
        
        @param index: Indice de la sonda que se quiere eliminar.
        @type index: int
        """
        del self._sondasFIFO[index]
        if len(self._sondasFIFO) == 0 :
            self._trabajador.trabajoPendiente.clear()

    def listarEjecucion(self):
        """
        Muestra por pantalla la lista de sondas que estan en la cola de
        ejecucion. Muestra el indice asociado a cada sonda.
        """
        res = ""
        if not (self._sondaActual == None):
            res+= "Sonda en ejecucion: " + self._sondaActual.getName() + "\n"

        if len(self._sondasFIFO) == 0 :
            res+= "No hay ninguna sonda en la cola de ejecucion\n"
        else:
            res+= "--------------------------- Cola de Ejecucion --------------"
            res+= "-----------------------\n"
            index = 0
            for sonda in self._sondasFIFO:
                res+= "\t" + str(index) + "\t" + sonda.getName() + "\n"
        return res

    def _getSiguienteSonda(self):
        """
        Devuelve la primera sonda de la cola de ejecucion, eliminandola de esta
        y estableciendola como sonda actual.
        """
        try:
            sonda = self._sondasFIFO.pop()
        except:
            self._trabajador.trabajoPendiente.clear()
            return None

        return sonda

    def Ejecutar(self):
        """
        Activa la ejecucion del Thread trabajador si existe alguna sonda en la
        cola de ejecucion o si existe alguna sonda pausada.
        """
        if len(self._sondasFIFO) > 0 or not (self._sondaActual == None):
            self._trabajador.trabajando.set()    
            return True
        else :
            print "No hay elementos en la cola de ejecucion"
            return False


    def Parar(self):
        """
        Para la ejecucion de la sonda actual.
        """
        if  self._trabajador.trabajando.isSet():
            self._trabajador.trabajando.clear()
            return True
        else :
            print "La sonda actual " + sondaActual.getName() + " no esta en ejecucion"
            return False

    def runningFunc(self):
        """
        Funcion ejecutada por el Thread que ejecuta la sonda y el proceso de 
        guardado de resultados.
        """
        print("Trabajador Iniciado")
     
	while self._trabajador.trabajando.wait() :
            if self._sondaActual == None:
                self._sondaActual = self._getSiguienteSonda()

            if not self._trabajador.trabajoPendiente.isSet():
                self._trabajador.trabajoPendiente.wait()
                continue
            
            try:
                res_ok = self._sondaActual.ejecutarPaso()
                if not res_ok:
                    self._sondaActual = None
                    continue
                
                infoRes = self._sondaActual.getResultInfo()
                self._informar(infoRes)
            except:
                print "Error ejecutando la sonda: ", sys.exc_info()[0], sys.exc_info()[1]
                break

        print("Trabajador Parado")
        
    def _informar(self, infoRes):
        """
        Metodo que propaga la informacion por todos los escritores disponibles durante
        la ejecucion.
        
        @param infoRes: Informacion de resultados obtenidos por la sonda.
        @type infoRes: InfoResultado
        """
        for escritor in self._escritores:
            escritor.informar(infoRes)
            

global GdE
"""
Variable global para referenciar el Gestor de Ejecucion.
"""
GdE = GestorDeEjecucion()