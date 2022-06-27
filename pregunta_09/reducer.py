#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

contador = 0

if __name__ == '__main__':
	lista1 = []

	for line in sys.stdin:
		key,date,val=line.split("\t")
		val=int(val)

		lista1.append((key,date,val))

		lista1.sort(key=lambda x:(x[2]),reverse=False)

	
	for elemento in lista1:		
		sys.stdout.write("{}   {}   {}\n".format(elemento[0],elemento[1],elemento[2]))
		contador +=1
		if contador == 6:
			break
				
