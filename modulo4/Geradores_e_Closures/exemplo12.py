list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


def addition(n): 
    return n + n 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 