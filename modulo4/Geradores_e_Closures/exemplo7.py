the_list = []
ll=[]

for x in range(10):
    ll.append(x)
    the_list.append("par" if x % 2 == 0 else "impar")

print(ll)
print(the_list)
