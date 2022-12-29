
def SomaIdade(string):

    soma =0
    for ix in range(len(string)):
        numero = int(string[ix])
        soma = soma + numero
    sint=str(soma)
    taman = len(sint)
    if taman == 2:
        valor = int(sint[0])+int(sint[1])
        return valor
    else :
        return sint

print(">>",SomaIdade('19991229'))
print(">",SomaIdade('20000101'))



the_string = '19991229'
soma =0
for ix in range(len(the_string)):
    numero = int(the_string[ix])
    soma = soma + numero
    #print(the_string[ix], end='-')

print("soma",soma )
sint=str(soma)

valor = int(sint[0])+int(sint[1])
print(valor)