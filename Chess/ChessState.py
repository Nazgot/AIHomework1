import pprint, copy
import copy
from .ChessPieces import ChessPieces as cp

# This class stores a game state and the possible moves for each piece
class ChessState():

    def __init__(self, heuristic = 'PIECE_VALUE', board = []):
        self.board = board
        self.value = 0
        self.heuristic = heuristic
        self.horizon = []
        self.white_win = False
        self.black_win = False
        self.final = False

    # Assign to the current state the starting board (only to be used at the start of the game)
    def base_state(self):
        self.board = [[cp.B_ROOK.value, cp.B_KNIGHT.value, cp.B_BISHOP.value, cp.B_QUEEN.value, cp.B_KING.value, cp.B_BISHOP.value, cp.B_KNIGHT.value, cp.B_ROOK.value],
            [cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value, cp.B_PAWN.value],
            [cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value],
            [cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value],
            [cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value],
            [cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value,cp.EMPTY.value],
            [cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value, cp.W_PAWN.value],
            [cp.W_ROOK.value, cp.W_KNIGHT.value, cp.W_BISHOP.value, cp.W_QUEEN.value, cp.W_KING.value, cp.W_BISHOP.value, cp.W_KNIGHT.value, cp.W_ROOK.value]]
        # The heuristic value on the initial state is 0
        self.value = 0

    # Prints the current state
    def print_board(self):
        pprint.pprint(self.board)

    # Prints the horizon of the current state
    def print_horizon(self):
        for state in self.horizon:
            state.print_board()
            print('\n')

    # Generates the horizon from the current state
    def generate_horizon(self, turn):
        # White turn management
        if turn == False:
            # Foreach movable piece, generate a state with the piece moved in every direction it can move
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.board[i][j] >= cp.W_PAWN.value and self.board[i][j] <= cp.W_KING.value:
                        self.compute_horizon(i, j)
        # Black turn management
        if turn == True:
            # Foreach movable piece, generate a state with the piece moved in every direction it can move
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.board[i][j] >= cp.B_PAWN.value and self.board[i][j] <= cp.B_KING.value:
                        self.compute_horizon(i, j)

    # Used to compute the value of this state
    def compute_value(self):
        if self.heuristic == 'PIECE_VALUE':
            self.piece_value()
        if self.heuristic == 'PIECE_VALUE_WITH_POSITIONS':
            self.piece_value_with_positions()

    def compute_horizon(self, i: int, j: int):
        piece = self.board[i][j]
        # White pawn management
        if piece == cp.W_PAWN.value:
            if self.check_bounds(i - 1, j) and self.check_empty(i - 1, j):
                self.move(piece, i, j, i - 1, j)
            if self.has_black_piece(i - 1, j - 1):
                self.move(piece, i, j, i - 1, j - 1)
            if self.has_black_piece(i - 1, j + 1):
                self.move(piece, i, j, i - 1, j + 1)
        # Black pawn management
        if piece == cp.B_PAWN.value:
            if self.check_bounds(i + 1, j) and self.check_empty(i + 1, j):
                self.move(piece, i, j, i + 1, j)
            if self.has_white_piece(i + 1, j - 1):
                self.move(piece, i, j, i + 1, j - 1)
            if self.has_white_piece(i + 1, j + 1):
                self.move(piece, i, j, i + 1, j + 1)

        # Rooks management
        if piece == cp.W_ROOK.value or piece == cp.B_ROOK.value:
            # Vertical UP Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j) and (self.check_empty(i - k, j) or self.check_color(piece, i - k, j)):
                    if self.move(piece, i, j, i - k, j) == True:
                        break
                else:
                    break
            # Vertical DOWN Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j) and (self.check_empty(i + k, j) or self.check_color(piece, i + k, j)):
                    if self.move(piece, i, j, i + k, j) == True:
                        break
                else:
                    break
            # Horizontal left Movement
            for k in range (1, 8):
                if self.check_bounds(i, j - k) and (self.check_empty(i, j - k) or self.check_color(piece, i, j - k)):
                    if self.move(piece, i, j, i, j - k) == True:
                        break
                else:
                    break
            # Horizontal right Movement
            for k in range (1, 8):
                if self.check_bounds(i, j + k) and (self.check_empty(i, j + k) or self.check_color(piece, i , j + k)):
                    if self.move(piece, i, j, i, j + k) == True:
                        break
                else:
                    break
        # Knights management
        if piece == cp.W_KNIGHT.value or piece == cp.B_KNIGHT.value:
            # Up - Left Movement
            if self.check_bounds(i - 2, j - 1) and (self.check_empty(i - 2, j - 1) or self.check_color(piece, i - 2, j - 1)):
                self.move(piece, i, j, i - 2, j - 1)
            # Up - Right Movement
            if self.check_bounds(i - 2, j + 1) and (self.check_empty(i - 2, j + 1) or self.check_color(piece, i - 2, j + 1)):
                self.move(piece, i, j, i - 2, j + 1)
            # Right - Up Movement
            if self.check_bounds(i - 1, j + 2) and (self.check_empty(i - 1, j + 2) or self.check_color(piece, i - 1, j + 2)):
                self.move(piece, i, j, i - 1, j + 2)
            # Right - Down Movement
            if self.check_bounds(i + 1, j + 2) and (self.check_empty(i + 1, j + 2) or self.check_color(piece, i + 1, j + 2)):
                self.move(piece, i, j, i + 1, j + 2)
            # Down - Right Movement
            if self.check_bounds(i + 2, j + 1) and (self.check_empty(i + 2, j + 1) or self.check_color(piece, i + 2, j + 1)):
                self.move(piece, i, j, i + 2, j + 1)
            # Down - Left Movement
            if self.check_bounds(i + 2, j - 1) and (self.check_empty(i + 2, j - 1) or self.check_color(piece, i + 2, j - 1)):
                self.move(piece, i, j, i + 2, j - 1)
            # Left - Down Movement
            if self.check_bounds(i - 1, j - 2) and (self.check_empty(i - 1, j - 2) or self.check_color(piece, i - 1, j - 2)):
                self.move(piece, i, j, i - 1, j - 2)
            # Left - Up Movement
            if self.check_bounds(i + 1, j - 2) and (self.check_empty(i + 1, j - 2) or self.check_color(piece, i + 1, j - 2)):
                self.move(piece, i, j, i + 1, j - 2)

        # Bishops management
        if piece == cp.W_BISHOP.value or piece == cp.B_BISHOP.value:
            # Left - UP Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j - k) and (self.check_empty(i - k, j - k) or self.check_color(piece, i - k, j - k)):
                    if self.move(piece, i, j, i - k, j - k) == True:
                        break
                else:
                    break
            # Left - Down Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j - k) and (self.check_empty(i + k, j - k) or self.check_color(piece, i + k, j - k)):
                    if self.move(piece, i, j, i + k, j - k) == True:
                        break
                else:
                    break
            # Right - UP Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j + k) and (self.check_empty(i - k, j + k) or self.check_color(piece, i - k, j + k)):
                    if self.move(piece, i, j, i - k, j + k) == True:
                        break
                else:
                    break
            # Right - Down Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j + k) and (self.check_empty(i + k, j + k) or self.check_color(piece, i + k, j + k)):
                    if self.move(piece, i, j, i + k, j + k) == True:
                        break
                else:
                    break
        # Kings Management
        if piece == cp.W_KING.value or piece == cp.B_KING.value:
            # Up Movement
            if self.check_bounds(i - 1, j) and (self.check_empty(i - 1, j) or self.check_color(piece, i - 1, j)):
                self.move(piece, i, j, i - 1, j)
            # Up - Right diagonal movement
            if self.check_bounds(i - 1, j + 1) and (self.check_empty(i - 1, j + 1) or self.check_color(piece, i - 1, j+ 1)):
                self.move(piece, i, j, i - 1, j + 1)
            # Right Movement
            if self.check_bounds(i, j + 1) and (self.check_empty(i, j + 1) or self.check_color(piece, i, j + 1)):
                self.move(piece, i, j, i, j + 1)
            # Down - Right diagonal movement
            if self.check_bounds(i + 1, j + 1) and (self.check_empty(i + 1, j + 1) or self.check_color(piece, i + 1, j + 1)):
                self.move(piece, i, j, i + 1, j + 1)
            # Down Movement
            if self.check_bounds(i + 1, j) and (self.check_empty(i + 1, j) or self.check_color(piece, i + 1, j)):
                self.move(piece, i, j, i + 1, j)
            # Down - Left Movement
            if self.check_bounds(i + 1, j - 1) and (self.check_empty(i + 1, j - 1) or self.check_color(piece, i + 1, j - 1)):
                self.move(piece, i, j, i + 1, j - 1)
            # Left Movement
            if self.check_bounds(i, j - 1) and (self.check_empty(i, j - 1) or self.check_color(piece, i, j - 1)):
                self.move(piece, i, j, i, j - 1)
            # Up - Left diagonal movement
            if self.check_bounds(i - 1, j - 1) and (self.check_empty(i - 1, j - 1) or self.check_color(piece, i - 1, j - 1)):
                self.move(piece, i, j, i - 1, j - 1)
        #Queen Management
        if piece == cp.W_QUEEN.value or piece == cp.B_QUEEN.value:
            # Same movements as a rook
            # Vertical UP Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j) and (self.check_empty(i - k, j) or self.check_color(piece, i - k, j)):
                    if self.move(piece, i, j, i - k, j) == True:
                        break
                else:
                    break
            # Vertical DOWN Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j) and (self.check_empty(i + k, j) or self.check_color(piece, i + k, j)):
                    if self.move(piece, i, j, i + k, j) == True:
                        break
                else:
                    break
            # Horizontal left Movement
            for k in range (1, 8):
                if self.check_bounds(i, j - k) and (self.check_empty(i, j - k) or self.check_color(piece, i, j - k)):
                    if self.move(piece, i, j, i, j - k) == True:
                        break
                else:
                    break
            # Horizontal right Movement
            for k in range (1, 8):
                if self.check_bounds(i, j + k) and (self.check_empty(i, j + k) or self.check_color(piece, i , j + k)):
                    if self.move(piece, i, j, i, j + k) == True:
                        break
                else:
                    break
            # Same movements as a bishop
            # Left - UP Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j - k) and (self.check_empty(i - k, j - k) or self.check_color(piece, i - k, j - k)):
                    if self.move(piece, i, j, i - k, j - k) == True:
                        break
                else:
                    break
            # Left - Down Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j - k) and (self.check_empty(i + k, j - k) or self.check_color(piece, i + k, j - k)):
                    if self.move(piece, i, j, i + k, j - k) == True:
                        break
                else:
                    break
            # Right - UP Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i - k, j + k) and (self.check_empty(i - k, j + k) or self.check_color(piece, i - k, j + k)):
                    if self.move(piece, i, j, i - k, j + k) == True:
                        break
                else:
                    break
            # Right - Down Diagonal Movement
            for k in range (1, 8):
                if self.check_bounds(i + k, j + k) and (self.check_empty(i + k, j + k) or self.check_color(piece, i + k, j + k)):
                    if self.move(piece, i, j, i + k, j + k) == True:
                        break
                else:
                    break


    # Checks if there is a white piece at the given position
    def has_white_piece(self, i, j):
        # Checking if the piece would go out of bound
        if self.check_bounds(i, j) == False:
            return False
        if self.board[i][j] >= cp.W_PAWN.value and self.board[i][j] <= cp.W_KING.value:
            return True 
        else: 
            return False
    
    # Checks if there is a black piece at the given position
    def has_black_piece(self, i, j):
        # Checking if the piece would go out of bound
        if self.check_bounds(i, j) == False:
            return False
        if self.board[i][j] >= cp.B_PAWN.value and self.board[i][j] <= cp.B_KING.value:
            return True 
        else: 
            return False

    # Performs the actual piece movement and returns a new state with the new board
    def move(self, piece, old_i, old_j, new_i, new_j):
        eaten = False
        #From the current board
        new_board = copy.deepcopy(self.board)

        # Flag = true if the move eats an opponent piece
        if new_board[new_i][new_j] != cp.EMPTY.value:
            eaten = True
        
        # We empty the old position
        new_board[old_i][old_j] = cp.EMPTY.value
        # We move the piece in the new position
        new_board[new_i][new_j] = piece

        # We create a new state using the new modified board
        new_state = ChessState(self.heuristic, new_board)

        # Check if the king is going to be caputerd in the new state for either player
        if self.board[new_i][new_j] == cp.W_KING.value:
            new_state.black_win = True
            new_state.final = True
        if self.board[new_i][new_j] == cp.B_KING.value:
            new_state.white_win = True
            new_state.final = True

        # We compute the heuristica value of the new state
        new_state.compute_value()
        # We append the new state to the horizon of the current state
        self.horizon.append(new_state)
        return eaten

    # Checks wheter the movement will go out of bound of the board
    def check_bounds(self, i, j):
        if i < 0 or i > 7 or j < 0 or j > 7:
            return False
        else:
            return True
    
    # Checks if the piece will fall on a square with a piece of the opponent
    def check_color(self, piece, i, j):
        if piece >= cp.W_PAWN.value and piece <= cp.W_KING.value and self.has_black_piece(i, j):
            return True
        if piece >= cp.B_PAWN.value and piece <= cp.B_KING.value and self.has_white_piece(i, j):
            return True
        return False
    
    # Checks if a given position is empty
    def check_empty(self, i, j):
        if self.board[i][j] == cp.EMPTY.value:
            return True
        return False

    # TODO: Checks if the king will be in check if this move happen
    def is_in_check(self, i, j):
        for k in self.board:
            for y in i:
                True 

    # In this heuristic we count the value of pieces in the board and we add it to the opponent value
    # White pieces values: Pawn = 1, Bishop/Knight = 3, Rook = 5, Queen = 9
    # Black pieces values: Pawn = -1, Bishop/Knight = -3, Rook = -5, Queen = -9
    def piece_value(self):
        for i in range(0, 8):
            for j in range(0, 8):
                # White pieces
                # If this is a winning state for white
                if self.white_win == True:
                    self.value = 999
                    return
                if self.board[i][j] == cp.W_PAWN.value:
                    self.value = self.value + 1
                    continue
                if self.board[i][j] == cp.W_BISHOP.value or self.board[i][j] == cp.W_KNIGHT.value:
                    self.value = self.value + 3
                    continue
                if self.board[i][j] == cp.W_ROOK.value:
                    self.value = self.value + 5
                    continue
                if self.board[i][j] == cp.W_QUEEN.value:
                    self.value = self.value + 9
                    continue
                # Black pieces
                # If this is a winning state for black
                if self.black_win == True:
                    self.value = -999
                    return
                if self.board[i][j] == cp.B_PAWN.value:
                    self.value = self.value - 1
                    continue
                if self.board[i][j] == cp.B_BISHOP.value or self.board[i][j] == cp.B_KNIGHT.value:
                    self.value = self.value - 3
                    continue
                if self.board[i][j] == cp.B_ROOK.value:
                    self.value = self.value - 5
                    continue
                if self.board[i][j] == cp.B_QUEEN.value:
                    self.value = self.value - 9
                    continue

    # In this heuristic we use the same logic as the piece value heurisitc to define how much the pices are worth
    # Then we compute a score from the postion of pieces given an heatmap of the chess board           
    def piece_value_with_positions(self):
        heatmap = [
                    [0.8, 1.2, 1.6, 1.7, 1.6, 1.8, 1.9, 0.5],
                    [0.8, 1.3, 1.4, 2.5, 2.6, 1.3, 1.4, 0.9],
                    [0.9, 1.1, 2.4, 1.8, 1.9, 2.9, 1.3, 1.0],
                    [0.9, 0.4, 1.8, 2.7, 2.8, 1.7, 1.7, 1.1],
                    [0.9, 1.3, 2.0, 2.8, 2.8, 1.8, 1.6, 1.1],
                    [0.8, 1.1, 2.3, 1.8, 1.7, 2.9, 1.2, 1.0],
                    [0.8, 1.1, 1.4, 2.3, 2.4, 1.3, 1.2, 0.9],
                    [0.7, 1.2, 1.5, 1.7, 1.7, 1.8, 1.9, 0.5]
                  ]
        
        for i in range(0, 8):
            for j in range(0, 8):
                # White pieces
                # If this is a winning state for white
                if self.white_win == True:
                    self.value = 999
                    return
                if self.board[i][j] == cp.W_PAWN.value:
                    self.value = round(self.value + 1 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.W_BISHOP.value or self.board[i][j] == cp.W_KNIGHT.value:
                    self.value = round(self.value + 3 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.W_ROOK.value:
                    self.value = round(self.value + 5 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.W_QUEEN.value:
                    self.value = round(self.value + 9 * heatmap[i][j], 4)
                    continue
                # Black pieces
                # If this is a winning state for black
                if self.black_win == True:
                    self.value = -999
                    return
                if self.board[i][j] == cp.B_PAWN.value:
                    self.value = round(self.value - 1 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.B_BISHOP.value or self.board[i][j] == cp.B_KNIGHT.value:
                    self.value = round(self.value - 3 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.B_ROOK.value:
                    self.value = round(self.value - 5 * heatmap[i][j], 4)
                    continue
                if self.board[i][j] == cp.B_QUEEN.value:
                    self.value = round(self.value - 9 * heatmap[i][j], 4)
                    continue
