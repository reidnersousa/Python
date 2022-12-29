
import calendar
#print(calendar.calendar(2020)) ## não precisa do print para imprimir 
calendar.prcal(2020)


#Calendário para um mês específico

print(calendar.month(2020, 11))


import calendar as c
import calendar as a
c.setfirstweekday(c.MONDAY)
c.prmonth(2022, 12)


a.setfirstweekday(a.SUNDAY)
a.prmonth(2022,12)
a.prmonth(2018,12)
import calendar
print(calendar.weekday(2022, 12, 24))  ## retorna 5 pois 24 cair num sabado
print(calendar.weekday(2018, 12, 24))  ## retorna 0 pois 24 cair numa segunda-feira 


print(calendar.weekheader(2))
print(calendar.weekheader(1))
print(calendar.weekheader(3))
