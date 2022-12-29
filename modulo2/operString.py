str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)



# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
print(ord("b"))
print(ord("α"))

# Demonstrating the chr() function.

# print(chr(97))        ### deu erro
# print(chr(945))       ### deu erro


####        Strings como sequências: indexação


# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end='-')

print()

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Slices

alpha = "abdefg"

print("=",alpha[0:0]) ## imprimir nada 
print("=",alpha[0:1])
print("=",alpha[1:1])
print("[3:]",alpha[3:])
print("[:3]",alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#   Os loops Operadores in e not in .
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# A primeira diferença importante não lhe permite 
# utilizar a instrução del para remover qualquer coisa de uma string.

# As strings de Python não têm o método append() - não se pode expandi-las de forma alguma.

#   com a ausência do método append() , o método insert() é ilegal, também:


alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)


# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
print(">>>",min("cccabbbccc"))

# Demonstrating min() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))

print()
# Demonstrating max() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

print("tamanho ",len("\n\n"))

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)


for ch in "abc":
    print(chr(ord(ch) + 1), end='')


print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
#print("αβγδ".capitalize())


s1 = 'Where are the snows of yesteryear?'
s2 = s1.split() # transforma uma string numa alista ou seja cada palavra 
#vai ser uma sting  dentro de uma lista 
print(type(s2))
print(s2)
print(s2[-2])
print(s2[-2][0])
print(s2[-2][1])

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list) ### vai juntar os elementos da lista numa string 
p = ' '.join(the_list)
print(s)
print(p)


s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)