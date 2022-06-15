#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("credit.csv", "r").readlines()
data=[z.split(",")for z in data]
purpose_amount=[[z[3],z[4]] for z in data]



import sys

for key,value in purpose_amount:
	sys.stdout.write("{}\t{}\n".format(key,value))