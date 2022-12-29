variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

print(variable_1)
print(variable_2)



lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

## Ex4
print("kskskskks")
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
