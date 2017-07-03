def factorial(place):
  fac = 1
  while place > 0:
    fac = fac * place
    place -= 1
  return fac

def sum_of_fac_digits(place):
  x = factorial(place)
  y = [int(d) for d in str(x)]
  solution = 0
  for dg in y:
    solution += dg
  return solution

print sum_of_fac_digits(100)


