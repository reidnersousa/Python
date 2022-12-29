def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)



#### usando scope global ele vai torna o var =2 global logo var =1  não e alterado por var=1 
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
