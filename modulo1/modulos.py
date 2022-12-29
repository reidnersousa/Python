import math

## from module import *  ## importa tudo do modulo 

def sin(x):
    if 2 * x == pi:
        print(x)
        print(2*x)
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))


from math import pi


# print(math.e) # vai da erro por que so to importand pi e nao math todo