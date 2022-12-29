from datetime import date
### isoweekday a semana vai de 1 ate  7 onde 1 é segunda-feira e 7 e domingo

d = date(2019, 11, 4)
print(d.isoweekday())



from datetime import date
### weekday a semana vai de 0 ate  6 onde 0 é segunda-feira e 6 e domingo
d = date(2019, 11, 4)
print(d.weekday())
