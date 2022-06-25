#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from binhex import LINELEN
import sys

if __name__ == '__main__':

	curkey = None
	total = 0
	suma = 0	
	promedio = 0
	cuenta = 0
		
	for line in sys.stdin:
			key,val = line.split("\t")
			val = int(val)
			aux = val
			aux1 = val
			if key == curkey:
				suma += aux
				cuenta += 1
				promedio = suma / cuenta
			else:
				if curkey is not None:
					sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,promedio))
				curkey = key
				suma = val
				promedio = val
				cuenta = 1
	sys.stdout.write("{}\t{}\t{}\n".format(curkey,suma,promedio))