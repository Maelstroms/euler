"""
Fourth problem of project Euler
"""

def string_reverse(string):
	rev = ""
	mark = []
	for i in range(len(string)):
		mark.append(i)
	mark.reverse()
	for i in mark:
		rev += string[i]
	return rev
	


print string_reverse("9010308")
palindromes = []
count1 = 999
count2 = 999

while count2 > 100:
	sum = count1 * count2
	track = str(sum)
	kcart = string_reverse(track)
	if track == kcart:
		palindromes.append(sum)
		print ("count1 is" , count1)
		print ("count2 is", count2)
		print ("together they are", track)
	else:
		if count1 == 100:
			count2 -= 1
			count1 = count2
	count1 -= 1

print max(palindromes)