# This file is where we will implement the runtime logic for our chess game

from piecesetup import *
from util_functions import *

def initialize_board():

    # initialize the board  
    board[0][0] = Rook([0,0], False)
    board[0][1] = Knight([0,1], False)
    board[0][2] = Bishop([0,2], False)
    board[0][3] = Queen([0,3], False)
    board[0][4] = King([0,4], False)
    board[0][5] = Bishop([0,5], False)
    board[0][6] = Knight([0,6], False)
    board[0][7] = Rook([0,7], False)

    # add all of the black pawns
    for i in range(8):
        board[1][i] = Pawn([1,i], False)

    board[7][0] = Rook([7,0], True)
    board[7][1] = Knight([7,1], True)
    board[7][2] = Bishop([7,2], True)
    board[7][3] = Queen([7,3], True)
    board[7][4] = King([7,4], True)
    board[7][5] = Bishop([7,5], True)
    board[7][6] = Knight([7,6], True)
    board[7][7] = Rook([7,7], True)

    # add all of the white pawns
    for i in range(8):
        board[6][i] = Pawn([6,i], True)


def main():

    print("Welcome to ASCII Chess!")

    initialize_board() # add pieces to our board

    print_board() # print our starting board
    
    user_move = "" # the string where user enters their move
 
    player = "white" # string supplement 
    white = True # keep track of whose turn it is
    success = False # keep track of whether the player made a successful move
    white_king_position = [7,4]
    black_king_position = [0,4]

    while(user_move != "exit"):
        print(f"It is {player}'s turn!")

        made_legal_move = False

        if in_check(white_king_position, True) and in_checkmate(True):
            print("Black wins by checkmate!")
            return 

        if in_check(black_king_position, False) and in_checkmate(False):
            print("White wins by checkmate!")
            return 

        
        while(not success):

            # only one should be true at the same time, so can just run both 
            if(in_check(white_king_position, True)):
                print("White king is in check. You must make a move that stops it")
                rint(f"Here are possible moves{list_possible_moves(True)}")

            if(in_check(black_king_position, False)):
                print("Black king is in check. You must make a move that stops it")
                print(f"Here are possible moves{list_possible_moves(False)}")

            user_move = input("Enter piece position and where you want to move it in the following format: 'a7a6' " )

            if(user_move == "exit"):
                print("Thanks for playing terminal chess!")
                return

            if parse_command(user_move) == False:
                print("Input incorrectly formatted. Try again.")
                continue

            current_position, new_position = parse_command(user_move)

            if board[current_position[0]][current_position[1]] == "":
                print("Make sure you're starting index has a piece on it.")
                continue

            curr_piece = board[current_position[0]][current_position[1]]

            print(current_position, new_position)
            print(curr_piece)

            # check that they move the right side
            if curr_piece.is_white != white:
                print("Cannot Move Opponent's Pieces!")
                continue

            # if the move was successful, we end our loop
            made_legal_move = curr_piece.move(new_position)

            if made_legal_move:
                break

            print("The attempted move was illegal. Try again")

        # keep track of the position of our kings so we can look for checks
        # faster than iterating through each piece to check where it went
        if 'King' in type(curr_piece).__name__ and player == "white":
            white_king_position = new_position

        elif 'King' in type(curr_piece).__name__ and player == "black":
            black_king_position = new_position
        
        # after a move has been made, reprint our board
        print_board()

        # switch our boolean and its respective string supplement
        if player == "white":
            player = "black"
            white = False
        else:
            player = "white"
            white = True

    return 


if __name__ == "__main__":
    main()

