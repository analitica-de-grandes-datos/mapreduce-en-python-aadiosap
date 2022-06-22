#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.split("   ")for z in data]
pregunta6=[[z[0],z[2][0:4]] for z in data]



import sys

for key,value in pregunta6:
	sys.stdout.write("{}\t{}\n".format(key,value))