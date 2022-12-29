def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")


happy_new_year()
happy_new_year(False)



def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
x=boring_function()
print(x)
print("This lesson is boring...")



### funçõa com lista

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s


print(list_sum([5, 4, 3]))
#   vai da erro 
# print(list_sum(5))
