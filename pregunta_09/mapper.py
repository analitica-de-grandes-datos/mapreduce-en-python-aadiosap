#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.replace("\n","").split("   ") for z in data]
pregunta9=[[z[0],z[1],z[2]] for z in data]



import sys

for key,date,value in pregunta9:
	sys.stdout.write("{}\t{}\t{}\n".format(key,date,value))