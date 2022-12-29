import time

timestamp = 1572879180

### gmtiem criar um objeto struct_time
st = time.gmtime(timestamp)


## convert um objeto struct time ou truple numa string 
print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
