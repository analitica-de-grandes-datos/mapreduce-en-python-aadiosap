#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
	for line in sys.stdin:
		lista = line.split(" ")
		sys.stdout.write("{},1\n".format(lista[0]))