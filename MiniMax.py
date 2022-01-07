import numpy as np
from Chess.Dataset import Dataset
from Chess.Predict import Predict
from Heuristics.PieceValue import piece_value
from Heuristics.PieceValueWithPositions import piece_value_with_positions

def minimax(state, depth, alpha, beta, turn, predict):
    if turn == False:
        return maxi(state, depth, alpha, beta, turn, predict)
    else:
        return mini(state, depth, alpha ,beta, turn, predict)


def maxi(state, depth, alpha, beta, turn, predict):
    if depth == 0 or state.final == True:
        h1 = piece_value(state) if not turn else - piece_value(state)
        h2 = piece_value_with_positions(state) if not turn else - piece_value_with_positions(state)
        features = predict.scale([[h1, h2]])
        evaluation = predict.model.predict(features)[0][0]

        values = [h1, h2, evaluation]
        Dataset.data.append(values)

        return state, evaluation
    
    maximum = -np.inf
    best_state = state
    state.generate_horizon(turn)
    horizon = state.horizon

    for state in horizon:
        mini_best_state, score = mini(state, depth - 1, alpha, beta, turn, predict)
        if score > maximum:
            maximum = score
            best_state = mini_best_state
        alpha = max(alpha, score)
        if beta <= alpha:
            break
    
    return best_state, maximum


def mini(state, depth, alpha, beta, turn, predict):
    if depth == 0 or state.final == True:
        h1 = piece_value(state) if not turn else - piece_value(state)
        h2 = piece_value_with_positions(state) if not turn else - piece_value_with_positions(state)
        features = predict.scale([[h1, h2]])
        evaluation = predict.model.predict(features)[0][0]

        values = [h1, h2, evaluation]
        Dataset.data.append(values)
        
        return state, evaluation
    
    minimum = np.inf
    best_state = state
    state.generate_horizon(turn)
    horizon = state.horizon

    for state in horizon:
        maxi_best_state, score = maxi(state, depth - 1, alpha, beta, turn, predict)
        if score < minimum:
            minimum = score
            best_state = maxi_best_state
        beta = min(beta, score)
        if beta <= alpha:
            break    
    return best_state, minimum
