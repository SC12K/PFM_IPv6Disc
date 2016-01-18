#modulo unificado
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./Interfaz')
sys.path.append('./Core')
#Función para realizar prints solo cuando debug este activado.

import logging
tlevel=logging.DEBUG
"""
Nivel a escribir en el fichero de log.
"""
#tlevel=logging.INFO
#tlevel=logging.WARNING
logging.basicConfig(filename='BotSearcherIPv6.log',
                    format='[%(asctime)s]\t%(levelname)s\t: %(message)s',
                    level=tlevel)

def cargarClase(path, modulename, classname):
    """
    Carga una clase dado un path, un modulo y un nombre de clase.
    
    @param path: carpeta donde se encuentra el modulo.
    @type path: string
        
    @param modulename: Fichero *.py que contiene la clase..
    @type modulename: string
        
    @param classname: Nombre de la clase.
    @type classname: string
        
    @returns: Devuelve None si hay algun problema. En otro caso devuelve la
    clase.
    """
    try:
        if (path != "" and path != "./"):
            sys.path.append(path)
        module = __import__(modulename)
        class_ = getattr(module, classname)
        return class_
    except Exception as E:
        print E
        class_ = None
        return class_

def pathToFolderModule(path):
    """
    Calcula la carpeta y el modulo dado un path completo.
    
    @param path: direccion donde esta el modulo a cargar.
    @type path: string
        
    @returns: Devuelve la carpeta y el modulo especificados en el path.
    """
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
    """
    Normaliza una direccion IPv6. Por ejemplo:
    
    2001::1 (->) 2001:0000:0000:0000:0000:0000:0000:0001
    
    @param addr: direccion IPv6
    @type addr: string
        
    @returns: Devuelve la misma direccion normalizada.
    """
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
from GestorDeEjecucion import GestorDeEjecucion

global interprete
"""
Variable global para referenciar el interprete.
"""
interprete = Interprete()


#Gestor de Sondas
global GdS
"""
Variable global para referenciar el Gestor de Sondas.
"""
GdS = GestorDeSondas()


global GdE
"""
Variable global para referenciar el Gestor de Ejecucion.
"""
GdE = GestorDeEjecucion()