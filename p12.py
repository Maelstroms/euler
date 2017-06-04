"""
Problem 12 of project Euler
Find the first triangle number with 500 divisors

Think about trying to use prime factorization or coprime property
or at least figure it out.
"""

from math import sqrt

def primey(limit):
	markers = limit/10000
	primes =[2]
	if markers > 1:
		possibles = []
		for j in range(markers):
			if 10000*j == 0:
				possibles.append(xrange(3,10000*1,2))
			else:
				possibles.append(xrange((10000*j)+1, (10000*(j+1))+1,2))
	else:
		possibles = [xrange(3,limit,2)]
	for k in possibles:
		for p in primes:
			k = [y for y in k if y % p != 0]
		while min(k)**2 <= limit*2:
			primes.append(min(k))
			k = [x for x in k if x % min(k)**2 != 0 and x % min(k) != 0]
		# FOR LOOP ALERT, i IS USED HERE!!!!
	return primes


def tri_num_gen(place):
	num = 1
	sum = 0
	while num <= place:
		sum += num
		num += 1
	return sum

#print "test tri gen ", tri_num_gen(7)
#print tri_num_gen(20000)

primes = primey(75000)
print primes
def prime_factorization(num):
	primes
	fac = num
	bigdiv = 1
	for p in primes:
		div = 0
		while fac % p == 0:
			fac = fac/ p
			#print "fac ", div, "of ", fac, "is ", p
			div += 1
			if fac % p != 0:
				div += 1
				bigdiv *= div
				

	return bigdiv

print prime_factorization(10)
print prime_factorization(20)
print prime_factorization(360)



tri = 3
triup =3
while prime_factorization(tri) <= 500:
	tri += triup
	triup += 1
	print "tri here: ", tri
	print "num of divisors ", prime_factorization(tri)
	print "next step: ", triup
print tri
