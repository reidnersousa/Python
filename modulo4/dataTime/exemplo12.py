from datetime import date


### formatação de datas 
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))


from datetime import time
from datetime import datetime

t = time(14, 53)
print(">",t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))



t = time(14, 53)
for j in range(10):
    for i in range(10):
        t = time(14,j,i,)
        print(t.strftime("%H:%M:%S"))