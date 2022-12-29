from calendar import isleap
 
def is_year_leap(year):
    
    if isleap(year):
        return True
        print('É bissexto')
    else:
        return False
        print('Não é bissexto')



test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")



def days_in_month(year, month):
    #test_results = [False, True, True, False]
    if month ==2 :
       
        reposta=is_year_leap(year)
        if reposta is True:
            return 29
        else:
            return 28
    if month ==1:
        return 31
    if month == 11:
        return 30
    else :
        return None
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")





n =11
######
###         Primo
#####
def ePrimo(n):
    mult=0
    for count in range(2,n):
        if (n % count == 0):
        #    print("Multiplo de",count)
            mult += 1

    if(mult==0):
       # print(n,"primo")
        return True
    else:
      #  print("Tem",mult," multiplos acima de 2 e abaixo de",n)
        return False

print(ePrimo(n))


for i in range(1, 20):
	if ePrimo(i + 1):
			print(">>",i + 1, end=" ")
print()



def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

