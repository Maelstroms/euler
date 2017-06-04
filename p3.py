"""
third problem of project Euler
This takes forever to check the rest of the numbers.
the answer is 6857
need to find a better way to cut it off if it starts getting out of hand.
Thought about trying to make a union of two lists.
"""
from math import sqrt


def big_prime_fac(num):
	primes =[2]
	count = 3
	while count <= (sqrt(num)):
		for i in range(len(primes)):
			if count % primes[i] == 0:
				count += 1
				break
		else:
			if num % count == 0:
				primes.append(count)
			count += 1
	primes.reverse()
	for i in primes:
		if num % i == 0:
			return i


print big_prime_fac(600851475143)
