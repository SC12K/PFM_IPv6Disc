from SC12K_utils import *
from Sonda import Sonda
import threading


class Trabajador(threading.Thread):
  
	def __init__(self, target):
		self.trabajoPendiente = threading.Event()
		self.running = threading.Event()
		self.trabajoPendiente.clear()
		self.running.clear()
		
		threading.Thread.__init__(self, target=target)