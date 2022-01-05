from Chess.ChessPieces import ChessPieces as cp

# In this heuristic we count the value of pieces in the board and we add it to the opponent value
# White pieces values: Pawn = 1, Bishop/Knight = 3, Rook = 5, Queen = 9
# Black pieces values: Pawn = -1, Bishop/Knight = -3, Rook = -5, Queen = -9
def piece_value(state):
    for i in range(0, 8):
        for j in range(0, 8):
            # White pieces
            # If this is a winning state for white
            if state.white_win == True:
                state.value = 999
                return
            if state.board[i][j] == cp.W_PAWN.value:
                state.value = state.value + 1
                continue
            if state.board[i][j] == cp.W_BISHOP.value or state.board[i][j] == cp.W_KNIGHT.value:
                state.value = state.value + 3
                continue
            if state.board[i][j] == cp.W_ROOK.value:
                state.value = state.value + 5
                continue
            if state.board[i][j] == cp.W_QUEEN.value:
                state.value = state.value + 9
                continue
            # Black pieces
            # If this is a winning state for black
            if state.black_win == True:
                state.value = -999
                return
            if state.board[i][j] == cp.B_PAWN.value:
                state.value = state.value - 1
                continue
            if state.board[i][j] == cp.B_BISHOP.value or state.board[i][j] == cp.B_KNIGHT.value:
                state.value = state.value - 3
                continue
            if state.board[i][j] == cp.B_ROOK.value:
                state.value = state.value - 5
                continue
            if state.board[i][j] == cp.B_QUEEN.value:
                state.value = state.value - 9
                continue
    
    return state.value
