"""
Project Euler problem 14.
find which number under 1000000 has the longest chain.
"""

def evens(n):
	return n/2


def odds(n):
	return (3*n + 1)
	

length = 0
num = 3

while num <= 1000000:
	count = 0
	colatz = num
	while colatz > 1:
		count += 1
		if colatz % 2 == 0:
			colatz = evens(colatz)
		else:
			colatz = odds(colatz)
	if count > length:
		length = count
		longest = num
	print "longest chain is currently", length
	print "starting num was ", longest
	print "just tested ", num
	num += 1