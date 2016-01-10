import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion
import getopt

class NuevaSonda(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "NuevaSonda"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando Nueva Sonda. Parametros: " + str(params))
		options, args = getopt.getopt(params.split(),'n:d:e:',['nombre=', 'dispensador=','ejecutor='])
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
		logging.info("Añadiendo sonda " + nombre + " Dispensador: " + dispensador + " Ejecutor: " + ejecutor)
		
		return GdS.anadirSonda(nombre, dispensador, ejecutor)
		
	def help(self):
		res = ""
		res+= "******************************* Nueva Sonda ***********************************\n"
		res+= "NuevaSonda --nombre <nombre> --dispensador <DispensadorIPv6>\n"
		res+= "        --ejecutor <EjecutorSondeo>"
		res+= "NuevaSonda -n Nombre -d Dispensador -e EjecutorSondeo\n"
		res+= "Crea una nueva sonda con un dispensador y un ejecutor previamente cargados\n"
		res+= "Usando el nombre nos podemos referir a ella para configurarla.\n"
		res+= "*******************************************************************************"
		return res