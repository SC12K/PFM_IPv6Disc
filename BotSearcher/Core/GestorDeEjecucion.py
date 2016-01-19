from SC12K_utils import *
from Sonda import Sonda
from Trabajador import Trabajador

class GestorDeEjecucion(object):
  
    def __init__(self) :
        self.sondasFIFO = list()
        self.trabajador = Trabajador(target=self.runningFunc)
        self.trabajador.setDaemon(True)
        self.sondaActual = None
        self.trabajadorOn = False

    def anadirSonda(self,sonda):
        self.sondasFIFO.append(sonda)
        self.trabajador.trabajoPendiente.set()
        return True;

    def eliminarSonda(self,index):
        del self.sondasFIFO[index]
        if len(self.sondasFIFO) == 0 :
            self.trabajador.trabajoPendiente.clear()

    def listarEjecucion(self):
        res = ""
        if not (self.sondaActual == None):
            res+= "Sonda en ejecucion: " + self.sondaActual.getName() + "\n"

        if len(self.sondasFIFO) == 0 :
            res+= "No hay ninguna sonda en la cola de ejecucion\n"
        else:
            res+= "--------------------------- Cola de Ejecucion --------------"
            res+= "-----------------------\n"
            index = 0
            for sonda in self.sondasFIFO:
                res+= "\t" + str(index) + "\t" + sonda.getName() + "\n"
        return res

    def getSiguienteSonda(self):
        try:
            self.sondaActual = self.sondasFIFO.pop()
        except:
            self.trabajador.trabajoPendiente.clear()
            self.sondaActual = None
            return None

        return self.sondaActual

    def Ejecutar(self):
        if len(self.sondasFIFO) > 0 or not (self.sondaActual == None):
            self.trabajador.running.set()
            if not self.trabajadorOn:
                self.trabajadorOn = True
                self.trabajador.start()

            return True
        else :
            print "No hay elementos en la cola de ejecucion"
            return False

    def Parar(self):
        if  self.trabajador.is_alive():
            self.trabajador.running.clear()
            return True
        else :
            print "La sonda actual " + sondaActual.getName() + " no esta en ejecucion"
            return False

    def runningFunc(self):
        print("Ejecutando Trabajador")
        sonda = None

        while self.trabajador.running.wait() :
            if sonda == None:
                sonda = self.getSiguienteSonda()

            if not self.trabajador.trabajoPendiente.isSet():
                self.trabajador.trabajoPendiente.wait()
                continue
            try:
                res = sonda.ejecutarPaso()
                if res == "":
                    sonda = None
            except:
                print "Error ejecutando la sonda: ", sys.exc_info()[0], sys.exc_info()[1]
                break

        print("Trabajador Parado")