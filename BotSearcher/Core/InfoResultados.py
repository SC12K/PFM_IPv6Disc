from logger import *

class InfoResultados(object):
    """
    Convencion de comunicacion de resultados entre la sonda y los modulos de
    escritura.
    
    Funcionan a traves de un diccionario de etiquetas con la siguiente forma:
   
    [(<IP>,(<etiqueta1>,(<tipo1>,<valor1>)), (<etiquetaN>,(<tipoN>,<valorN>))...
    ,(<IP>,(<etiqueta1>,(<tipo1>,<valor1>)), (<etiquetaN>,(<tipoN>,<valorN>))...
    ,(<IP>,(<etiqueta1>,(<tipo1>,<valor1>)), (<etiquetaN>,(<tipoN>,<valorN>))...
    ,(<IP>,(<etiqueta1>,(<tipo1>,<valor1>)), (<etiquetaN>,(<tipoN>,<valorN>))...
    (<IP>,(<etiqueta1>,(<tipo1>,<valor1>)), (<etiquetaN>,(<tipoN>,<valorN>))...]
    
    Sera el modulo de escritura de destino el encargado de modelar esta
    informacion y adaptarla a su formato concreto.
    """
    
    def __init__(self):
        """
        Inicializa la lista de resultados como un diccionario. Usara de Clave la
        IP.
        """
        
        self._listaDeResultados = list()
        self._sondaOrigen = ["NoConocido", "NoConocido", "NoConocido"]
    
    def identificarSonda(self, nombre, dispIPv6, ejec):
        """
        Permtite identificar la sonda de origen para poder distingirla
        posteriormente. Permite identificar tambien el dispensador y el
        ejecutor usados.
        
        Modifica el atributo _sondaOrigen : [<sonda>, <dispensador>, <ejecutor>]
        No es un campo obligatorio. Por defecto tiene valor:
        ["NoConocido", "NoConocido", "NoConocido"]
        """
        
        self._sondaOrigen[0] = nombre
        self._sondaOrigen[1] = dispIPv6
        self._sondaOrigen[2] = ejec
    
    def anadirIP(self, ipv6):
        """
        Anade una IPv6 a la lista de resultados y inicializa su diccionario de
        etiquetas, a la espera de ser rellenado.
        
        @param ipv6: Direccion ipv6 a anadir.
        @type ipv6: string
        """
        
        self._listaDeResultados.append([ipv6], dict())
        
    def anadirAtributo(self, etiqueta, tipo, valor):
        """
        Anade una etiqueta al ultimo registro IPv6 registrado.
        """
        
        registro = self._listaDeResultados[-1][1]
        registro[etiqueta] = [tipo, valor]
    
    def getListaDeResultados(self):
        """
        Devuelve la lista de resultados para ser tratada.
        """
        
        return self._listaDeResultados