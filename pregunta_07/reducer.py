#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
	lista1 = []

	for line in sys.stdin:
		key,val1,val2=line.split(",")
		val2=int(val2)

		lista1.append((key,val1,val2))

		lista1.sort(key=lambda x:(x[0],x[2]),reverse=False)

	for elemento in lista1:
		sys.stdout.write("{}   {}   {}\n".format(elemento[0],elemento[1],elemento[2]))