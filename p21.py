def list_divisors(num):
  divisors = []
  x = 1
  while x < num:
    if num % x == 0:
      divisors.append(x)
    x += 1
  return divisors

#sum(list)

def all_amicable_numbers(limit):
  count = 1
  solution = []
  while count < limit:
    first = list_divisors(count)
    sum_first = sum(first)
    if sum_first < limit and sum_first > count:
      second = list_divisors(sum_first)
      sum_second = sum(second)
      if count == sum_second:
        solution.append(sum_first)
        solution.append(sum_second)
    count += 1
  return solution

#print list_divisors(220)
print sum(all_amicable_numbers(10000))

