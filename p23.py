""" Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
import time

#there must be a pattern that allows more efficient discovery of factors.
# Maybe some gains from saving previous numbers and factoring in their multiples?
def list_divisors(num):
  divisors = []
  x = 1
  while x < num:
    if num % x == 0:
      divisors.append(x)
    x += 1
  return divisors


def abundant_numbers(limit):
  x = 0
  found_abundants = []
  while x < limit:
    divs = sum(list_divisors(x))
    if divs > x:
      found_abundants.append(x)
    x+=1
  return found_abundants


#actually doing opposite
def sums_of_abundant_numbers(limit):
  found_abundants = []
  abundant_sums = []
  solution = []
  x = 0
  while x < limit:
    if sum(list_divisors(x)) > x:
      found_abundants.append(x)
      for a in found_abundants:
        if (a + x) < limit:
          abundant_sums.append(a + x)
        else:
          solution.append(x)
    x+=1
  return solution


def filter_others(limit):
  rocks = sums_of_abundant_numbers(limit)
  return sum(l3)

start = time.time()

#print sums_of_abundant_numbers(200)
#print filter_others(200)
#print abundant_numbers(28123)
print sum(sums_of_abundant_numbers(28123))

end = time.time()
print(end - start)
