# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#my_list[start:end]
# start é o index do primeiro elemento incluído no slice;
# end é o index do primeiro elemento não incluído no slice.


# apagando elementos com slice e del 
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# apagandos todos os elementos da lista 
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


# apagando a lista inteira 

my_list = [10, 8, 6, 4, 2]
del my_list
# print(my_list) vai da um erro de run time caso rode esse print(my list)

