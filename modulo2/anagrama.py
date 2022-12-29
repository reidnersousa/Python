palavra ="Listen"
palavra1="Silent"

x= palavra.lower()
y= palavra1.lower()

lista =list(x)
lista2=list(y)
lista.sort()
lista2.sort()
print(lista)
print(lista2)

print(lista == lista2)

def isAnagrama(string1,string2):
    x =string1.lower()
    y =string2.lower()
    lista1=list(x)
    lista2=list(y)

    lista1.sort()
    lista2.sort()
    if lista1 == lista2 :
        print("e um anagrama")
    else :
        print("nao e  anagrama ")


isAnagrama("aab","baa")