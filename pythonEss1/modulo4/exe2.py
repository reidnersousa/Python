a =[i for i in range (-1,2)]
print(a)


lst =[[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c]% 2 != 0:
            print("#",lst[r][c])

print(lst)


my_list =[1,2]
print("A",my_list[-1])

for v in range(2):
    #print("v ",v)
    print("my",my_list[v])
    print("antes        ",my_list)
    my_list.insert(-1,my_list[v])
    print("dentro do for",my_list)

print(">>",my_list)
# insert(idx, value)


my_a=[x*x for x in range(5) ]

def fuaaa(lst):
    del lst [lst[2]]
    return lst

print(my_a)
print(fuaaa(my_a))


def fa(a,b):
    return b**a

# print(fa(b=2,2))      #erro

a=1
b=0
a=a^b
b=a^b 
a=a^b
print(a,b)
p=1^0
print(p)

print("a","b","c",sep="sep")


