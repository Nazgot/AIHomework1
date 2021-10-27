# Greedy 
# This algorithm selects the max value of the states in the given horizon if it's player 1 turn
# and the min value if it's player 2 turn, it also removes everything else from the horizon
def pick(horizon, turn):
    if turn == False:
        return max(horizon, key=lambda p: p.value), []
    if turn == True:
        return min(horizon, key=lambda p: p.value), []