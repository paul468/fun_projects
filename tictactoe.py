import time, random

#initializing the board as a list, so items can be appended -
board=[]

#scores table for looking up the values of the 'get_winner' function for the minimax algorithm -
scores = {
    "X": -1,
    "O":1,
    "tie":0
}

#responsible for generating the shape of the board, it appends lists that contain '%' strings - 
def generate(scalex, scaley):
    for i in range(scalex):
        row = []
        for i in range(scaley):
            row.append('%')
        board.append(row)

#responsible for printing the board to the console, it prints out every character in the list in the list with a little decoration -
def render():
    for i in range(len(board)):
        for l in range(len(board[i])):
            print(board[i][l], end="-")
        print("\n| | |")
    print("\n")

#responsible for getting all the 'free' spots that are a '%' character -
def get_free_spots():
    spots = []
    for i in range(len(board)):
        for l in range(len(board[i])):
            if board[i][l] == "%":
                spots.append([i,l])
    return spots

#gets the winner of the board by comparing characters in groups of three -
def get_winner(board):
    spots = get_free_spots()
    if (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[2][0]=="X" and board[1][1] == "X" and board[0][2] == "X") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][2] == "X" and board[1][2]=="X" and board[2][2] == "X") or (board[1][0] == "X" and board[1][1]=="X" and board[1][2] == "X") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"):
        return "X"
    if (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[2][0]=="O" and board[1][1] == "O" and board[0][2] == "O") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][2] == "O" and board[1][2]=="O" and board[2][2] == "O") or (board[1][0] == "O" and board[1][1]=="O" and board[1][2] == "O") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        return "O"
    #print(spots)
    if len(spots) == 0:
        return "tie"
    return "ongoing"

#performs a move on the board and returns True if it has indeed succeeded, else it returns False, the get_free_spots function is used to look up if the move is valid -
def make_move(x,y, turn):
    spots = get_free_spots()
    if [x,y] in spots:
        if turn:
            board[x][y] = "X"
            return True
        else:
            board[x][y] = "O"
            return True
    else:
        return False

#the main minimax-algorithm. It calls itself recursively until it returns an absolute value from the 'scores' look-up table.
def minimax(board, depth, isPlayer):
    result = get_winner(board)
    if result != "ongoing":
        return scores[result]
    if isPlayer:
        bestScore = -10**10
        for i in get_free_spots():
            make_move(i[0], i[1], False)
            #render()
            score = minimax(board, depth + 1, False)
            board[i[0]][i[1]] = '%'
            bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 10**10
        for i in get_free_spots():
            make_move(i[0], i[1], True)
            #render()
            score = minimax(board, depth + 1, True)
            board[i[0]][i[1]] = '%'
            bestScore = min(score, bestScore)
        return bestScore


#responsible for calling the minimax-algo and choosing the best move.
def bestMove(turn):
    move = [-1, -1]
    BestScore = -10**10

    for i in get_free_spots():
        make_move(i[0], i[1], turn)
        score = minimax(board, 0,False)
        board[i[0]][i[1]] = '%'
        if score > BestScore:
            BestScore = score
            move = i
    print("Current calculated eval: " + str(BestScore))
    return move
    
# the function to bring it all together.
def main():
    generate(3,3)
    turn = True
    while True:
        
        render()
        #this is used to check if the previous player has performed their move yet -
        if turn:
            #separating the x and y coordinates -
            move = input("Enter your move as follows: x y >>>").split()

            #checking if the move is indeed valid and performing it -
            if not make_move((int(move[1]) - 1) % 3, (int(move[0]) - 1) % 3, turn):
                print("Invalid Move!")
            else:
                #toggling 'turn'
                turn = not turn

                #checking if the game is over yet -
                if get_winner(board) != "ongoing":
                    render()
                    if get_winner(board) == "tie":
                        print("That's a wrap! It's a tie!")
                        break
                    print(get_winner(board) + " won!")
                    break
        else:
            #it is the minimax's turn to move now -
            move = bestMove(turn)
            if not make_move(move[0], move[1], turn):
                print("Oh, the computer made an invalid move!")
            else:
                turn = not turn
                if get_winner(board) != "ongoing":
                    render()
                    if get_winner(board) == "tie":
                        print("That's a wrap! It's a tie!")
                        break
                    print(get_winner(board) + " won!")
                    break
main()