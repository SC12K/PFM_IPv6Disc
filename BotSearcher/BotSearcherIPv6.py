import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('./Interfaz')
from Interprete import Interprete

interprete = Interprete()
interprete.cargarRepertorio('./configuration.xml')
interprete.ejecutarBucle()