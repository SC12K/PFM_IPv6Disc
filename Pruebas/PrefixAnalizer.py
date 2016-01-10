#Analizador de Prefijos
#Saca estadisticas de los prefijos usados

def NormalizePart(part):
	if(len(part)==4):
		pass
	else:
		for _ in range(4-len(part)):
			part = "0" + part
		
	return part
	
def NormalizeAddr(addr):
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
	
	return addrNorm[:-1]
	



#main
estadisticas = dict()

#extraer la direcciones ipv6 y normalizar:
infile = open("test.txt", "r")
linea = infile.readline()

addrList = []

while linea != "\n" and linea != "":
	liean_div = linea.split(";")

	addrNorm = NormalizeAddr(liean_div[1])
	
	addrList = addrList + [addrNorm]
	
	linea = infile.readline()

addrAnt = ""
addrListNR = []
for addr in sorted(addrList):
	if(addr != addrAnt):
		addrListNR = addrListNR + [addr]
		addrAnt = addr

print len(addrList)
print len(addrListNR)

for addr in addrListNR:
	#nos quedamos con los 4 primeros bloques (el prefijo)
	#4 + 1 + 4 + 1 + 4 + 1 + 4 = 19
	#prefix = addr[:19]
	acum = ""
	for c in addr:
		acum = acum + c
		if(c != ":"):
			if(acum in estadisticas):
				estadisticas[acum]+=1
			else:
				estadisticas[acum]=1
	
	
	
#dibuja estadisticas y las guarda en fichero csv
f = open("./estadisticas.csv", "w")
f.write("Prefix;Times;Long\n")

for i in range(40):
	for key in sorted(estadisticas.keys()):
		if len(key) == i:
			#print key + ''.join(' ' for _ in range(20 - len(key))) + "--> " + str(estadisticas[key])
			f.write(key + ";" + str(estadisticas[key]) + ";" + str(len(key)) + "\n")
	
