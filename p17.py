"""
Problem 17 of Project Euler
what is the sum of the letters that are used to write out the numbers 1 to 1000?
"""

onesplace = { 0:"", 1 : "one", 2 :"two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",  7 : "seven" , 8 : "eight", 9 : "nine", 10 : "ten", 11: "eleven", 12: "twelve", 13:"thirteen", 14: "fourteen", 15:"fifteen", 16: "sixteen", 17:"seventeen", 18:"eighteen", 19: "nineteen" }
tensplace= { 2: "twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7 :"seventy", 8:"eighty", 9:"ninety" }




def number_char_count(limit):
	total = 0
	counter = 1
	while counter < limit +1:
		#print ("counter at" + str(counter))
		if counter == 1000:
			total += len("onethousand")
		elif counter < 1000 and counter > 99:
			total += len("hundred")
			progress = str(counter)
			total += under_hundred(int(progress[0]))
			if int(progress[1]+progress[2]) != 0:
				total += 3 + under_hundred(int(progress[1]+progress[2]))
		
		
		else:
			total += under_hundred(counter)
		counter +=1
	return total

def under_hundred(num):
	progress = 0
	if num > 19:
		work_in_progress = str(num)
		progress += len(tensplace[int(work_in_progress[0])])
		progress += len(onesplace[int(work_in_progress[1])])
	else:
		progress += len(onesplace[num])
	return progress
			
#print number_char_count(5)
#should be 19
#print number_char_count(10)
#should be 39
#print number_char_count(15)
#should be 73 or 74, too lazy to check
#print number_char_count(115)
#1089 maybe?
#print number_char_count(999)
print number_char_count(1000)
