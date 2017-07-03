import json
practice = ["MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER","MARIA","SUSAN","MARGARET","DOROTHY","LISA","NANCY","KAREN"]

points = {'A': 1,
'B': 2,
'C': 3,
'D': 4,
'E': 5,
'F': 6,
'G': 7,
'H': 8,
'I': 9,
'J': 10,
'K': 11,
'L': 12,
'M': 13,
'N': 14,
'O': 15,
'P': 16,
'Q': 17,
'R': 18,
'S': 19,
'T': 20,
'U': 21,
'V': 22,
'W': 23,
'X': 24,
'Y': 25,
'Z': 26}


def import_names():
  with open('p022_names.txt', 'r') as f:
    read_data =f.read()
  lst =json.loads(read_data)
  lst.sort()
  return lst

def list_of_letters(lst):
  solution = list(map(list, lst))
  return solution

def letters_to_points(lst):
  count = 0
  while count < len(lst):
    convert = lst[count]
    place = 0
    while place < len(convert):
      convert[place] = points[convert[place]]
      place += 1
    lst[count] = sum(convert) * (count+1)
    count += 1
  return lst

def sum_lists(lst):
  solution = list(map(sum, lst))
  return solution

# nms = practice
nms = import_names()
listy = list_of_letters(nms)
pointy = letters_to_points(listy)
print sum(pointy)



