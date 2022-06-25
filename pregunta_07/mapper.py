#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.split("   ")for z in data]
pregunta_7=[[z[0],z[1],z[2].replace("\n","").replace("\t","")] for z in data]
pregunta_7=[[z[0],z[1],int(z[2])] for z in data]


import sys

for letra,fecha,numero in pregunta_7:
	sys.stdout.write("{}\t{}\t{}\n".format(numero,letra,fecha))