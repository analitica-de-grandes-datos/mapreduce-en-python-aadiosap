#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.split("   ")for z in data]
pregunta_4=[[z[0],z[1],z[2].replace("\n","")] for z in data]



import sys

for letra,fecha,numero in pregunta_4:
	sys.stdout.write("{}\t{}\t{}\n".format(letra,numero,fecha))