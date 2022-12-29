frase='Ten animals I slam in a net'

lista =list(frase)
print(lista)
lista_sem_Branco =''.join(lista)
print("lista",lista_sem_Branco)

frase_Quebrada=frase.split()
frase_sem_Branco = ''.join(frase_Quebrada)
print(frase_Quebrada)
frase_Quebrada.reverse()
print(frase_Quebrada)
frase_sem_Branco_reverse =''.join(frase_Quebrada)

print("a",frase_sem_Branco_reverse)
print("b",frase_sem_Branco)



palavraReversa = frase_sem_Branco_reverse.upper()
palavraOriginal = frase_sem_Branco.upper()
print(palavraOriginal)
print(palavraReversa)