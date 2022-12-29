class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        print(self)
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            
            return 1

        ret = self.__p1 + self.__p2

        self.__p1 =self.__p2
        self.__p2 =ret
        #self.__p1, self.__p2 = self.__p2, ret
        return ret
   
   
    def __str__(self):
        #return '{0}'.format(self.__p2)
        return '%d'%(self.__p2)

        #return f'{self.__p2} '


for i in Fib(5):
    print(i)

f = Fib(5)
print(f)