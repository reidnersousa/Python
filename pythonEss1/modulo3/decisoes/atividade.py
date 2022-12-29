c0=15
i=0
while  c0 !=1:
    if c0 % 2 == 0:
        c0 =c0/2
        print(c0)
    else :
        c0 = 3*c0+1
        print(c0)
    i=i+1
print("passos",i)


nums =[]
vals = nums
vals.append(1)

print(len(vals),len(nums))
print(vals,nums)

val =[0,1,2]
print(val)
val[0],val[1]=val[1],val[2]
print(val)


my_list =[1,2,3]
for v in range (len(my_list)):
    my_list.insert(1,my_list[v])