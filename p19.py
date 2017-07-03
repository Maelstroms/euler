import time
from datetime import date
import datetime

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
"""

"""
day of the week:

0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday
"""

# print time.time()
# print date.today()
# print date.fromordinal(693596)
# date.isoweekday()
#date.isocalendar()



#How many days between two dates
#requires lists, [Y, M, D]
def days_between_dates(start, end):
  begin_date = date(start[0],start[1],start[2]).toordinal()
  end_date = date(end[0],end[1],end[2]).toordinal()
  #first_jan_1900 = date.fromordinal(693596)
  return end_date - begin_date

def number_of_sundays_starting_months(start, end):
  begin_date = date(start[0],start[1],start[2]).toordinal()
  end_date = date(end[0],end[1],end[2]).toordinal()
  solution = 0
  while begin_date <= end_date:
    x = date.fromordinal(begin_date)
    if x.weekday() == 6 and x.day == 1:
      solution += 1
    begin_date +=1
  return solution

#print days_between_dates([1901,01,01], [2000,12,31])
print number_of_sundays_starting_months([1901,01,01], [2000,12,31])








