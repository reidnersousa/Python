def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
## A conclusão é óbvia - a alteração do valor do parâmetro não 
## se propaga fora da função (em qualquer caso, não quando a variável 
## é uma escalar, como no exemplo).


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)



### aqui alterou
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

### mas se alterar uma lista identificada pelo parâmetro 
### (nota: a lista, não o parâmetro!), a lista irá refletir a alteração.


### fica ligado nisso

var = 2
def mult_by_var(x):
    return x * var


print(mult_by_var(7))    # outputs: 14
######################
def mult(x):
    var = 5
    return x * var


print(mult(7))    # outputs: 35

##########################
def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # outputs: 49


def adding(x):
    var = 7
    return x + var


print(adding(4))    # outputs: 11
print("s",var)    # NameError


def message():
    alt = 1
    print("Hello, World!")


# print(alt) ## vai da errro 



a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)



a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)
