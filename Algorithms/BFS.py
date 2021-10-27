# BFS is FIFO so we just return the 0-element that was the first to enter the horizon
def pick(horizon):
    state = horizon[0]
    horizon.remove(state)
    return state, horizon