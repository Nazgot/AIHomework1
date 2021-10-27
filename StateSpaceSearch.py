from Algorithms import BFS, DFS, Random as rnd, Greedy, GreedyWithRandomness as GreedyR
from Chess import ChessState

# The algorithm assumes that the state passed as parameter is in the starting state of the game
def search(state):
    came_from = []
    # White starts first 
    turn = False
    # Generating the horizon for the white player
    state.generate_horizon(turn)
    horizon = state.horizon
    count = -1
    # While we have states in the horizon
    while len(horizon) > 0:
        #if count == 0:
        #    break
        count += 1
        # We pick a state in the horizon
        picked_state, horizon = GreedyR.pick(horizon, turn)
        # Swapping turn to the opposing player
        turn = not turn 

        came_from.append(picked_state)
        # If the state is final we return
        picked_state.print_board()
        print('\n---------------- Turn#: ' + str(count) + ' - state value: ' + str(picked_state.value) + ' -----------------')
        if picked_state.final == True:
            print("Black Wins" if picked_state.black_win else "White Wins")
            break

        # generating the horizon from the current state
        picked_state.generate_horizon(turn)
        # We add the new horizon to the list of states composing the horizon
        horizon.extend(picked_state.horizon)
        


# Implemented Heuristics: 
# PIECE_VALUE, PIECE_VALUE_WITH_POSITIONS
def main():
    start = ChessState.ChessState('PIECE_VALUE_WITH_POSITIONS')
    start.base_state()
    search(start)

main()
