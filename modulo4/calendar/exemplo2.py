import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.


import calendar  

c = calendar.Calendar(calendar.SUNDAY)
## 0 é segunda-feira
for weekday in c.iterweekdays():
    print(weekday, end=" ")


import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    #print(date, end=" ")
    print(date)


import calendar  

c = calendar.Calendar()
## os quatro primeiros zero representam 28/10/2019(segunda-feira) ate 31/10/2019(quinta-feira)
# o ultimo sero  e 01/12/2019(domingo)
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
