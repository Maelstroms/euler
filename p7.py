"""
Seventh problem of project Euler
"""


def primey(place):
	primes = [2]
	count = 2
	while len(primes) < place:
		for i in range(len(primes)):
			if count % primes[i] == 0:
				count += 1
				break
		else:
			primes.append(count)
			count += 1
	#print primes
	return primes[place-1]

	
print primey(6)
print primey(100)
print primey(10001)