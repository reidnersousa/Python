
## essas variaveis estão sendo armazenadas no local na memoria por conta do :
### vehicles_two = vehicles_one


vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
print("list_2",list_2)
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)


squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)