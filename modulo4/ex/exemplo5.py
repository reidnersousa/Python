i =4

while i>0:
    i -=2
    print("*")
    if i==2:
        break
else:
    print(">*")


class A:
    def __init__(self,v):
        self._a =v+1

a=A(0)
print(a._a)


t=(1,)
t=t[0]+t[0]
print(t)


m1 ="Bond"
m2 ="James Bond"

print(m1.isalpha(),m2.isalpha())


class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(issubclass(C,A)and issubclass(C,B))


s1="string1"
s2=s1[:]

print(s1,"  ",s2)



def fun(x):
    return 1 if x % 2 != 0 else 2


print(fun(1))