#modulo unificado
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./Interfaz')
sys.path.append('./Core')
#Función para realizar prints solo cuando debug este activado.


def printD(str):
	if debug:
		print str
		
def cargarClase(path, modulename, classname):
	try:
		if (path != "" and path != "./"):
			sys.path.append(path)
		module = __import__(modulename)
		class_ = getattr(module, classname)
		printD(dir(class_))
	except Exception as E:
		print E
		class_ = None
	return class_
	
def pathToFolderModule(path):
		pathParts =  path.rsplit('/',1)
		print pathParts
		if len(pathParts) > 1 :
			folder = pathParts[0] + "/"
			module = pathParts[1].split('.',1)[0]
		else :
			module = pathParts[0].split('.',1)[0]
			folder = "./"
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

#Flag de debug para printD
global debug
debug = False

