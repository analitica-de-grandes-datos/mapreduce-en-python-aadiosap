#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from binhex import LINELEN
import sys



if __name__ == '__main__':

	curkey = None
	lista=[]
	
		
	for line in sys.stdin:
			key,val = line.split("\t")
			val = int(val.replace("\n",""))
			if key == curkey:
				lista.append(val)
			else:
				if curkey is not None:
					lista=sorted(lista)
					resultado=",".join(map(lambda x:str(x),lista))
					sys.stdout.write("{}\t{}\n".format(curkey,resultado))
					lista=[]					
				curkey = key
				lista.append(val)
				resultado = None
	lista=sorted(lista)
	resultado=",".join(map(lambda x:str(x),lista))			
	sys.stdout.write("{}\t{}\n".format(curkey,resultado))
	lista = []