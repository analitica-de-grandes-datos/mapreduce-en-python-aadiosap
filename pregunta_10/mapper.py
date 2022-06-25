#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.replace("\n","").split("\t") for z in data]
data=[[z[1].split(","),z[0]] for z in data]
pregunta10=[z for z in data]



import sys

for key,value in pregunta10:
	for letra in key:
		sys.stdout.write("{}\t{}\n".format(letra,value))