# A primeira e mais clara distinção entre listas e tuples é a
# sintaxe utilizada para as criar - os tuples preferem usar parêntesis curvos, 
# enquanto as listas gostam de ver parêntesis retos, 
# embora também seja possível criar um tuple a partir de um conjunto de valores separados por vírgulas.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print("a",elem)


my_tuple = (1, 10, 100, 1000)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)




var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)


one_elem_tuple_1 = ("one", "three","estou criando uma tupla")    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.

print(one_elem_tuple_1)
one_elem_tuple_1 =("two","estou criando uma nova tupla ou seja estou apgando os dados ante..")
print(one_elem_tuple_1)
print(type(one_elem_tuple_1))

my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple = "guitar"    # The TypeError exception will be raised.
print(my_tuple)
