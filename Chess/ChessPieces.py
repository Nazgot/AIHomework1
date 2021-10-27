from enum import Enum

# Enum representing the different chess pieces
class ChessPieces(Enum):
    # Black pieces
    B_PAWN = 1
    B_ROOK = 2
    B_KNIGHT = 3
    B_BISHOP = 4
    B_QUEEN = 5
    B_KING = 6
    # White Pieces
    W_PAWN = 7
    W_ROOK = 8
    W_KNIGHT = 9
    W_BISHOP = 10
    W_QUEEN = 11
    W_KING = 12
    # This represents an empty tile on the board
    EMPTY = 0