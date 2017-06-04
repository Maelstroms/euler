"""
Problem 16 of Project Euler
What is the sum of the digits of 2^1000
"""

import time


def digit_sum(n):
	sum = 0
	sep = str(n)
	for l in range(len(sep)):
		d = sep[l]
		sum += int(d)
	return sum

now = time.clock()

print digit_sum(2**1000)

print "time elapsed: " + str(time.clock()-now) + "seconds"

#10000001000010100111010000110011