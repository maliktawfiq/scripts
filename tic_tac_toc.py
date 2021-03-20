from random import randrange
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
    # and prints it out to the console.


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    dec = input("Enter Your Choice.......... :")
    if len(dec) == 1 and dec != '0':
        dec = int(dec)
        for row in range(3):
            for col in range(3):
                if board[row][col] == dec:
                    board[row][col] = 'O'
        return 1
    else:
        return 0
    # checks the input and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    lst = []
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) == int:
                lst.append((row, col))
    return lst
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

    # The function analyzes the board status in order to check if
    count = 0
    win = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                count += 1
        if count == 3:
            win = True
        count = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == sign:
                count += 1
        if count == 3:
            win = True
        count = 0
    count1 = 0
    count2 = 0
    for i in range(3):
        if board[i][i] == sign:
            count1 += 1
        if board[2-i][i] == sign:
            count2 += 1
    if count1 == 3 or count2 == 3:
        win = True
    return win
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    free = make_list_of_free_fields(board)
    valid = len(free)
    if valid > 0:
        num = randrange(valid)
        row, col = free[num]
        board[row][col] = "X"


    # The function draws the computer's move and updates the board.
board[1][1] = 'X'
free = make_list_of_free_fields(board)
flag = True
winX = False
winO = False
display_board(board)
while(len(free)):
    if flag == True:
        if enter_move(board):
            display_board(board)
            winO = victory_for(board, 'O')
            flag = False
        else:
            print("Enter A Valid number please")
            enter_move(board)
    else:
        draw_move(board)
        display_board(board)
        winX = victory_for(board, 'X')
        flag = True
    if winX == True:
        print("computer won")
        break
    elif winO == True:
        print("you won")
        break
if winX == False and winO == False:
    print("Tie!!")
