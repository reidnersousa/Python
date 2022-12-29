import calendar  

c = calendar.Calendar()
### primeiro representa  o dia e segundo o dia da semana 0 domingo 
for data in c.monthdays2calendar(2022, 12):
    print(data)
