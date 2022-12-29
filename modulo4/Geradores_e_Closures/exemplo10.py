two = lambda: 2
sqr = lambda x: x * x    ## o quadrado
pwr = lambda x, y: x ** y


print(sqr(3))
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

