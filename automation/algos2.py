def symmetric(state):
    odds = []
    for i in range(7):
        if state.state[i] % 2 == 1:
            odds.append(i)
    assert len(odds) == 2, f"L'algorithme symétrique n'a pas pu s'appliquer dans la situation {state.state}"
    return tuple(odds)


def improved_symmetric(state):
    if state.state == [0, 0, 0, 0, 0, 1, 5]:
        return 5, 6
    if state.state[6] < 4:
        return symmetric(state)
    elif state.state[6] == 4:
        if state.state[5] == 0:
            return symmetric(state)
        elif state.state[5] == 1:
            return state.state.index(1), 6
        else:
            return 5, 6
    else:
        return state.state.index(1), 5


def improved_symmetric_v2(state):
    if state.state[5] + state.state[6] == 6:
        return 5, 6
    elif state.state[5] + state.state[6] == 5:
        if state.state[5] % 2 == 1:
            return state.state.index(1), 6
        else:
            return state.state.index(1), 5
    else:
        return symmetric(state)


algos2 = {"sym": symmetric, "symp": improved_symmetric, "symp_v2": improved_symmetric_v2}
