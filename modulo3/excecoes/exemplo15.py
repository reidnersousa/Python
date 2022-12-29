try:
    raise Exception(1,2,3)

except Exception as e:
    print(len(e.args))
    print(e)


x=0
x +=0

print(x)