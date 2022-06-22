#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.split(",")for z in data]
columna=[[z[0],z[1]] for z in data]



import sys

for key,value in columna:
	sys.stdout.write("{}\t{}\n".format(key,value))