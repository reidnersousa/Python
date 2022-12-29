from datetime import datetime

date1=datetime(2019,11,22,11,11,11)
date2=datetime(2019,11,22,0,0,0)

print(date1-date2)


class A:
    def __init__(self):
        pass


a=A(1)
print(hasattr(a,'A'))