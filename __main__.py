from Config import Config
from Chess.Dataset import Dataset
from Chess.Predict import Predict
from Chess.ChessState import ChessState
from MiniMax import minimax
import numpy as np
import time

def play_match(predict):
    state = ChessState('PIECE_VALUE_WITH_POSITIONS')
    state.base_state()
    game = []

    game_over = False
    turn = False
    count = 0

    while not game_over:
        if count % 1 == 0:
            print("\n-----------------------" + str(count) + "turn: "+ str(turn)+"----------------------\n")
            state.print_board()
        count += 1
        state, value = minimax(state, 1, -np.inf, np.inf, turn, predict)
        game.append(state)

        
        
        if state.final == True:
            game_over = True
            winner = True if state.black_win else False

        turn = not turn
    return winner



def main():
    print("Starting")

    Dataset.read()
    predict = Predict()
    predict.load_model()
    black_wins = 0

    for counter in range(50): 
        print("\nStarting match " + str(counter))
        start = time.time()
        if play_match(predict) == True:
            black_wins +=1
        end = time.time()
        print("\nMatch lasted %d seconds", end - start)

        if Config.TRAINING:
            predict.update_dataset()
            predict.train_model()
            predict.save_model()
    
        Dataset.write()
    
    print("Black wins = " + str(black_wins) + "\nWhite wins = " + str(50-black_wins))


if __name__ == "__main__":
    main()