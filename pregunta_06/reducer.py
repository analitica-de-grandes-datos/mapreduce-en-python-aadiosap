#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from binhex import LINELEN
import sys

if __name__ == '__main__':

	curkey = None
	total = 0
	maximo = 0	
	minimo = 0
		
	for line in sys.stdin:
			key,val = line.split("\t")
			val = float(val)
			aux = val
			aux1 = val
			if key == curkey:
				if aux > maximo:
					maximo = aux
				if aux1 < minimo:
					minimo = aux1
			else:
				if curkey is not None:
					sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo,minimo))
				curkey = key
				maximo = val
				minimo = val
	sys.stdout.write("{}\t{}\t{}\n".format(curkey,maximo,minimo))
