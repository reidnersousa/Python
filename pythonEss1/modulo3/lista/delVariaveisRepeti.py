my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

lista =[1,2,3,4,6,7,8,9,10]
listaFinal=[]
i=0
for number in my_list:
    i=0
    for number2 in lista:
        if number == number2:
            print("number",number,"number2",number2)
            del my_list[number2]
    
print("The list with unique elements only:")
print(my_list)

