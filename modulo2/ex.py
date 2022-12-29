def mysplit(strng):
    
    
   
    lista=[]
    s=''
    
    strng=strng+' '
    for ix in range(len(strng)):
        #print(strng[ix])
        if strng[ix]!=' ':
            s=s+strng[ix]

        else :
            lista.append(s)
            s=''
        #print(s)
        #print(lista)
    return lista
   
print(mysplit("To be or not aaaaaa "))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
#print(type(mysplit(" abc ")))
#print(mysplit(""))


txt = "I like bananas"

#x = txt.replace("bananas", "apples")
y = txt.replace(" ","")
z= txt.replace(" "," ")
#print(txt)

#print(y)
#print(z)


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
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
