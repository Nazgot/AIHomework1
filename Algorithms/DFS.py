# DFS is LIFO so we just return the last element from the horizon
def pick(horizon):
    state = horizon[-1]
    horizon.remove(state)
    return state, horizon