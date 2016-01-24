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