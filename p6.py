"""
Problem 6 of project Euler
"""

def diference_squares(num):
	ra = range(num + 1)
	sum_squares = 0
	sum_squared = 0
	for i in ra:
		sum_squared += i
		sum_squares += (i **2)
	sum_squared **= 2
	dif = sum_squared - sum_squares
	return dif
	
print diference_squares(100)