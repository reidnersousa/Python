pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1  estou dizendo e a chave do dic
print(item_1)    # outputs: soil        aqui ele retorna qual o valor da chave

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water

print(pol_eng_dictionary.values())
print(pol_eng_dictionary.keys())


phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}

a ={}
print(a)
a ["a"]=''
print(a)
a["a"]="aaa"
print(a)


#

##      percorrendo o dic
##

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)

#
#
#       verifica se um elementoe esta dentro 
#

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")

####
###
###     copiando um elemento         usando o metodo copy()


pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

# O programa irá imprimir 6 para o ecrã. Os elementos do tuple tup foram “descompactados” nas a, b, e c variáveis.
tup = 1, 2, 3
print(type(tup))
a, b, c = tup
# a,b,c,d =tup ### vai da erro pois espera 4 variaveis e a tupla so tem 3 ou seja não vai atribuir para cada um 
print(a,b,c,tup)


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

#for item in (d1, d2):
for key, value in d1.items():
    print("Pol/Eng ->", key, ":", value)
    d3[key] =value

for key, value in d2.items():
    print("Pol/Eng ->", key, ":", value)
    d3[key] =value


print(d3)


##
##3
####     melhor forma de fazer

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

###
        #    convento uma lista numa tupla
###
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list) ## conventeu para uma tipo tupla
print(t)
print(type(t))

##
##   conventendo uma tuple e  um dict
###

colors = (("green", "#008000"), ("blue", "#0000FF"))

print(colors[0][0])
print(colors[0][1])
print(colors[0][0][0])

colors_dictionary=dict(colors)
print(type(colors_dictionary))
print(colors_dictionary)


#######

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(my_dictionary)

print(copy_my_dictionary)

####3
#####

colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)