#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("data.csv", "r").readlines()
data=[z.split(",")for z in data]
columna=[z[0][9:11] for z in data]

import sys

for key in columna:
	sys.stdout.write("{}\t1\n".format(key))