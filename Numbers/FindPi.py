

my_pi=1
for i in range(1,15000):
	my_pi+=((1/pow(16,i)) * ((4/(8*i + 1)) - (2/(8*i + 4)) - (1/(8*i + 5)) - (1/(8*i + 6))))
	print my_pi
print my_pi

