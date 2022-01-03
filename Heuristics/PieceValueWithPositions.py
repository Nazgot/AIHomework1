from Chess.ChessPieces import ChessPieces as cp

# In this heuristic we use the same logic as the piece value heurisitc to define how much the pices are worth
# Then we compute a score from the postion of pieces given an heatmap of the chess board
def piece_value_with_positions(state):
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
            if state.white_win == True:
                state.value = 999
                return
            if state.board[i][j] == cp.W_PAWN.value:
                state.value = round(state.value + 1 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.W_BISHOP.value or state.board[i][j] == cp.W_KNIGHT.value:
                state.value = round(state.value + 3 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.W_ROOK.value:
                state.value = round(state.value + 5 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.W_QUEEN.value:
                state.value = round(state.value + 9 * heatmap[i][j], 4)
                continue
            # Black pieces
            # If this is a winning state for black
            if state.black_win == True:
                state.value = -999
                return
            if state.board[i][j] == cp.B_PAWN.value:
                state.value = round(state.value - 1 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.B_BISHOP.value or state.board[i][j] == cp.B_KNIGHT.value:
                state.value = round(state.value - 3 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.B_ROOK.value:
                state.value = round(state.value - 5 * heatmap[i][j], 4)
                continue
            if state.board[i][j] == cp.B_QUEEN.value:
                state.value = round(state.value - 9 * heatmap[i][j], 4)
                continue
