from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#randrange(end)
#randrange(beg, end)
#randrange(beg, end, step)
#randint(left, right)

#range(end)
#range(beg, end)
#range(beg, end, step)


from random import randint

for i in range(10):
    print(randint(1, 10), end=',')



from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))
print(sample(my_list,3))


# choice(sequence)
# sample(sequence, elements_to_choose)
# A primeira variante escolhe um elemento "aleatório" a partir da sequência de input e devolve-o.

# O segundo constrói uma lista (uma amostra; em inglês, uma sample) 
# que consiste no elemento elements_to_choose “sorteado” a partir da sequência de input.