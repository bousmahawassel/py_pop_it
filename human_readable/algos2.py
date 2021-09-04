import numpy as np


def symetric(board, last_move):
    col, rows = last_move
    return 5 - col, rows


def intelligent_symetric(board, last_move):
    not_full_cols = []
    for col in range(6):
        if not board[:, col].all():
            not_full_cols.append(col)
    if len(not_full_cols) > 2:
        return symetric(board, last_move)
    elif len(not_full_cols) == 1:
        print(not_full_cols)
        col = board[:, not_full_cols[0]]
        print(col)
        zeros = np.where(col == 0)[0]
        print(zeros)
        zeros = np.delete(zeros, 0)
        print(zeros)
        return not_full_cols[0], list(zeros)
    else:
        if board[:, not_full_cols[0]].sum() == 5:
            return not_full_cols[1],
        elif board[:, not_full_cols[1]].sum() == 5:
            return not_full_cols[0],
        else:
            return symetric(board, last_move)


algos2 = {"symétrique": symetric, "symétrique intelligent": intelligent_symetric}
