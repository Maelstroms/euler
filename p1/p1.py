"""
Project Euler problem 1
"""

def p1(limit):
	count = 0
	sum = 0
	while count < limit:
		if count % 3 == 0 or count % 5 == 0:
			sum += count
		count += 1
	return sum

print "p1"
print p1(10) # should be 23
print p1(20) # should be 78
print p1(1000)

def multis(limit):
	count = 3
	sum = 0
	while count < limit:
		sum += count
		count += 3
	count = 5
	while count < limit:
		if count % 3 != 0:
			sum += count
		count += 5
	return sum
	
print "multis"
print multis(10)
print multis(20)
print multis(1000)