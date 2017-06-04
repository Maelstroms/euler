"""
Fourth problem of project Euler
"""

def finder():
	count = 0
	num = 20
	check = 20
	while count < 9000000000000000:
		if num % check == 0:
			check -= 1
			if check == 2:
				return num
		elif num % check != 0:
			check = 20
			count += 1
			num +=20

		
print finder()