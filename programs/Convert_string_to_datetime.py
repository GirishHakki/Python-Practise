# solution 1 using dateutil module

from dateutil import parser

date_time = parser.parse("Oct 14 1997 7:15AM")

print(date_time)
print(type(date_time))