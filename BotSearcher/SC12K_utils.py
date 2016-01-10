#modulo unificado
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./Interfaz')
sys.path.append('./Core')
#Función para realizar prints solo cuando debug este activado.

import logging
logging.basicConfig(filename='BotSearcherIPv6.log', format='[%(asctime)s]\t%(levelname)s\t: %(message)s', level=logging.DEBUG)

		
def cargarClase(path, modulename, classname):
	try:
		if (path != "" and path != "./"):
			sys.path.append(path)
		module = __import__(modulename)
		class_ = getattr(module, classname)
	except Exception as E:
		print E
		class_ = None
	return class_
	
def pathToFolderModule(path):
		logging.debug("pathToFolderModule path: " + path)
		pathParts =  path.rsplit('/',1)
		if len(pathParts) > 1 :
			folder = pathParts[0] + "/"
			module = pathParts[1].split('.',1)[0]
		else :
			module = pathParts[0].split('.',1)[0]
			folder = "./"
			
		logging.debug("pathToFolderModule path: " + path + "--> Folder: " + folder + " Module: " + module)
		return folder, module
		
def NormalizeAddr(addr):
	parts = addr.split(':')
	addrAux = ""
	addrLeft = ""
	count = 0
	leftcount = 0
	for part in parts:
		if part != "":
			count = count + 1
			part = NormalizePart(part)
			addrAux = addrAux + part + ":"
		else:
			addrLeft = addrAux
			addrAux = ""
		
	padding = ""
	for _ in range(8 - count):
		padding = padding + "0000:"
	
	addrNorm = addrLeft + padding + addrAux
	logging.debug("NormalizeAddr addrIn: " + addr + " --> addrOut: " + addrNorm[:-1])
	return addrNorm[:-1]
		
#importamos las clases base
from Interprete import Interprete
from GestorDeSondas import GestorDeSondas

#interprete de comandos.
global interprete 
interprete = Interprete()

#Gestor de Sondas
global GdS
GdS = GestorDeSondas()

