def display_board(board):
    b=board
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    di={"A":"1","B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9}
    print("+-------+-------+-------+\n|       |       |       |\n|  ",di["A"],"  |  ",di["B"],"  |  ",di["C"]," |\n|       |       |       |")
    print("+-------+-------+-------+\n|       |       |       |\n|  ",di["D"],"  |  ",di["E"],"  |  ",di["F"],"  |\n|       |       |       |")
    print("+-------+-------+-------+\n|       |       |       |\n|  ",di["G"],"  |  ",di["H"],"  |  ",di["I"],"  |\n|       |       |       |\n+-------+-------+-------+")
    print(type(di))

    #for key, value in di.items():
    #    print(" chave->", key, "valor", value)
    #print(di["A"])

display_board(5)


def enter_move(board):
    return None
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.

def make_list_of_free_fields(board):
    return None
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    return None

def draw_move(board):

    return None
    # The function draws the computer's move and updates the board.

