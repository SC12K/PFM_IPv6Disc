#!/
"""
Fichero de entrada al programa. Carga la configuracion inicial y ejecuta el
interprete. Cuando el interprete se cierra, guarda el Gestor De Sondas antes de
salir.
"""
from SC12K_utils import *

def main(argv):
    """
    Funcion main. Recibe como parametro el fichero de configuracion.
    """
    logging.info('Consola iniciada en Lo:Suyo:Seria:Una:IP:To:Chula (o.ip.v.4)')
    filename = './configuration.xml'
    """
    Nombre del archivo de configuracion.
    """
    logging.info('Cargando repositorio de instrucciones en interprete. Fichero:'
                 + filename)
    interprete.cargarRepertorio(filename)
    logging.info('Repositorio cargado.')
    logging.info('Cargando gestor de sondas.')
    GdS.cargar('modulos.xml')
    logging.info('Gestor de sondas cargado.')
    interprete.ejecutarBucle()
    logging.info('Interprete Cerrado')
    logging.info('Guardando Gestor de Sondas')
    GdS.guardar()
    logging.info('Cerrar')

if __name__ == "__main__":
    main()