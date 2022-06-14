#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
data = open("C:\Users\user\Desktop\DOC ESPECIALIZACION\ANALITICA DE GRANDES DATOS\LABORATORIOS\mapreduce-en-python-aadiosap\pregunta_01\mapper.py", "r").readlines()
data=[z.split(",")for z in data]
credit_score=[z[2]for z in data]



import sys

for valor in credit_score:
	sys.stdout.write("{}\t1\n".format(valor))

#if __name__ == "__main__":
#
#    for line in sys.stdin:
#        for word in line.split():
#            sys.stdout.write("{}\t1\n".format(word))
