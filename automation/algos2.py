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
        print(state.state.index(1))
        return state.state.index(1), 5


algos2 = {"symetric": symetric, "imp_symetric": improved_symetric}
