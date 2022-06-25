#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
	for line in sys.stdin:
		val, key, date= line.split("\t")
		date = date.replace("\n","")      
		sys.stdout.write("{}\t{}\t{}\n".format(val,date,key))