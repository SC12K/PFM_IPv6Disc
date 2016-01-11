import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion
import getopt

class Parametros(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "Parametros"
	
	def run(self, params, interprete):
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
				
		#Chequeo de parametros mínimos:
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
			
		GdS.setParametro(sonda, mdisp, key, value)
		
		return True
		
	def help(self):
		logging.debug("Ejecutando Parametros help")
		res = "******************************* Parametros ********************************\n"
		res+= "Parametros -s <sonda> -d|-e -l : Muestra la lista de parametros del\n"
		res+= "dispensador (-d) o del ejecutor (-e) perteneciente a la sonda\n"
		res+= "Parametros -s <sonda> -d|-e -k <key1>,<key2>,<key3> -v <value>,<value2>,<value3>:\n"
		res+= "Establece el valor, dado como value*, de los parametros, dados como key*, en la\n"
		res+= "indicada\n"
		res+= "****************************************************************************"
		return res