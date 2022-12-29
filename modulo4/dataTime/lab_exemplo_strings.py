


from datetime import timedelta
from datetime import date
from datetime import datetime
import time

od = date(2020,11,4)

d = date(2020, 11, 4)
#print(d.strftime('%Y/%m/%d'))

com_mim=datetime(2020,11,4,14,53,00)
print(com_mim.strftime('%Y/%m/%d %H:%M:%S'))
print(com_mim.strftime('%y/%B/%d %H:%M:%S %p '))
print (d.strftime("%a, %Y %b %d "))
print (d.strftime("%A, %Y %B %d "))
print (d.strftime("Weekday : %w "))
print (d.strftime("Day of the year : %j"))
print (d.strftime("Week number of the year : %W"))


print("\noutro exemplo")

my_date = date(2020, 9, 29)
print("Year:", my_date.year) # Year: 2020
print("Month:", my_date.month) # Month: 9
print("Day:", my_date.day) # Day: 29


from datetime import time

t = time(14, 39)
print(t.strftime("%H:%M:%S"))