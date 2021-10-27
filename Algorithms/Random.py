import random

# We just pick a random state to proceed the game
def pick(horizon):
    state = random.choice(horizon)
    horizon.remove(state)
    return state, horizon