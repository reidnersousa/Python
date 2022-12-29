for i in range(10):
    print("The value of i is currently", i)
print("\n")

array=[10,11,12,13,14]
for i in range(0, 5):
    print(array[i])
    print("The value of i is currently", i)


### a função pode aceita 3 valores o primeiro e qual o valor inical do i , o segundo e ate onde vai e 
# o terceiro e qtd de incrmento 
for i in range(2, 8, 3):
    print("The value of i is currently", i)

## nao vai executar
for i in range(1, 1):
    print("The valuesss of i is currently", i)
# nao vai executar pois o primeiro elemento tem que ser menor que segundo 
for i in range(2, 1):
    print("Não fui executado The value of i is currently", i)


power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
