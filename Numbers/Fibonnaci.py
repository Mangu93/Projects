import sys
def main(argv):
	if len(argv) != 1:
	        sys.exit('No valido')
	na = 0
	nb =1
	nc = 0
	lista_fib =[na,nb]
	while nc < int(sys.argv[1]):
		nc=na+nb
		lista_fib.append(nc)
		na=nb
		nb=nc
	for i in lista_fib:
		print i
if __name__ == "__main__":
	main(sys.argv[1:])