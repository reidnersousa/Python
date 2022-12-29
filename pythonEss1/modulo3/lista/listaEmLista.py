from pprint import pprint


row = []
WHITE_PAWN = 1
for i in range(8):
    row.append(WHITE_PAWN)

pprint(row)
print()
board = []
EMPTY =0
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#print(board)
pprint(board)

print()
board = [[EMPTY for i in range(8)] for j in range(8)]
pprint(board)