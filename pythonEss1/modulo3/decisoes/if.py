x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
    

##################################
####    Exemplo
######
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")



x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")
else:
    print("else not be executed because x>8 ,because x=10 so don´t executed")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")



print("outtro exemplo")

x = 10

if x == 10:  # True
    print("x == 10")
else :
    print("posso ter esse else")

if x > 15:  # False
    print("x > 15")
#else :  
 ##   print("nao posso ter esse else ") por conta do elif 

elif x > 10:  # False
    print("x > 10")

###else: ### nao posso fazer isso pois causa um erro sintaxe  
   ### print("else will not be executed")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")



######################################################
###
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
