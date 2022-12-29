# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'Beta'.center(8) + ']')

print('[' + 'gamma'.center(20, '*') + ']')



# Demonstrating the endswith() method:

# A classe endswith() verifica se a string dada termina com o argumento especificado e 
# devolve True ou False, dependendo do resultado da verificação.
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demonstrating the find() method:
print("Eta".find("ta"))   # retorna 1 
print("Eta".find("mma"))  # retorna -1 caso nao tenha 


#A classe find() é semelhante a index(), que já conhece -
#procura uma substring e devolve o index de primeira ocorrência desta substring, mas:

t = 'theta'
print()
print(t.find('eta'))    #2
print(t.find('et'))     #2
print(t.find('the'))    #0
print(t.find('ha'))     #-1
print('kappa'.find('a', 2))


the_text = """the A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)




# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# O método sem parâmetros chamado isalnum() verifica se a string contém apenas 
# dígitos ou carateres alfabéticos (letras) 
# e devolve True ou False de acordo com o resultado.



# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# O método sem parâmetros chamado isalnum() verifica se a string contém apenas 
# dígitos ou carateres alfabéticos (letras) 
# e devolve True ou False de acordo com o resultado.
print()
t = 'Six lambdas'
print(t.isalnum())  #False 

t = 'ΑβΓδ'
print(t.isalnum()) #True

t = '20E1'
print(t.isalnum())  # True


# Example 1: Demonstrating the isapha() method:
# procura somente letras
print("Moooo".isalpha()) # true 
print('Mu40'.isalpha())  #False

# Example 2: Demonstrating the isdigit() method:
# procura somente digitios 
print('2018'.isdigit())     #True
print("Year2019".isdigit()) #False


# Example 1: Demonstrating the islower() method:
# procura letras que estejam escritas em minusculas retorna true se tive e false s enao tive 
print("Moooo".islower()) # False
print('moooo'.islower()) # True
print("mOOO".islower())  # False

# Example 2: Demonstrating the isspace() method:
# procura espaço em branco nas string caso tenha retorna true o opsoto false
print(' \n '.isspace())     #True
print(" ".isspace())        #True
print("mooo mooo mooo".isspace())  #False 

# Example 3: Demonstrating the isupper() method:
#Procura na String ve se todas e letras são maisuclas 
print("Moooo".isupper()) #False
print('moooo'.isupper()) #False
print('MOOOO'.isupper()) #True
