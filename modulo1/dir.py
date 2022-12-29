import math

for name in dir(math):
    print(name, end="\t")



from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)
print()
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


from math import e, exp, log
print("\n")
#e → uma constante com um valor que é uma aproximação do número de Euler (e)
#exp(x) → encontrar o valor de ex;
#log(x) → o logaritmo natural de x
#log(x, b) → o logaritmo de x para base b
#log10(x) → o logaritmo decimal de x (mais preciso do que log(x, 10))
#log2(x) → o logaritmo binário de x (mais preciso do que log(x, 2))
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))



#ceil(x) → o teto de x (o menor inteiro maior ou igual a x)
#floor(x) → o piso de x (o maior número inteiro menor ou igual a x)
#trunc(x) → o valor de x truncado a um número inteiro (tenha cuidado - não é equivalente a um teto ou piso)
#factorial(x) → devolve x! (x tem de ser um integral e não um negativo)
#hypot(x, y) → devolve o comprimento da hipotenusa de um triângulo de ângulo retângulo com o comprimento das pernas igual a x e y 
#(o mesmo que sqrt(pow(x, 2) + pow(y, 2)) mas mais preciso)
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))


## gerando numeros aleatorios

from random import random

for i in range(5):
    print(random())


print()
from random import random, seed

seed(0)

for i in range(5):
    print(random())

