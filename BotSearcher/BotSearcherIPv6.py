from SC12K_utils import *

logging.info('Consola iniciada en Lo:Suyo:Seria:Una:IP:To:Chula (o.ip.v.4)')
filename = './configuration.xml'
logging.info('Cargando repositorio de instrucciones en interprete. Fichero:' + filename)
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


