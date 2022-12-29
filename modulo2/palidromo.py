#string = "aba"
string='Ten animals I slam in a net'

stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print ("SIM")
else:
    print ("NAO")