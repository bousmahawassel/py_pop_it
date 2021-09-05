def symetric(state):
    odds = []
    for i in range(7):
        if state.state[i] % 2 == 1:
            odds.append(i)
    assert len(odds) == 2, f"L'algorithme symétrique n'a pas pu s'appliquer dans la situation {state.state}"
    return tuple(odds)


def improved_symetric(state):
    if state.state == [0, 0, 0, 0, 0, 1, 5]:
        return 5, 6
    if state.state[6] < 4:
        return symetric(state)
    elif state.state[6] == 4:
        if state.state[5] == 0:
            return symetric(state)
        elif state.state[5] == 1:
            print(state.state.index(1))
            return state.state.index(1), 6
        else:
            return 5, 6
    else:
        return state.state.index(1), 5


def improved_symetric_v2(state):
    if state.state[5] + state.state[6] == 6:
        return 5, 6
    elif state.state[5] + state.state[6] == 5:
        if state.state[5] == 0:
            return state.state.index(1), 5
        elif state.state[5] % 2 == 1:
            return state.state.index(1), 6
        else:
            return state.state.index(1), 5
    else:
        return symetric(state)


algos2 = {"sym": symetric, "symp": improved_symetric, "symp_v2": improved_symetric_v2}
