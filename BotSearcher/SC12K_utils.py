from logger import *

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

