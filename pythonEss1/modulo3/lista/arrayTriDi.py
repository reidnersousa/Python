#Arrays tridimensionais

from pprint import pprint

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#pprint(rooms)

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1



# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

pprint(table)
print()
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

print()
# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

pprint(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
