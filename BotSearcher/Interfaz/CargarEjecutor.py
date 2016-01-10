import sys
sys.path.append('../')
from SC12K_utils import *
from Instruccion import Instruccion

class CargarEjecutor(Instruccion) :

	def __init__(self):
		self.init()
		
	def init(self):
		self.name = "CargarEjecutor"
	
	def run(self, params, interprete):
		logging.debug("Ejecutando CargarEjecutor. Parametros: " + str(params))
		#folder: desde el principio hasta el último '/'.
		#module: desde el ultimo '/' hasta el '.' del py
		#disp: nombre de la clase: igual que el module o dado por el usuario.
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
		logging.debug("Ejecutando CargarEjecutor help")
		res = ""
		res+= "************************** Cargar Ejecutor ******************************\n"
		res+= "CargarEjecutor <path> : Carga el modulo .py dado en el path y la clase\n"
		res+= "con el mismo nombre que el modulo.\n"
		res+= "CargarEjecutor <path> <classname> : Carga el modulo .py dado en el path y\n"
		res+= "la classe de nombre dado.\n"
		res+= "****************************************************************************"
		return res