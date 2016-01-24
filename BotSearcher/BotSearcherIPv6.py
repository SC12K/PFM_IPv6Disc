"""
Fichero de entrada al programa. Carga la configuracion inicial y ejecuta el
interprete. Cuando el interprete se cierra, guarda el Gestor De Sondas antes de
salir.
"""
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./Interfaz')
sys.path.append('./Core')
from logger import *
from GestorDeModulos import *
from GestorDeSondas import *
from GestorDeResultados import *
from GestorDeEjecucion import *
from Interprete import *

def main():
    """
    Funcion main. Recibe como parametro el fichero de configuracion.
    """
    logging.info('Consola iniciada en Lo:Suyo:Seria:Una:IP:To:Chula (o.ip.v.4)')
    filename = './configuration.xml'
    ficherodecarga = './modulos.xml'
    """
    Nombre del archivo de configuracion.
    """
    logging.info('Cargando repositorio de instrucciones en interprete. Fichero:'
                 + filename)
    interprete = Interprete()
    interprete.cargarRepertorio(filename)
    logging.info('Repositorio cargado.')
    logging.info('Cargando gestor de Modulos.')
    GdM.cargarXML(ficherodecarga)
    logging.info('Gestor de Modulos cargado.')
    logging.info('Cargando gestor de sondas.')
    GdS.cargarXML(ficherodecarga)
    logging.info('Gestor de sondas cargado.')
    logging.info('Cargando gestor de resultados.')
    GdR.cargarXML(ficherodecarga)
    logging.info('Gestor de resultados cargado.')
    interprete.ejecutarBucle()
    logging.info('Interprete Cerrado')
    logging.info('Guardando datos en el xml')
    logging.info('Creando Nodo Raiz')
    root = xmlparser.Element('CargaInicial')
    xml_GdM = GdM.guardarXML()
    logging.info('Guardando Gestor de Modulos')
    root.append(xml_GdM)
    logging.info('Guardando Gestor de Sondas')
    xml_GdS = GdS.guardarXML()
    root.append(xml_GdS)
    logging.info('Guardando Gestor de Resultados')
    xml_GdR = GdR.guardarXML()
    root.append(xml_GdR)
    logging.info('Cerrar')
    tree = xmlparser.ElementTree(root)
    tree.write('modulos.xml')
    

if __name__ == "__main__":
    main()