

import calendar as c

c.prcal(2020)




import calendar
  
# providing firstweekday = 0
obj = calendar.Calendar(2022)
numero_de_semanas_num_ano=0
for i in range (1,13):
    for week in obj.monthdayscalendar(2022, i):
            if week[0]==0:
                #print(week)
                numero_de_semanas_num_ano -=1
            
                #print(">",week)
            numero_de_semanas_num_ano +=1

print(numero_de_semanas_num_ano)


def quanto_Semanas_anuais(ano):
    objeto=calendar.Calendar(ano)
    semanas_ano=0
    for i in range (1,13):
        for week in objeto.monthdayscalendar(ano, i):
            if week[0]==0:
                #print(week[0],week[1],week[2])
                #print(week)
                semanas_ano -=1
            
                
            semanas_ano +=1
    return semanas_ano

ss=quanto_Semanas_anuais(2022)
print(ss)

ss1=quanto_Semanas_anuais(2026)
print(ss1)