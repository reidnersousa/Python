# Caesar cipher.
text = "AAAAC"
cipher = ''
for char in text:
    if not char.isalpha(): # se o caratere atual não for alfabético 
        continue    # ignorá-lo
    char = char.upper() 
    code = ord(char) + 1 # obter o codigo da letra e incremental-lo em um 
    if code > ord('Z'): # se o codigo resultante tive "deixado" o alfabeto latino (se for maior do que o codigo Z)
        code = ord('A') #altera-lo para o codigo A
    cipher += chr(code) # anexar o caractere recebido ao fim da mensagem 

print(cipher)


# Caesar cipher - decrypting a message.
#cipher = 'a'
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


# Numbers Processor.

line = "aaaa"
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
