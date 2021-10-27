import random

# This algorithm selects the max value of the states in the given horizon if it's player 1 turn
# and the min value if it's player 2 turn, it also removes everything else from the horizon
# If the game is balance (value = 0) we pick a random option
def pick(horizon, turn):
    compare = horizon[0].value
    for state in horizon:
        if state.value != compare:
            if turn == False:
                return max(horizon, key=lambda p: p.value), []
            if turn == True:
                return min(horizon, key=lambda p: p.value), []
    
    state = random.choice(horizon)
    return state, []

    