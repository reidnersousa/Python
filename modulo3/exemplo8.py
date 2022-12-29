class SuperOne:
    pass


class SuperTwo(SuperOne):
    pass

### não posso colocar para herda duas classes; pois SuperOne ja foi herdado por 
## SuperTwo logo nao posso fazer assim :
#class Sub(SuperOne, SuperTwo):
class Sub(SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
