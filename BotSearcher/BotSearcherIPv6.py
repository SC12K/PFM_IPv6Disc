from SC12K_utils import *

logging.info('Consola iniciada en Lo:Suyo:Seria:Una:IP:To:Chula (o.ip.v.4)')
filename = './configuration.xml'
logging.info('Cargando repositorio de instrucciones en interprete. Fichero:' + filename)
interprete.cargarRepertorio(filename)
logging.info('Repositorio cargado.')
logging.info('Cargando gestor de sondas.')
GdS.cargar()
logging.info('Gestor de sondas cargado.')

interprete.ejecutarBucle()

