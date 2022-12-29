# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1


# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)



### Utilize break para sair de um loop, por exemplo:


text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")


# Utilize continue para ignorar a iteração atual e continuar com a próxima iteração, por exemplo:
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

 # Os loops while e for também podem ter uma cláusula else em Python. 
 # A cláusula else executa-se após o loop terminar a sua execução, 
 # desde que não tenha sido terminado por break, por exemplo.:

n = 0


while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")


##################################
# A sintaxe de range() parece como se segue: range(start, stop, step), onde:
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

