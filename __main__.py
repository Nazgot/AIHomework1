from Config import Config
from Chess.Dataset import Dataset
from Chess.Predict import Predict
from Chess.ChessState import ChessState
from MiniMax import minimax
import time

def play_match():
    state = ChessState.ChessState('PIECE_VALUE_WITH_POSITIONS')
    state.base_state()
    game = []

    game_over = False
    turn = False
    count = 0

    while not game_over:
        count += 1
        state, value = minimax(state, 3, 1, 1, turn)
        game.push(state)

        if state.final == True:
            game_over = True

        turn = not turn



def main():

    Dataset.load()
    predict = Predict()
    predict.load_model()

    for counter in range(50): 
        print("\nStarting match " + counter)
        start = time.time()
        play_match()
        end = time.time()
        print("\nMatch lasted %d seconds", end - start)

        if Config.TRAINING_MODE:
            predict.update_dataset()
            predict.train_model()
            predict.save_model()
    
        Dataset.dump()


if __name__ == "__main__":
    main()