import calendar  

c = calendar.Calendar()
## os quatro primeiros zero representam 28/10/2019(segunda-feira) ate 31/10/2019(quinta-feira)
# o ultimo sero  e 01/12/2019(domingo)
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
print("\n")
for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")
print("\n")
for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")
print("\n")
for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")