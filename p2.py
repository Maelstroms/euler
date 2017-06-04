"""
problem 2 of project Euler
"""

def fib(place):
	if place <= 0:
		return 0
	elif place == 1:
		return 1
	return fib(place - 1) + fib(place - 2)
def p2(limit):
	wow = 0
	p = 0
	sum = 0
	while wow < limit:
		wow = fib(p)
		if wow % 2 == 0:
			sum += wow
		p += 1
	return sum

print p2(4000000)