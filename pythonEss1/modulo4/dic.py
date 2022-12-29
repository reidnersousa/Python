dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


## print(phone_numbers['president'])    ## vai da erro pois o elemento nao esta na dicionario


##3 uma forma de ver se o elemento esta no dicionairo

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])


######
#######     Como utilizar um dicionário: modificar e adicionar valores
######
print("\n\n")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
dictionary['cat'] = 'minou' # troquei o chat por minou
print(dictionary)


#
#       Adicionar uma nova chave
#   
#   Adicionar um novo par key-value a um dicionário é tão simples como alterar um valor - 
##  basta atribuir um valor a uma nova chave, previamente inexistente.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'  ## add um novo valor e uma nova chave 
print(dictionary)

##
##
##  atualizar o dict caso não tem dado para atualizar ele criar um novo

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

#
##  Remover uma chave
##
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

###
###
###     remover o ultimo elemento 
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

