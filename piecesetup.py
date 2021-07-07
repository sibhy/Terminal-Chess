from util_functions import *


# create our Pawn class
class Pawn():
 
    # if our position is (-1,-1), the piece has been captured
    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        if is_white:
            self.moves = POSSIBLE_DIRECTIONS_PAWN_WHITE
        else:
            self.moves = POSSIBLE_DIRECTIONS_PAWN_BLACK
        self.moves_limit = 1

    # TODO: 2.1 - implement the move method for Pawns
    # INFO: we want the row number of the pawn to increase by 1 when a Pawn is
    # white and the row number to decrease when the Pawn is black. Also, if 
    # the move brings us to the end of the board, call the promote method on 
    # the pawn's position and exit the function. Otherwise, update the board 
    # with our pawn.
    
    def move(self, new_position):
        # update self.position based on the position of the pawn
        # check if we reach the last rows, if so, call the promote method on 
        # our current position

        if is_this_king_in_check(self.is_white):
            return False

        if self.is_white:
            if(is_valid_position(self.position, new_position, POSSIBLE_DIRECTIONS_PAWN_WHITE, 1)):

                board[self.position[0]][self.position[1]] = ""
                old_piece = board[new_position[0]][new_position[1]]
                board[new_position[0]][new_position[1]] = self

                if is_this_king_in_check(self.is_white):
                    board[self.position[0]][self.position[1]] = self
                    board[new_position[0]][new_position[1]] = old_piece
                    return False

            self.position = new_position
            return True

            if(self.position[0] == 0 or self.position[0] == 7):
                    self.promote()

            return True

        else: 

            if(is_valid_position(self.position, new_position, POSSIBLE_DIRECTIONS_PAWN_BLACK, 1)):
                
                board[self.position[0]][self.position[1]] = ""
                old_piece = board[new_position[0]][new_position[1]]
                board[new_position[0]][new_position[1]] = self

                if is_this_king_in_check(self.is_white):
                    board[self.position[0]][self.position[1]] = self
                    board[new_position[0]][new_position[1]] = old_piece
                    return False

            self.position = new_position
            return True

            if(self.position[0] == 0 or self.position[0] == 7):
                    self.promote()

            return True

    # TODO 2.2: Write the promote method to add a Queen if the pawn reaches the end
    def promote(self):
        board[self.position[0]][self.position[1]] = Queen(self.position, self.is_white)

    def __repr__(self):
        if(self.is_white == False):
            return "B_Pawn"
        else:
            return "W_Pawn"

class Queen():

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        self.moves = POSSIBLE_DIRECTIONS_QUEEN
        self.moves_limit = 99


    # TODO: 3.1 write the method move such that if our new_position is 
    # reachable based on our current position, that we change our current to that
    # otherwise, return false. Ensure that the board is updated accordingly.

    def move(self, new_position):

        if(is_valid_position(self.position, new_position, self.moves)):
            board[self.position[0]][self.position[1]] = ""
            old_piece = board[new_position[0]][new_position[1]]
            board[new_position[0]][new_position[1]] = self
            if is_this_king_in_check(self.is_white):
                board[self.position[0]][self.position[1]] = self
                board[new_position[0]][new_position[1]] = old_piece
                return False
            self.position = new_position
            return True
            
        return False

    def __repr__(self):
        if(self.is_white == False):
            return "B_Queen"
        else:
            return "W_Queen"


# TODO: 4.1, following the same structure as our previous classes, create the 
# King class with the same constructor as the previous two.
class King():

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        self.in_check = False
        self.moves = POSSIBLE_DIRECTIONS_KING
        self.moves_limit = 1

    # TODO: 4.2, write the function move such that if our new_position is 
    # reachable based on our current position, that we change our current to that
    # otherwise, return false. Write this code using top-down-design, assuming that 
    # the is_valid_position method has been implemented.

    def move(self, new_position):

        if(is_valid_position(self.position, new_position, self.moves)):
            board[self.position[0]][self.position[1]] = ""
            old_piece = board[new_position[0]][new_position[1]]
            board[new_position[0]][new_position[1]] = self

            if is_this_king_in_check(self.is_white):
                board[self.position[0]][self.position[1]] = self
                board[new_position[0]][new_position[1]] = old_piece
                return False

            self.position = new_position
            return True
            
        return False

    def __repr__(self):
        if(self.is_white == False):
            return "B_King"
        else:
            return "W_King"

    
# TODO: 5.1, just as we did for the King class, create the Knight class with 
# the same structure 

class Knight():

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        self.moves = POSSIBLE_DIRECTIONS_KNIGHT
        self.moves_limit = 1

    # TODO Q6, using the directions defined in part 1, write the move method
    # for Knights. 
    # Hint: Use a similar structure to the Kings method.
    def move(self, new_position):

        if(is_valid_position(self.position, new_position, self.moves)):
            board[self.position[0]][self.position[1]] = ""
            old_piece = board[new_position[0]][new_position[1]]
            board[new_position[0]][new_position[1]] = self
            if is_this_king_in_check(self.is_white):
                board[self.position[0]][self.position[1]] = self
                board[new_position[0]][new_position[1]] = old_piece
                return False
            self.position = new_position
            return True
            
        return False

    def __repr__(self):
        if(self.is_white == False):
            return "B_Knight"
        else:
            return "W_Knight"

# TODO: 7, Write the classes for Bishops and Rooks, using the same structure 
# as before. Implement the move method for both pieces.

class Bishop():

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        self.moves = POSSIBLE_DIRECTIONS_BISHOP
        self.moves_limit = 99

    # TODO Q6, using the directions defined in part 1, write the move method
    # for Knights. 
    # Hint: Use a similar structure to the Kings method.
    def move(self, new_position):

        if(is_valid_position(self.position, new_position, self.moves)):
            board[self.position[0]][self.position[1]] = ""
            old_piece = board[new_position[0]][new_position[1]]
            board[new_position[0]][new_position[1]] = self
            if is_this_king_in_check(self.is_white):
                board[self.position[0]][self.position[1]] = self
                board[new_position[0]][new_position[1]] = old_piece
                return False
            self.position = new_position
            return True
            
        return False


    def __repr__(self):
        if(self.is_white == False):
            return "B_Bishop"
        else:
            return "W_Bishop"

class Rook():

    def __init__(self, position, is_white):
        self.position = position
        self.is_white = is_white
        self.moves = POSSIBLE_DIRECTIONS_ROOK
        self.moves_limit = 99
    
    def move(self, new_position):
        

        if(is_valid_position(self.position, new_position, self.moves)):
            board[self.position[0]][self.position[1]] = ""
            old_piece = board[new_position[0]][new_position[1]]
            board[new_position[0]][new_position[1]] = self
            if is_this_king_in_check(self.is_white):
                board[self.position[0]][self.position[1]] = self
                board[new_position[0]][new_position[1]] = old_piece
                return False
            self.position = new_position
            return True
            
        return False

    def __repr__(self):
        if(self.is_white == False):
            return "B_Rook"
        else:
            return "W_Rook"







    



        



            











        