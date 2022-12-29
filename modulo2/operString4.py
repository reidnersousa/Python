# Test examples here.
print('alpha' == 'alpha')
print('alpha' != 'Alpha')


print('alpha' < 'alphabet')


print('beta' > 'Beta')


# Test examples here.
print('10' == '010')#False
print('10' > '010') ##True
print('10' > '8')   #False
print('20' < '8')   #True
print('20' < '80')  #True
print('20' > '80')  #False
#print('10'>10)## vai da erro


# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

# Test code here.
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
print(itg,flt)


s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
#print(s3[1])


s1 = '12'
i = int(s1) # se s1 fosse 12.8 não daria certo daria um erro 
print(i)
s2 = str(i)
f = float(s2)
print(s1 == s2)
