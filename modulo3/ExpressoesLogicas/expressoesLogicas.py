# Example 1:
var =1
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))
####
#           Operadores bitwise
####

# & (e comercial) - conjunção bitwise;
# | (barra) - disjunção bitwise;
# ~ (til) - negação bitwise;
# ^ (acento circunflexo) - bitwise exclusive ou (xor).


i = 15
j = 22
log = i and j
print(log)


bit = i & j

print(bit) ##


logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)



var = 17
var_right = var >> 1  #  17//2 =8
var_left = var << 2   #  17*4 =68
print(var, var_left, var_right)
