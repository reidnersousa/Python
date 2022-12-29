x='\\\\'
print(len(x))   ### imprimir 2 

#y='\\\'
##print(len(y))

#z='\'          da erro tem que ser duas barras 
#print(len(z))

print(__name__)

class A:
    def __init__(self ,v):
        self.__a=v+1


a=A(0)
print(a.__a)