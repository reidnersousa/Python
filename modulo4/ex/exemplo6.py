x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)


t=(1,2,3,4)
t=t[-2:-1]
print(t)
x=t[0]
print(x)
t=t[-1]

print(t)

class A :
    A=1
    def __init__(self):
        self.a=0


print(hasattr(A,"A"))  ### pq true 
print(type(A))