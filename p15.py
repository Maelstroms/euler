"""Problem 15 of project Euler
How many moves are there in a 20 x 20 grid? only right and down

in a 2x2 grid there are only 4 moves
6 different 4 move combinations

you can only have 400 moves
down is 0
right is 1

Investigate the efficiency of the problem. Curse at recursive stupidity.
"""
import time
import math

# (n+n)! / (n! * n!)


right = "right"
down = "down"

rights= 0
downs = 0

def grid_moves(right, down):
	paths = 0
	if (right == 0 or down == 0):
		return 1
		
	else:
		return grid_moves((right - 1), down) + grid_moves(right, (down - 1))

now = time.clock()

#print grid_moves(5,5)
#print grid_moves(10,10)
#print grid_moves(15,15)
#print grid_moves(20, 20)

#What makes this run faster?

def catalancalc(n):
	return math.factorial(n+n) / (math.factorial(n) * math.factorial(n))

#print catalancalc(5)
print catalancalc(20)
print "time elapsed = " + str(time.clock() - now) + "seconds"