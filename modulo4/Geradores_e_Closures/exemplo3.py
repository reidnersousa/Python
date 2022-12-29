def fun(n):
    for i in range(n):
        return i


m=fun(5)

print(m)


def fun2(n):
    for i in range(n):
        yield i


o = fun2(5)
print(o)