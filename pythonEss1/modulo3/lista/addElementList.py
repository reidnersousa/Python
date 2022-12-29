numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

### no ultimo lugar da lista

numbers.append(4)  # colcando o numero 4 no ultimo lugar 

print(len(numbers))
print(numbers)

###
        ## location =0  e valor =222 
numbers.insert(0, 222) # adicionar num lugar especifico 
print(len(numbers))
print(numbers)

#

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)