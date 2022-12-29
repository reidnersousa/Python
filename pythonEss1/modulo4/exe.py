def fun(x):
    if x % 2 ==0:
        return 1
    else :
        return 

print(fun(fun(2)+1))
print(fun(2))
print(fun(2)+1)

def fun2(x):
    global y
    y=x*x
    return y

fun2(2)
print(y)

tup =(1,2,4,8)
tup = tup[1:-1] #(2,4)
tup =tup[0]
print("tup",tup)

print("k")

#print(ch, end="")

def any():
    print(var+1,end='')

var =1
any()
print("a",var)

def ff (inp =2 , out =3):
    return inp*out

print(ff (out=2))

def f(x):
    if x==0:
        return 0
    return x+f(x-1)

print("f")
print(f(3))
print(3+f(3-1))
print(f(2))



def oo (x):
    x+=1
    return x

x=2
x=oo(x+1)
print(x)