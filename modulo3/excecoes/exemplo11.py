import math

try:
    print(math.sqrt(-19))
except ValueError:
    print("inf")
else:
    print("fine")