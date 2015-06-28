import sys
def main(argv):
	if len(argv) != 1:
	        sys.exit('No valido')
	list_prime=[]
	d=2
	n=int(sys.argv[1])
	print "D: " +str(d)
	while d*d <= n:
		if (n % d) == 0:
			list_prime.append(d)
			n //= d
	d=d+1
	if n > 1:
		list_prime.append(n)
	for i in list_prime:
		print "Primo: " +str(i)

if __name__ == "__main__":
	main(sys.argv[1:])