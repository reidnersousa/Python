first_number = 0 ##
second_number = 0### 

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")


### com try e except 

#first_number = int(input("Enter the first number: "))
#second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")


try:
    print("1")
    x = 1 / 0
    print("2") ### nao foi executador 
except:
    print("Oh dear, something went wrong...")

print("3")


try:
    x = 5 # 0 'a'
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("We're done")

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexingError:
    print("index")
except:
    print("some")



try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")


def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")


import math

x = 1 # 
assert x >= 0.0
#as assertions não substituem as exceções nem validam os dados - são seus suplementos.

x = math.sqrt(x)

print(x)


#O programa corre sem falhas se introduzir um valor numérico válido maior 
# ou igual a zero; caso contrário, ele para e emite a seguinte mensagem:

