"""
Problem 9 of project Euler
Find the Pythagorean triplet who's elements add up to 1000
"""
from math import sqrt

def integer_checker(num):
	if num - int(num)== 0:
		return True
	else:
		return False


def pytha_trip(start):
	count = 0
	csq =(start**2)
	trips = []
	while count < csq:
		count += 1
		a = sqrt(count)
		b = sqrt(csq - count)
		if integer_checker(a) and integer_checker(b):
			if a != 0 and b != 0:
				trips.append([int(a),int(b),start])
	if trips != []:
		return trips
	else:
		return False

def lt_seperator(ind, lt):
	pass

def is_sum_1000(nums):
	if (nums[0]+ nums[1]+ nums[2]) == 1000:
		return nums
	return False

def product(nums):
	return (nums[0]*nums[1]*nums[2])
	

def put_together():
	cstart = 330
	while cstart < 1000:
		pita = pytha_trip(cstart)
		#print pita
		if pita != False:
			for i in pita:
				k = is_sum_1000(i)
				#print k
				if k != False:
					return product(k)
			else:
				cstart += 1
		else:
			cstart+= 1
	return "something is wrong"

print put_together()


