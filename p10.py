"""
Tenth problem of project Euler
Find the sum of all the primes below two million.
"""
from math import sqrt
import time
start_time = time.time()

def prime_sum(limit):
	markers = limit/10000
	sum = 2
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
		while min(k)**2 <= limit:
			sum += min(k)
			primes.append(min(k))
			k = [x for x in k if x % min(k)**2 != 0 and x % min(k) != 0]
		# FOR LOOP ALERT, i IS USED HERE!!!!
		for i in k:
			sum += i
	return sum

	
#print prime_sum(10)
#print prime_sum(100)
#print prime_sum(10000) #This is the biggest limit I am willing to go in a single computation
#print prime_sum(100000)
print prime_sum(2000000)


print "this program took: ", time.time() - start_time, "seconds"
# with range: 4.63551902771