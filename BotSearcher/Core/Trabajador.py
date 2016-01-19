from SC12K_utils import *
from Sonda import Sonda
import threading


class Trabajador(threading.Thread):
    """
    Thread personalizado con senales de control para el rearranque y el control
    de la cola de ejecucion.
    """
    def __init__(self, target):
        """
        Inicializa las senales de trabajoPendiente y running a Falso.
        
        @param target: Funcion que se ejecutara en el thread. Se pasa al padre.
        @type target: funcion 
        """
        self.trabajoPendiente = threading.Event()
        """
        Senal de control que indica si la cola tiene elementos (cierto) o no 
        (falso).
        """
        self.running = threading.Event()
        """
        Senal de control que indica si se ha solicitado que el thread funcion
        (cierto) o no (falso).
        """
        self.trabajoPendiente.clear()
        self.running.clear()
        threading.Thread.__init__(self, target=target)