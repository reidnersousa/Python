def strange_list_fun(n):
    strange_list = []
    l =[]
    for i in range(0, n):
        print(i)
        strange_list.insert(-1, i)
        l.insert(0,i)
        print("l=",l)    
    return strange_list

print(strange_list_fun(5))



l =[]
l.insert(1,2)
print(l)
l.insert(1,3)
print(l)