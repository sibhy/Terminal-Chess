# This file contains the utlity functions for our Chess game

from piecesetup import *
import copy
import re

# our board is an 8 x 8 2D list

# TODO: 1.1 - Using list comprehension initialize our default board and all of 
# the possible directions for each piece except the pawn. 
# Label them in the following format
# 'POSSIBLE_DIRECTIONS_{piece name}

board = [[""] * 8 for i in range(8)] # initialize our default board

POSSIBLE_DIRECTIONS_KING = [(-1,0), (1,0), (0,1), (0, -1), (1, 1), (-1, -1), 
                            (1, -1), (-1, 1)]

POSSIBLE_DIRECTIONS_QUEEN = [(-1,0), (1,0), (0,1), (0, -1), (1, 1), (-1, -1), 
                            (1, -1), (-1, 1)]

POSSIBLE_DIRECTIONS_ROOK = [(-1,0), (1,0), (0,1), (0, -1)]

POSSIBLE_DIRECTIONS_BISHOP = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

POSSIBLE_DIRECTIONS_KNIGHT = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),
                                (-2,1)]

POSSIBLE_DIRECTIONS_PAWN_BLACK = [(1,0),(1,-1),(1,1),(2,0)]

POSSIBLE_DIRECTIONS_PAWN_WHITE = [(-1,0),(-1,1),(-1,-1),(-2,0)]

ROW_LABELS = ['1','2','3','4','5','6','7','8']

COLUMN_LABELS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# function for making fields, seen in module 2 
def mk_field(val, str_len=None, is_first=False):
    prefix = ''
    if is_first:
        prefix += '|'
    if not str_len:
        print("test")
        str_len = len(val)
    return f'{prefix}{str(val).center(str_len)} |'

# TODO: define a function that lists possible moves that can be made when a 
# player is in_check. This will also be the key helper for our checkmate function

def in_checkmate(king_is_white):
    return list_possible_moves(king_is_white) == []
        
def list_possible_moves(king_is_white):
    
    possible_moves = []

    for row in range(len(board)):
        for col in range(len(board[0])):
            curr_piece = board[row][col]
            if curr_piece != "" and curr_piece.is_white == king_is_white:
                for row2 in range(len(board)):
                    for col2 in range(len(board[0])):
                        if is_valid_position(curr_piece.position, [row2,col2], curr_piece.moves, curr_piece.moves_limit):
                            
                            board[row][col] = ""
                            old_piece = board[row2][col2]
                            board[row2][col2] = curr_piece
                            
                            if not is_this_king_in_check(curr_piece.is_white):
                                possible_moves.append([curr_piece, row, col])

                            board[row2][col2] = old_piece
                            board[row][col] = curr_piece

    return possible_moves


# TODO: define a function that checks whether the given side's king is in check
# by finding the king on the board and then running in_check on it

def is_this_king_in_check(king_is_white):

    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] != ""):
                if("King" in type(board[row][col]).__name__):
                    if(board[row][col].is_white == king_is_white):
                        return in_check([row,col], king_is_white)

# TODO: define a function in_check that checks whether a given side's king 
# is in check. iterate through every square, see if it is a piece, see if it 
# is on the other side, and see if it is a valid position to get to the current 
# king's square
    

def in_check(king_position, king_is_white):

    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col]) != "":
                if(board[row][col].is_white != king_is_white):
                    if(type(board[row][col]).__name__ != "King"):
                    # print(f"Checking for checks: Piece: {type(board[row][col]).__name__} Position: {board[row][col].position}")
                        if is_valid_position(board[row][col].position, king_position, board[row][col].moves, board[row][col].moves_limit):
                            return True



# TODO: creating the generic is_valid_position function to pass in possible 
# moves and the length of movement

def is_valid_position(current_position, new_position, possible_directions, moves_limit = 99):

    
    curr_piece = board[current_position[0]][current_position[1]]
    # if our piece is a king and in check, stop it regardless 
    if 'King' in type(curr_piece).__name__ and in_check(new_position, curr_piece.is_white):
        return False
    
    # iterate through every possible direction
    for direction in possible_directions:

        # preventing aliasing - students will likely trip up on this
        temp_position = [0,0]
        temp_position[0] = current_position[0]
        temp_position[1] = current_position[1]

        # kings, pawns, and knights can only make 'one move'
        moves_made = 0

        temp_position[0] += direction[0]
        temp_position[1] += direction[1]

        # continue in that direction until we are out of the board's range
        while(temp_position[0] >= 0 and temp_position[0] < 8 and 
            temp_position[1] >= 0 and temp_position[1] < 8 and 
            moves_made < moves_limit):

            # if we hit a piece of the same color, don't allow the move
            temp_piece = board[temp_position[0]][temp_position[1]]
        
            # pieces cannot cross through pieces 
            if temp_piece != "" and not (temp_position[0] == new_position[0] and temp_position[1] == new_position[1]):
                # print("You cannot move through another piece.")
                break

            if temp_piece != "" and temp_piece.is_white == curr_piece.is_white:
                break

            # pawns cannot capture what is in front of them 
            if 'Pawn' in type(curr_piece).__name__ and temp_piece != "" and direction[1] == 0:
                # print("Pawns cannot capture pieces in front of them.")
                break  
            
            # pawns cannot go diagonally without capturing 
            if 'Pawn' in type(curr_piece).__name__ and temp_piece == "" and direction[1] != 0:
                # print("Pawns cannot move diagonally without capturing a piece.")
                break
            
            # pawns can only go 2 forward when in their original row
            
            if 'Pawn' in type(curr_piece).__name__ and curr_piece.is_white and current_position[0] != 6 and abs(direction[0]) == 2:
                # print("White Pawns can only move two squares when in row 2")
                break

                
            if 'Pawn' in type(curr_piece).__name__ and not curr_piece.is_white and current_position[0] != 1 and abs(direction[0]) == 2:
                # print("Black Pawns can only move two squares when in row 7")
                break
        
            # if we hit our new_position, return true
            if temp_position[0] == new_position[0] and temp_position[1] == new_position[1]:
                # print("Valid new position, moving piece!")
                return True
            
            # increment our position
            temp_position[0] += direction[0]
            temp_position[1] += direction[1]
           
            moves_made += 1

    # print("No possible way to reach piece.")
    return False



# TODO: write the function parse_command such that it will parse and return the 
# current position and old position in (#,#) format
def parse_command(command):

    if not re.match(r"[a-h][1-8][a-h][1-8]", command):
        return False

    curr_col = ord(command[0]) - ord('a') 
    curr_row = 8 - int(command[1])

    new_col = ord(command[2]) - ord('a')
    new_row = 8 - int(command[3])

    return (curr_row,curr_col), (new_row, new_col)

# TODO: complete the function for printing the board
def print_board():

    # these commands clear the terminal screen, leave them as is
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')


    COLUMN_WIDTH = 11

    print(mk_field("", COLUMN_WIDTH, True), end = "")

    # print each of our columns
    for i in range(len(COLUMN_LABELS) - 1):
        print(mk_field(COLUMN_LABELS[i], COLUMN_WIDTH), end = "")
    
    print(mk_field('h', COLUMN_WIDTH))

    for j in range(len(ROW_LABELS)):

        print(mk_field(ROW_LABELS[len(ROW_LABELS) - j - 1], COLUMN_WIDTH, True), end = "")
        
        # go through each row of the 
        for k in range(len(board[0]) - 1):
            
            print(mk_field(board[j][k], COLUMN_WIDTH, False), end = "")

        print(mk_field(board[j][k+1], COLUMN_WIDTH, False))


