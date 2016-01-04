#DNSIPv6Searcher.py pequeño script para buscar direcciones IPv6 a partir de nombres de servicios o dominios (ej. www.google.es) usando busquedas DNS.

import socket
import sys
import getopt
import string
import random as rnd

def printV(line):
	global verbose
	if(verbose):
		print line

def printUsage():
	print "DNSIPv6Searcher.py usage: DNSIPv6Searcher -i infile -o outfile [options]"
	print "  -i infile: nombre del fichero con los nombres de servicio o dominio."
	print "  -o outfile: nombre del fichero estructurado de salida."
	print "  options: "
	print "    -v: verbose"
	print "    -a: añade al final del fichero de salida (si existe) los resultados de la nueva busqueda."
	print "    -b: prueba a generar url's después de acabar las url de entrada. No puede ir con -r"
	print "    -r num: prueba a generar url's de forma aletoria de un tamaño concreto. No puede ir con -b"
	print "    -m num: maximo de iteraciones para los 2 modos anteriores. 1000 por defecto"
	exit()

#Establece los parametros
def setParams():
	options, args = getopt.getopt(sys.argv[1:],'vhi:o:abr:',['verbose','help'])
	#Definir parametros por defecto
	global verbose
	global anadir
	global infilename
	global outfilename
	global bruteforce
	global random
	global maxiter
	global sizeStr
	
	verbose = False
	anadir = False
	bruteforce = False
	random = False
	maxiter = 1000000
	sizeStr = 0
	
	for opt, arg in options:
		if(opt in ('-h','--help')):
			printUsage()
		elif (opt in ('-v','--verbose')):
			printV("Verbose Mode On")
			verbose = True
		elif (opt == '-a'):
			printV("Append Mode On")
			anadir = True
		elif (opt == '-b'):	
			if(random == False):
				printV("Brute Force On")
				bruteforce = True
		elif (opt == '-r'):
			if(bruteforce == False):
				printV("Radom Mode On. Size: " + arg)
				random = True
				sizeStr = int(arg)
		elif (opt == '-i'):
			printV("Input File " + arg)
			infilename = arg
		elif (opt == '-o'):
			printV("Output File " + arg)
			outfilename = arg
		else:
			printUsage()

def peticion(url):
	try:
		addrlist = socket.getaddrinfo(url, 80, socket.AF_INET6, 0, socket.IPPROTO_TCP)	
		for addr in addrlist:
			if len(addr[4]) == 4:
				printV("Direccion IPv6 detectada: " + addr[4][0])
				ipv6addr = addr[4][0]
				return ipv6addr
	except socket.gaierror:
		pass
	
	return ""
			
def fileSearch():
	global verbose
	global infilename
	#Bucle de generacion
	infile = open(infilename,'r');

	linea = infile.readline()
	while linea != "":
		
		if(linea[-1] == '\n'):
			linea = linea[:-1]
		printV("Peticion a " + linea + " ...")
		ipv6addr = peticion(linea)
		if(ipv6addr != ""):
			outfile.write(linea + ';' + ipv6addr + '\n')
		linea = infile.readline()
		
	#Cerrar fichero
	infile.close()

def incChar(char):
	Alfabeto="abcdefghijklmnñopqrstuvwxyz0123456789-_"
	i = Alfabeto.index(char)
	i = i + 1
	carro = False
	if i==len(Alfabeto):
		i = 0
		carro = True
	return Alfabeto[i], carro

def incStr(str):
	if (len(str)==1):
		result, carro = incChar(str)
		return result, carro
	else:
		res, carro = incStr(str[1:])
		if(carro == False):
			result = str[0] + res
		else:
			res2, carro = incChar(str[0])
			result = res2 + res
		
	return result, carro
		
def bruteForce():
	printV("BruteForce")
	global maxiter
	
	name = "e4s"
	doms = [".es", ".com", ".org", ".de", ".fr", ".uk"]
	iter = 0
	while iter < maxiter:
		urlbase = "www." + name
		for ext in doms:
			url = urlbase + ext
			printV("Peticion a " + url + " ...")
			ipv6addr = peticion(url)
			if(ipv6addr != ""):
				outfile.write(url + ';' + ipv6addr + '\n')
		
		name, carro = incStr(name)
		if (carro == True):
			name = "a" + name
		
		iter = iter + 1
	
	
def randomMode():
	printV("randomMode")
	global maxiter
	global sizeStr
	
	name = ''.join(rnd.choice("abcdefghijklmnñopqrstuvwxyz0123456789-_") for _ in range(sizeStr))
	doms = [".es", ".com", ".org", ".de", ".fr", ".uk"]
	iter = 0
	while iter < maxiter:
		urlbase = "www." + name
		for ext in doms:
			url = urlbase + ext
			printV("Peticion a " + url + " ...")
			ipv6addr = peticion(url)
			if(ipv6addr != ""):
				outfile.write(url + ';' + ipv6addr + '\n')
		
		name = ''.join(rnd.choice("abcdefghijklmnñopqrstuvwxyz0123456789-_") for _ in range(sizeStr))
		
		iter = iter + 1
	
#tratamiento de args
global verbose
global anadir
global infilename
global outfilename
global bruteforce
global random

verbose = False

if len(sys.argv) >= 2:
	"Iniciando..."
	try:
		setParams()
	except getopt.GetoptError as e:
		print "Error en los parametros"
		printUsage()
		
else:
	print "Error en los parametros"
	printUsage()

printV("Parametros correctos.")
printV("Ejecutando...")

#Abrir fichero salida
if(anadir):
	outfile = open(outfilename,'a')
else:
	outfile = open(outfilename,'w')
	
fileSearch()

if(bruteforce):
	bruteForce()
if(random):
	randomMode()

outfile.close()
